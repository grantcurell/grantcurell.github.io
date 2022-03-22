#!/bin/sh

numjobs="8"
iodepth="128"

for i in `seq 0 1 11`
do
	if [[ $i -le 11 ]]
	then
		numa_str="--numa_mem_policy=bind:2,6,10,14,18,22,26,30,34,38,42,46,50,54,58,62,66,70,74,78 --numa_cpu_nodes=2,6,10,14,18,22,26,30,34,38,42,46,50,54,58,62,66,70,74,78"
	else
		numa_str="--numa_mem_policy=bind:3,7,11,15,19,23,27,31,35,39,43,47,51,55,59,63,67,71,75,79 --numa_cpu_nodes=3,7,11,15,19,23,27,31,35,39,43,47,51,55,59,63,67,71,75,79"
	fi
	fio --filename=/dev/nvme${i}n1 --ioengine=libaio --iodepth=$iodepth \
	    --direct=1 --ramp_time=10s --time_based --runtime=2m --rw=read \
	    --name=foo --numjobs=$numjobs --bs=1m $numa_str &
done 
