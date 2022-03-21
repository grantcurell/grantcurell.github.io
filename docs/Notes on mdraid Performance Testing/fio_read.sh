#!/bin/sh

numjobs="8"
iodepth="128"

for i in `seq 0 1 23`
do
	if [[ $i -le 11 ]]
	then
		numa_str="--numa_mem_policy=bind:0-7 --numa_cpu_nodes=0-7"
		#numa_str="--numa_mem_policy=bind:0 --numa_cpu_nodes=0"
	else
		numa_str="--numa_mem_policy=bind:8-15 --numa_cpu_nodes=8-15"
		#numa_str="--numa_mem_policy=bind:1 --numa_cpu_nodes=1"
	fi
	fio --filename=/dev/nvme${i}n1 --ioengine=libaio --iodepth=$iodepth \
	    --direct=1 --ramp_time=10s --time_based --runtime=2m --rw=read \
	    --name=foo --numjobs=$numjobs --bs=1m $numa_str &
done 
