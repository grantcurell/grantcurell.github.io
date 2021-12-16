# Nvidia GPUDirect

## Background Research

See [Background Research](./background_research.md) for background information I studied before doing this.

## Source Code

See [the test file](test_code/rdma-loopback.cpp)

## Test Scenario

We would like to use GPDirect RDMA to write packets coming directly off of a Mellanox card into GPU memory.

## Lab Configuration

### Hardware Configuration

Dell R750 with a Mellanox MLX6 as the transmitting device and a MLX5 as the receiving device.

### RHEL Version

```
NAME="Red Hat Enterprise Linux"
VERSION="8.5 (Ootpa)"
ID="rhel"
ID_LIKE="fedora"
VERSION_ID="8.5"
PLATFORM_ID="platform:el8"
PRETTY_NAME="Red Hat Enterprise Linux 8.5 (Ootpa)"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:redhat:enterprise_linux:8::baseos"
HOME_URL="https://www.redhat.com/"
DOCUMENTATION_URL="https://access.redhat.com/documentation/red_hat_enterprise_linux/8/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"

REDHAT_BUGZILLA_PRODUCT="Red Hat Enterprise Linux 8"
REDHAT_BUGZILLA_PRODUCT_VERSION=8.5
REDHAT_SUPPORT_PRODUCT="Red Hat Enterprise Linux"
REDHAT_SUPPORT_PRODUCT_VERSION="8.5"
Red Hat Enterprise Linux release 8.5 (Ootpa)
Red Hat Enterprise Linux release 8.5 (Ootpa)

```

### GCC Version

```
[root@gputest ~]# gcc --version
gcc (GCC) 8.5.0 20210514 (Red Hat 8.5.0-4)
Copyright (C) 2018 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

## Installation

### MLNX_OFED

1. Download MLNX_OFED drivers from https://www.mellanox.com/products/infiniband-drivers/linux/mlnx_ofed
   1. MLNX_OFED is version dependent. I suggest you use  `subscription-manager release --set=8.4` to ensure your version of RHEL stays at the version for which MLNX_OFED was compiled
2. Upload the ISO to the target box
3. Run:

```bash
dnf group install "Development Tools" -y
dnf install -y tk tcsh tcl gcc-gfortran kernel-modules-extra gcc-g++ gdb rsync ninja-build make zip
mount MLNX* /mnt
cd /mnt
./mlnxofedinstall
```

### CUDA Development Packages

1. Make sure you have an Nvidia GPU that shows on the device with `lspci | grep -i nvidia`
2. Make sure you have the kernel dev headers for your kernel. with `rpm -qa | grep devel | grep kernel && uname -r`
3. Run the following (See [Nvidia's instructions](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=RHEL&target_version=8&target_type=rpm_local) for details):

```bash
dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
subscription-manager repos --enable=rhel-8-for-x86_64-appstream-rpms
subscription-manager repos --enable=rhel-8-for-x86_64-baseos-rpms
subscription-manager repos --enable=codeready-builder-for-rhel-8-x86_64-rpms
sudo rpm -i cuda-repo-rhel8-11-5-local-11.5.1_495.29.05-1.x86_64.rpm
sudo dnf config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-rhel8.repo
sudo dnf clean expire-cache
sudo dnf module install -y nvidia-driver:latest-dkms
sudo dnf install -y cuda
export PATH=/usr/local/cuda-11.5/bin${PATH:+:${PATH}}
echo 'export PATH=/usr/local/cuda-11.5/bin${PATH:+:${PATH}}' >> /root/.bashrc
```

### Prepare the Code

First we need to make some manual adjustments to some parameters in the code. For this you need the MAC addresses

### Compiling and Running the App

```bash
g++ rdma-loopback.cc -o rdma-loopback -libverbs -I/usr/local/cuda/include -L/usr/local/cuda/lib64 -lcudart
```
