# Notes on ID-Based Ordering
## Notes on PCIe

### Human readable overview of how PCIe works

http://xillybus.com/tutorials/pci-express-tlp-pcie-primer-tutorial-guide-1/
http://xillybus.com/tutorials/pci-express-tlp-pcie-primer-tutorial-guide-2

### How does ID-based Ordering (IDO) Work?

https://blog.csdn.net/weixin_48180416/article/details/115790068

### How does transaction ordering work?

https://blog.csdn.net/weixin_40357487/article/details/120162461?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&utm_relevant_index=1

### What is a PCIe Root Complex?

https://www.quora.com/What-is-a-PCIe-root-complex?share=1

### How does PCIe Enumeration Work?

https://www.quora.com/What-is-PCIE-enumeration/answer/Satish-Kumar-525?ch=15&oid=31389493&share=44585235&target_type=answer

### NVMe over PCIe vs Other Protocols

https://www.quora.com/Is-NVMe-faster-than-PCIe/answer/Mike-Jones-169?ch=15&oid=193548046&share=a587ff45&target_type=answer

### What is a PCIe Function?

https://www.quora.com/What-is-a-PCIe-function/answer/Udit-Khanna-2?ch=15&oid=58319695&share=c7f066e5&target_type=answer

### PCIe-Bus and NUMA Node Correlation

https://social.msdn.microsoft.com/Forums/en-US/fabb05b7-eb3f-4a7c-91c5-1ced90af3d0c/pciebus-and-numanode-correlation

### How does the root complex work?

https://codywu2010.wordpress.com/2015/11/29/how-modern-multi-processor-multi-root-complex-system-assigns-pci-bus-number/

### What is PCIe P2P?

https://xilinx.github.io/XRT/master/html/p2p.html

### What is Relaxed Ordering

https://qr.ae/pG6SWe

### What is a traffic class (TC)?

https://www.oreilly.com/library/view/pci-express-system/0321156307/0321156307_ch06lev1sec6.html

### PCIe BAR Register

https://github.com/cirosantilli/linux-kernel-module-cheat/blob/366b1c1af269f56d6a7e6464f2862ba2bc368062/kernel_module/pci.c

## How NVMe Drive Opcodes Work

https://stackoverflow.com/questions/30190050/what-is-the-base-address-register-bar-in-pcie
https://stackoverflow.com/questions/19006632/how-is-a-pci-pcie-bar-size-determined

- BIOS/OS discovers whether PCIe device exists
- Places the addresses for mmio or I/O port addresses in NVMe drive​'s BAR registers (which it figures out from the configuration registers)
- It seems from the documentation I found NVMe does this through 64bit mmio
- Driver establishes the admin queue via BAR0. The admin queue's base addresses are in ASQ and ACQ respectively
- I submit commands to the admin submission queue to establish I/O queues.
- Send/receive data via I/O queues.

## How does SR-IOV work?

https://docs.microsoft.com/en-us/windows-hardware/drivers/network/overview-of-single-root-i-o-virtualization--sr-iov-

Architecture: https://docs.microsoft.com/en-us/windows-hardware/drivers/network/sr-iov-architecture

