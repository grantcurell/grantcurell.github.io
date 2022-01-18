# Title

## My Setup

### OS Version



## Description of the Problem

What we are doing in the below steps is playing a packet from one Mellanox card directly into another. Before playing the packet, we write to a region in GPU memory with a specific pattern and in the packet we send we have a different pattern. As a proof of concept we expect that the packet's data overwrites this memory buffer.

See [this post](https://forums.developer.nvidia.com/t/clarification-on-requirements-for-gpudirect-rdma/188114) for the original description of the problem.

1. A queue pair and its associated resources are established exactly as described in the (generic application flow)[https://docs.nvidia.com/networking/display/RDMAAwareProgrammingv17/Typical+Application]
  1. Lines 0-192 of the attached code
2. Register a region of host memory and fill it with a known pattern
   1. lines 192-195
3. ​Register a region of GPU memory 
   1. Lines 197-223
4. Send a packet containing a known pattern from one Mellanox device to another
   1. Lines 223-375
5. Copy the data from the GPU device's memory region into the host system memory which we expect to overwrite the host system memory's bit pattern with the one we just sent
   1. Line 375-380
6. Confirm that the memory patterns match. The idea being that we just sent a *new* pattern from one Mellanox device to the other and then told it to overwrite the pattern that was already in system memory with what the GPU received. The logic being that we expect the pattern which was in system memory to be overwritten by what was just sent.
   1. This happens in lines 391-396​

 At no point does the CUDA toolkit issue any errors. Everything returns as a success however, the pattern in system memory *is not* overwritten. Need to determine why this simple POC does not work in order to move forward with customer.