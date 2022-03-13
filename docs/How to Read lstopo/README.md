# How to Read lstopo

The first time I looked at `lstopo`, I found the output rather overwhelming so I wrote this guide to break down what I was looking at.

## Subject Platform

Dell R840

![](images/2022-03-13-11-44-05.png)

### Package

The word package is synonymous with the word socket. In the R840's case there are four separate, physical, sockets.

### Caches (LXi, LXd, and L3)

This in particular confused me at first as the nomenclature is specific to your architecture (ex: Intel or AMD). Here you see three caches LXi, LXd, and L3. L<some_number>i refers to an [instruction cache](./images/18-notes.pdf), L<some_number>d refers to a [data cache](./images/18-notes.pdf), and L3 is a mixed cache including data and instructions. In the Intel architecture the first couple of levels may be dedicated to data or instruction caches but higher levels are mixed.

### Cores

It helps here to look at the output of `lscpu`

```
[root@r8402 ~]# lscpu
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              80
On-line CPU(s) list: 0-79
Thread(s) per core:  2
Core(s) per socket:  10
Socket(s):           4
NUMA node(s):        4
Vendor ID:           GenuineIntel
BIOS Vendor ID:      Intel
CPU family:          6
Model:               85
Model name:          Intel(R) Xeon(R) Gold 5215 CPU @ 2.50GHz
BIOS Model name:     Intel(R) Xeon(R) Gold 5215 CPU @ 2.50GHz
Stepping:            7
CPU MHz:             2643.471
CPU max MHz:         3400.0000
CPU min MHz:         1000.0000
BogoMIPS:            5000.00
Virtualization:      VT-x
L1d cache:           32K
L1i cache:           32K
L2 cache:            1024K
L3 cache:            14080K
NUMA node0 CPU(s):   0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76
NUMA node1 CPU(s):   1,5,9,13,17,21,25,29,33,37,41,45,49,53,57,61,65,69,73,77
NUMA node2 CPU(s):   2,6,10,14,18,22,26,30,34,38,42,46,50,54,58,62,66,70,74,78
NUMA node3 CPU(s):   3,7,11,15,19,23,27,31,35,39,43,47,51,55,59,63,67,71,75,79
```

First we need to understand a bit about computer architecture. In modern servers, you have the physical processors, cores within those processors, and finally logical cores (due to HyperThreading in Intel architectures ar Simultaneous Multi-Threading [SMT] in AMD architectures). AS you can see from the output of `lscpu`, in my server, each processor has 10 cores and each of those cores, due to hyperthreading, has 20 logical cores (as indicated by the NUMA node field). What you are seeing in this part:

![](images/2022-03-13-13-08-53.png)

are the 10 cores in each proc. Notice that the numbers are in ascending order starting with package L#0 which has cores 0-9, then L#1 has 10-19, on up to 39 in package L#3. Also notice that the output omits some of the procs for space reasons and simply says "10x total" to indicate that there are actually 10 procs total.

You can see that each individual core:

![](images/2022-03-13-13-16-36.png)

Further has PU L#0 and PU L#1. These refer to the two aforementioned logacl cores created from hyperthreading. 

#### NUMA Nodes

Perhaps more confusing are the smaller numbers. In package L#0 we see P#0, P#4, P#36, P#40, P#44, and P#76 actually drawn. As other posts have mentioned, these correspond to the various [NUMA Nodes](https://en.wikipedia.org/wiki/Non-uniform_memory_access#Cache_coherent_NUMA_(ccNUMA)). As mentioned in Wikipedia, modern architectures use some sort of cache coherent NUMA (ccNUMA). The subject can be quite complicated but a simple explanation is this: we want memory access to be faster. The best way to do this is to literally put the memory closer to the processor. NUMA nodes do this by directly attaching processors to some part of memory. The smaller numbers indicate the logical cores created by HyperThreading. From the output of `lscpu` you can see that all the logical processes shown in package L#0:

