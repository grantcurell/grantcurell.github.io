# Grant Curell's Dell Projects

Every time Dell asks me to figure something out, I write it down. Mostly because more often than not someone asks me about it a year later and I have to remember what I did.

## Questions

If you have any questions about something I did, open an issue on the repo at [grantcurell.github.io](https://github.com/grantcurell/grantcurell.github.io/issues) or write me at `grant_curell AT dell dot com`.

## Additional Files

Most of the files I use in the projects are linked from the markdown documentation but often there might be additional files not visible for this site. It may be easier to browse to the [actual docs folder](https://github.com/grantcurell/grantcurell.github.io/tree/master/docs) and look at the appropriate folder.

## Disclaimer

These are just my personal notes for the random things I test. I'm generally thorough,
but there is no guarentee on completeness :-D

## How to Configure ONIE

I ran the network version of the ONIE installation using a web server. Below
is what I did to get things installed. We will host the OS installer on our
web server and then we will use ONIE to grab it. We will use a DNS record to 
control the ONIE server location.

1. Install Apache on RHEL or your favorite Linux distro.
2. Make sure you allow HTTP traffic through the firewall
3. Download your operating system of choice and untar it.
4. Upload `<YOUR INSTALLER>.bin` to the root of your web server.
5. Create a symlink to the installer with `ln -s <YOUR INSTALLER>.bin onie-installer`. The file must have this name for the installation to work.
6. The switch will use DHCP to acquire an IP address. On the DNS server pointed to by your DHCP configuration, add a record for onie-server and point it at the host running Apache.

On a test box, run a DHCP request, ensure you pull the correct DNS server and that the host can resolve `onie-server`. After you confirm DNS is working, browse to the onie-installer file
on your Apache server and make sure you can download it without issue.

**Warning:** It must be able to resolve the hostname onie-server with the FQDN.
If `onie-server` is not immediately resolvable, the install process will not work.

## ONIE Boot the Switch

1. Connect to the switch over the console port. My configuration was:

        Baud Rate: 115200
        Data Bits: 8
        Stop Bits: 1
        Parity: None
        Flow Control: None

2. Connect the ethernet management port of the switch to the same network containing your web server. ONIE will use the management port to establish a connection to the ONIE server.
3. Once the grub menu appears, select ONIE Installer. In my case this was the top option.
4. At this point the ONIE discovery process will commence. It will print each location it attempts to search. It should find the onie-server DNS record and the installation should begin automatically. If this doesn't happen it means there is an issue with the preconfiguration above. Try swapping out the ethernet management cable with a host. Make sure that host pulls DNS/DHCP correctly and is able to download the onie-installer file.
5. Wait for the installation to finish and the switch to reboot. Login with admin/admin.
6. If after logging in you are told you can't enter configuration mode because "% Error: ZTD is in progress(configuration is locked)." run `ztd cancel`

## Configure Managment Interface on Dell OS10

Do the following to configure a management interface on Dell OS10

    OS10# configure terminal
    OS10(config)# interface mgmt 1/1/1
    OS10(conf-if-ma-1/1/1)# ip address 192.168.1.20/24
    OS10(conf-if-ma-1/1/1)# <165>1 2019-10-28T19:04:39.385196+00:00 OS10 dn_alm 669 - - Node.1-Unit.1:PRI [event], Dell EMC (OS10) %IP_ADDRESS_ADD: IP Address add is successful. IP 192.168.1.20/24 in VRF:default added successfully
    OS10(conf-if-ma-1/1/1)# do write memory