![](images/2022-03-13-13-46-09.png)

are included in NUMA node 0. You may also notice at the top it says NUMANode L#0 P#0 (45GB). This refers to the fact that NUMA node 0 has direct access to 1/4 of the total memory or 45GB. We can confirm this by looking at `cat /proc/meminfo`:

```
[root@r8402 ~]# cat /proc/meminfo
MemTotal:       196207488 kB
MemFree:        191452708 kB
MemAvailable:   191700740 kB
...SNIP...
```

In our example, if a process is running on Core L#0, logical processor P#36, then it can directly access any of the 45GBs directly attached to package L#0. An important note: modern operating systems are NUMA aware and will do their absolute best when you spawn a process to make sure that the memory allocated for that process will be on the same NUMA node. However, let's say that there is some larger process and that multiple threads are sharing access to memory. In this case you may have a scenario where a process is running on logical processor P#5 on package L#1 in which case that process will have to reach out from physical package of L#1 through what's called the [QPI](https://en.wikipedia.org/wiki/Intel_QuickPath_Interconnect) bus, through package L#0, and then gain access to the memory local to package L#0. The [QPI bus](https://en.wikipedia.org/wiki/Intel_QuickPath_Interconnect) is part of the Intel architecture and it provides interconnects between all the physical packages for exactly this purpose. AMD uses something called XGMI. This gets us pretty in the weeds on computer architecture because this actually changes over time. For example, on Intel's newer Skylake processors it is no longer the QPI bus but [ULtra Path Interconnect](https://en.wikipedia.org/wiki/Intel_Ultra_Path_Interconnect) that serves this function so when you're working at this level you have to pay attention to exactly what processor you are using.

Fun fact: When looking at things like [the Technical Guide](https://i.dell.com/sites/csdocuments/Product_Docs/en/dell-emc-poweredge-r7525-technical-guide.pdf) for servers you have to account for this when looking at total PCIe lane availability. The AMD EPYC gen 2/3 processors both support up to 128 PCIe lanes per processor BUT this is a bit misleading. When you have servers like the Dell R7525 (or any other vendor's two socket AMD server like HP's DL385) the two procs are connected via XGMI however XGMI consumes 48 PCIe lanes *per processor* so when doing your calculus you actually only end up seeing 80 per processor for a total of 160.

### PCIe

The last part of the diagram we haven't touched on is PCIe. Not to be confused with NUMA, PCIe devices also have locality to processors. Each processor has a certain number of PCIe lanes attached directly to it. Just like memory, if you have a process running on, let's say, package L#3 and it is writing to NVMe drive nvme3n1 that process will write more quickly than a process running on package L#0 which must write across the QPI bus, through package L#3, and then to the drive.

To fully understand how to interpret the PCIe results, it helps to understand a few PCIe basics.

#### PCIe Root Complex

All PCIe Express (PCIe) devices connect to the processor and memory through what is called the [PCIe root complex](https://en.wikipedia.org/wiki/Root_complex)

![](images/2022-03-13-14-39-27.png)


## Research

### Translation Lookaside Buffer

See: https://en.wikipedia.org/wiki/Translation_lookaside_buffer

A translation lookaside buffer (TLB) is a memory cache that is used to reduce the time taken to  access a user memory location.[1] It is a part of the chip's memory-management unit (MMU). The TLB stores the recent translations of virtual memory to physical memory and can be called an address-translation cache. A TLB may reside between the CPU and the CPU cache, between CPU cache and the main memory or between the different levels of the multi-level cache. The majority of desktop, laptop, and server processors include one or more TLBs in the memory-management hardware, and it is nearly always present in any processor that utilizes paged or segmented virtual memory.

#### TLB Misses

See [18-notes.pdf](./images/18-notes.pdf)

### Data and Instruction Caches

See [18-notes.pdf](./images/18-notes.pdf)

### StackExchange Explanaton of `lstopo`

https://unix.stackexchange.com/a/113549/240147