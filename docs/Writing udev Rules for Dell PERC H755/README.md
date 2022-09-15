
## /etc/udev/rules.d/99-abj.nr.rules

        KERNEL=="sd*",ACTION=="add|change",ATTRS{model}=="PERC_H755N_Front",\
                    ATTR{queue/nomerges}="2",\
                    ATTR{queue/nr_requests}="1023",\
                    ATTR{queue/rotational}="0",\
                    ATTR{queue/rq_affinity}="2",\
                    ATTR{queue/scheduler}="none",\
                    ATTR{queue/add_random}="0",ATTR{queue/max_sectors_kb}="4096"
        KERNEL=="sd*",ACTION=="add|change",ATTRS{model}=="Dell Ent NVMe v2",\
                    ATTR{queue/nomerges}="2",\
                    ATTR{queue/nr_requests}="1023",\
                    ATTR{queue/rotational}="0",\
                    ATTR{queue/rq_affinity}="2",\
                    ATTR{queue/scheduler}="none",\
                    ATTR{queue/add_random}="0",ATTR{queue/max_sectors_kb}="4096"
        SUBSYSTEM=="block",ACTION=="add|change",KERNEL=="nvme*[0-9]n*[0-9]",ATTRS{model}=="Dell Ent NVMe v2 AGN RI U.2 1.92TB",\
                    ATTR{queue/nomerges}="2",\
                    ATTR{queue/nr_requests}="1023",\
                    ATTR{queue/rotational}="0",\
                    ATTR{queue/rq_affinity}="2",\
                    ATTR{queue/scheduler}="none",\
                    ATTR{queue/add_random}="0",\
                    ATTR{queue/max_sectors_kb}="4096"
        SUBSYSTEM=="block",ACTION=="add|change",KERNEL=="md*",\
                    ATTR{md/sync_speed_max}="2000000",\
                    ATTR{md/group_thread_cnt}="64",\
                    ATTR{md/stripe_cache_size}="8192",\
                    ATTR{queue/nomerges}="2",\
                    ATTR{queue/nr_requests}="1023",\
                    ATTR{queue/rotational}="0",\
                    ATTR{queue/rq_affinity}="2",\
                    ATTR{queue/scheduler}="none",\
                    ATTR{queue/add_random}="0", ATTR{queue/max_sectors_kb}="4096"

## `udevadm test --action="add" /sys/block/sdc` with custom rules

        [root@r7525 rules.d]# udevadm test --action="add" /sys/block/sdc
        calling: test
        version 239 (239-58.el8)
        This program is for debugging only, it does not run any program
        specified by a RUN key. It may show incorrect results, because
        some values may be different, or not available at a simulation run.

        Load module index
        Parsed configuration file /usr/lib/systemd/network/99-default.link
        Created link configuration context.
        ...SNIP...
        Reading rules file: /etc/udev/rules.d/99-abj.nr.rules
        Reading rules file: /usr/lib/udev/rules.d/99-qemu-guest-agent.rules
        Reading rules file: /usr/lib/udev/rules.d/99-systemd.rules
        Reading rules file: /usr/lib/udev/rules.d/99-vmware-scsi-udev.rules
        rules contain 393216 bytes tokens (32768 * 12 bytes), 48613 bytes strings
        47970 strings (396524 bytes), 43723 de-duplicated (352159 bytes), 4248 trie nodes used
        GROUP 6 /usr/lib/udev/rules.d/50-udev-default.rules:59
        IMPORT 'scsi_id --export --whitelisted -d /dev/sdc' /usr/lib/udev/rules.d/60-persistent-storage.rules:50
        starting 'scsi_id --export --whitelisted -d /dev/sdc'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_SCSI=1'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_VENDOR=NVMe'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_VENDOR_ENC=NVMe\x20\x20\x20\x20'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_MODEL=Dell_Ent_NVMe_v2'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_MODEL_ENC=Dell\x20Ent\x20NVMe\x20v2'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_REVISION=.2.0'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_TYPE=disk'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_SERIAL=236435330529024150025384100000002'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_SERIAL_SHORT=36435330529024150025384100000002'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_SCSI_SERIAL=S6CSNA0R902415      '
        Process 'scsi_id --export --whitelisted -d /dev/sdc' succeeded.
        LINK 'disk/by-id/scsi-236435330529024150025384100000002' /usr/lib/udev/rules.d/60-persistent-storage.rules:52
        IMPORT builtin 'path_id' /usr/lib/udev/rules.d/60-persistent-storage.rules:73
        LINK 'disk/by-path/pci-0000:01:00.0-scsi-0:2:8:0' /usr/lib/udev/rules.d/60-persistent-storage.rules:75
        IMPORT builtin 'blkid' /usr/lib/udev/rules.d/60-persistent-storage.rules:90
        probe /dev/sdc raid offset=0
        IMPORT '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw' /usr/lib/udev/rules.d/61-scsi-sg3_id.rules:17
        starting '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw'(out) 'SCSI_TPGS=0'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw'(out) 'SCSI_TYPE=disk'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw'(out) 'SCSI_VENDOR=NVMe'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw'(out) 'SCSI_VENDOR_ENC=NVMe\x20\x20\x20\x20'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw'(out) 'SCSI_MODEL=Dell_Ent_NVMe_v2'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw'(out) 'SCSI_MODEL_ENC=Dell\x20Ent\x20NVMe\x20v2'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw'(out) 'SCSI_REVISION=.2.0'
        Process '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw' succeeded.
        IMPORT '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/vpd_pg80 --raw' /usr/lib/udev/rules.d/61-scsi-sg3_id.rules:27
        starting '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/vpd_pg80 --raw'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/vpd_pg80 --raw'(out) 'SCSI_IDENT_SERIAL=S6CSNA0R902415'
        Process '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/vpd_pg80 --raw' succeeded.
        IMPORT '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/vpd_pg83 --raw' /usr/lib/udev/rules.d/61-scsi-sg3_id.rules:30
        starting '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/vpd_pg83 --raw'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/vpd_pg83 --raw'(out) 'SCSI_IDENT_LUN_EUI64=36435330529024150025384100000002'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/vpd_pg83 --raw'(out) 'SCSI_IDENT_PORT_NAA_LOCAL=3bd790c2eff1ebd9'
        Process '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/vpd_pg83 --raw' succeeded.
        IMPORT 'fc_wwpn_id /devices/pci0000:00/0000:00:01.1/0000:01:00.0/host0/target0:2:8/0:2:8:0/block/sdc' /usr/lib/udev/rules.d/63-fc-wwpn-id.rules:8
        starting 'fc_wwpn_id /devices/pci0000:00/0000:00:01.1/0000:01:00.0/host0/target0:2:8/0:2:8:0/block/sdc'
        Process 'fc_wwpn_id /devices/pci0000:00/0000:00:01.1/0000:01:00.0/host0/target0:2:8/0:2:8:0/block/sdc' succeeded.
        LINK 'disk/by-id/scsi-SNVMe_Dell_Ent_NVMe_v2_S6CSNA0R902415' /usr/lib/udev/rules.d/63-scsi-sg3_symlink.rules:12
        LINK 'disk/by-id/scsi-236435330529024150025384100000002' /usr/lib/udev/rules.d/63-scsi-sg3_symlink.rules:25
        ATTR '/sys/devices/pci0000:00/0000:00:01.1/0000:01:00.0/host0/target0:2:8/0:2:8:0/block/sdc/queue/nomerges' writing '2' /etc/udev/rules.d/99-abj.nr.rules:14
        ATTR '/sys/devices/pci0000:00/0000:00:01.1/0000:01:00.0/host0/target0:2:8/0:2:8:0/block/sdc/queue/nr_requests' writing '1023' /etc/udev/rules.d/99-abj.nr.rules:14
        ATTR '/sys/devices/pci0000:00/0000:00:01.1/0000:01:00.0/host0/target0:2:8/0:2:8:0/block/sdc/queue/rotational' writing '0' /etc/udev/rules.d/99-abj.nr.rules:14
        ATTR '/sys/devices/pci0000:00/0000:00:01.1/0000:01:00.0/host0/target0:2:8/0:2:8:0/block/sdc/queue/rq_affinity' writing '2' /etc/udev/rules.d/99-abj.nr.rules:14
        ATTR '/sys/devices/pci0000:00/0000:00:01.1/0000:01:00.0/host0/target0:2:8/0:2:8:0/block/sdc/queue/scheduler' writing 'none' /etc/udev/rules.d/99-abj.nr.rules:14
        ATTR '/sys/devices/pci0000:00/0000:00:01.1/0000:01:00.0/host0/target0:2:8/0:2:8:0/block/sdc/queue/add_random' writing '0' /etc/udev/rules.d/99-abj.nr.rules:14
        ATTR '/sys/devices/pci0000:00/0000:00:01.1/0000:01:00.0/host0/target0:2:8/0:2:8:0/block/sdc/queue/max_sectors_kb' writing '4096' /etc/udev/rules.d/99-abj.nr.rules:14
        handling device node '/dev/sdc', devnum=b8:32, mode=0660, uid=0, gid=6
        preserve permissions /dev/sdc, 060660, uid=0, gid=6
        preserve already existing symlink '/dev/block/8:32' to '../sdc'
        found 'b8:32' claiming '/run/udev/links/\x2fdisk\x2fby-id\x2fscsi-236435330529024150025384100000002'
        creating link '/dev/disk/by-id/scsi-236435330529024150025384100000002' to '/dev/sdc'
        preserve already existing symlink '/dev/disk/by-id/scsi-236435330529024150025384100000002' to '../../sdc'
        found 'b8:32' claiming '/run/udev/links/\x2fdisk\x2fby-id\x2fscsi-SNVMe_Dell_Ent_NVMe_v2_S6CSNA0R902415'
        creating link '/dev/disk/by-id/scsi-SNVMe_Dell_Ent_NVMe_v2_S6CSNA0R902415' to '/dev/sdc'
        preserve already existing symlink '/dev/disk/by-id/scsi-SNVMe_Dell_Ent_NVMe_v2_S6CSNA0R902415' to '../../sdc'
        found 'b8:32' claiming '/run/udev/links/\x2fdisk\x2fby-path\x2fpci-0000:01:00.0-scsi-0:2:8:0'
        creating link '/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:8:0' to '/dev/sdc'
        preserve already existing symlink '/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:8:0' to '../../sdc'
        .ID_FS_TYPE_NEW=
        ACTION=add
        DEVLINKS=/dev/disk/by-id/scsi-SNVMe_Dell_Ent_NVMe_v2_S6CSNA0R902415 /dev/disk/by-id/scsi-236435330529024150025384100000002 /dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:8:0
        DEVNAME=/dev/sdc
        DEVPATH=/devices/pci0000:00/0000:00:01.1/0000:01:00.0/host0/target0:2:8/0:2:8:0/block/sdc
        DEVTYPE=disk
        ID_BUS=scsi
        ID_FS_TYPE=
        ID_MODEL=Dell_Ent_NVMe_v2
        ID_MODEL_ENC=Dell\x20Ent\x20NVMe\x20v2
        ID_PATH=pci-0000:01:00.0-scsi-0:2:8:0
        ID_PATH_TAG=pci-0000_01_00_0-scsi-0_2_8_0
        ID_REVISION=.2.0
        ID_SCSI=1
        ID_SCSI_INQUIRY=1
        ID_SCSI_SERIAL=S6CSNA0R902415
        ID_SERIAL=236435330529024150025384100000002
        ID_SERIAL_SHORT=36435330529024150025384100000002
        ID_TYPE=disk
        ID_VENDOR=NVMe
        ID_VENDOR_ENC=NVMe\x20\x20\x20\x20
        MAJOR=8
        MINOR=32
        SCSI_IDENT_LUN_EUI64=36435330529024150025384100000002
        SCSI_IDENT_PORT_NAA_LOCAL=3bd790c2eff1ebd9
        SCSI_IDENT_SERIAL=S6CSNA0R902415
        SCSI_MODEL=Dell_Ent_NVMe_v2
        SCSI_MODEL_ENC=Dell\x20Ent\x20NVMe\x20v2
        SCSI_REVISION=.2.0
        SCSI_TPGS=0
        SCSI_TYPE=disk
        SCSI_VENDOR=NVMe
        SCSI_VENDOR_ENC=NVMe\x20\x20\x20\x20
        SUBSYSTEM=block
        TAGS=:systemd:
        USEC_INITIALIZED=76984220
        Unload module index
        Unloaded link configuration context.

## Test Without Custom Rules

        [root@r7525 rules.d]# !udev
        udevadm test --action="add" /sys/block/sdc
        calling: test
        version 239 (239-58.el8)
        This program is for debugging only, it does not run any program
        specified by a RUN key. It may show incorrect results, because
        some values may be different, or not available at a simulation run.

        Load module index
        Parsed configuration file /usr/lib/systemd/network/99-default.link
        Created link configuration context.
        Reading rules file: /usr/lib/udev/rules.d/01-md-raid-creating.rules
        Reading rules file: /usr/lib/udev/rules.d/10-dm.rules
        Reading rules file: /usr/lib/udev/rules.d/11-dm-lvm.rules
        Reading rules file: /usr/lib/udev/rules.d/11-dm-mpath.rules
        Reading rules file: /usr/lib/udev/rules.d/11-dm-parts.rules
        Reading rules file: /usr/lib/udev/rules.d/13-dm-disk.rules
        Reading rules file: /usr/lib/udev/rules.d/39-usbmuxd.rules
        Reading rules file: /usr/lib/udev/rules.d/40-elevator.rules
        Reading rules file: /usr/lib/udev/rules.d/40-libgphoto2.rules
        /usr/lib/udev/rules.d/40-libgphoto2.rules:11: IMPORT found builtin 'usb_id --export %%p', replacing
        Reading rules file: /usr/lib/udev/rules.d/40-redhat.rules
        Reading rules file: /usr/lib/udev/rules.d/40-usb-blacklist.rules
        Reading rules file: /usr/lib/udev/rules.d/40-usb_modeswitch.rules
        Reading rules file: /usr/lib/udev/rules.d/50-udev-default.rules
        Reading rules file: /usr/lib/udev/rules.d/60-alias-kmsg.rules
        Reading rules file: /usr/lib/udev/rules.d/60-block.rules
        Reading rules file: /usr/lib/udev/rules.d/60-cdrom_id.rules
        Reading rules file: /usr/lib/udev/rules.d/60-drm.rules
        Reading rules file: /usr/lib/udev/rules.d/60-evdev.rules
        Reading rules file: /usr/lib/udev/rules.d/60-fido-id.rules
        Reading rules file: /usr/lib/udev/rules.d/60-input-id.rules
        Reading rules file: /usr/lib/udev/rules.d/60-libfprint-2-autosuspend.rules
        Reading rules file: /usr/lib/udev/rules.d/60-mdevctl.rules
        Reading rules file: /usr/lib/udev/rules.d/60-net.rules
        Reading rules file: /usr/lib/udev/rules.d/60-persistent-alsa.rules
        Reading rules file: /usr/lib/udev/rules.d/60-persistent-input.rules
        Reading rules file: /usr/lib/udev/rules.d/60-persistent-storage-tape.rules
        Reading rules file: /usr/lib/udev/rules.d/60-persistent-storage.rules
        Reading rules file: /usr/lib/udev/rules.d/60-persistent-v4l.rules
        Reading rules file: /usr/lib/udev/rules.d/60-raw.rules
        Reading rules file: /usr/lib/udev/rules.d/60-rdma-ndd.rules
        Reading rules file: /usr/lib/udev/rules.d/60-rdma-persistent-naming.rules
        Reading rules file: /usr/lib/udev/rules.d/60-sensor.rules
        Reading rules file: /usr/lib/udev/rules.d/60-serial.rules
        Reading rules file: /usr/lib/udev/rules.d/60-tpm-udev.rules
        Reading rules file: /usr/lib/udev/rules.d/61-gdm.rules
        Reading rules file: /usr/lib/udev/rules.d/61-gnome-bluetooth-rfkill.rules
        Reading rules file: /usr/lib/udev/rules.d/61-gnome-settings-daemon-rfkill.rules
        Reading rules file: /usr/lib/udev/rules.d/61-scsi-sg3_id.rules
        Reading rules file: /usr/lib/udev/rules.d/62-multipath.rules
        Reading rules file: /usr/lib/udev/rules.d/63-fc-wwpn-id.rules
        Reading rules file: /usr/lib/udev/rules.d/63-md-raid-arrays.rules
        Reading rules file: /usr/lib/udev/rules.d/63-scsi-sg3_symlink.rules
        Reading rules file: /usr/lib/udev/rules.d/64-btrfs.rules
        Reading rules file: /usr/lib/udev/rules.d/64-md-raid-assembly.rules
        Reading rules file: /usr/lib/udev/rules.d/65-libwacom.rules
        Reading rules file: /usr/lib/udev/rules.d/65-md-incremental.rules
        Reading rules file: /usr/lib/udev/rules.d/65-sane-backends.rules
        Reading rules file: /usr/lib/udev/rules.d/66-kpartx.rules
        Reading rules file: /usr/lib/udev/rules.d/68-del-part-nodes.rules
        Reading rules file: /usr/lib/udev/rules.d/69-btattach-bcm.rules
        Reading rules file: /usr/lib/udev/rules.d/69-cd-sensors.rules
        Reading rules file: /usr/lib/udev/rules.d/69-dm-lvm-metad.rules
        Reading rules file: /usr/lib/udev/rules.d/69-libmtp.rules
        Reading rules file: /usr/lib/udev/rules.d/69-md-clustered-confirm-device.rules
        Reading rules file: /etc/udev/rules.d/69-vdo-start-by-dev.rules
        Reading rules file: /usr/lib/udev/rules.d/70-hypervfcopy.rules
        Reading rules file: /usr/lib/udev/rules.d/70-hypervkvp.rules
        Reading rules file: /usr/lib/udev/rules.d/70-hypervvss.rules
        Reading rules file: /usr/lib/udev/rules.d/70-joystick.rules
        Reading rules file: /usr/lib/udev/rules.d/70-mouse.rules
        Reading rules file: /usr/lib/udev/rules.d/70-nvmf-autoconnect.rules
        Reading rules file: /etc/udev/rules.d/70-persistent-ipoib.rules
        Reading rules file: /usr/lib/udev/rules.d/70-power-switch.rules
        Reading rules file: /usr/lib/udev/rules.d/70-printers.rules
        Reading rules file: /usr/lib/udev/rules.d/70-spice-vdagentd.rules
        Reading rules file: /usr/lib/udev/rules.d/70-touchpad.rules
        Reading rules file: /usr/lib/udev/rules.d/70-uaccess.rules
        Reading rules file: /usr/lib/udev/rules.d/70-wacom.rules
        Reading rules file: /usr/lib/udev/rules.d/71-biosdevname.rules
        Reading rules file: /usr/lib/udev/rules.d/71-nvmf-iopolicy-netapp.rules
        Reading rules file: /usr/lib/udev/rules.d/71-prefixdevname.rules
        Reading rules file: /usr/lib/udev/rules.d/71-seat.rules
        Reading rules file: /usr/lib/udev/rules.d/73-idrac.rules
        Reading rules file: /usr/lib/udev/rules.d/73-seat-late.rules
        Reading rules file: /usr/lib/udev/rules.d/75-net-description.rules
        Reading rules file: /usr/lib/udev/rules.d/75-probe_mtd.rules
        Reading rules file: /usr/lib/udev/rules.d/75-rdma-description.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-broadmobi-port-types.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-cinterion-port-types.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-dell-port-types.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-dlink-port-types.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-ericsson-mbm.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-fibocom-port-types.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-foxconn-port-types.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-gosuncn-port-types.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-haier-port-types.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-huawei-net-port-types.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-longcheer-port-types.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-mtk-port-types.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-nokia-port-types.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-quectel-port-types.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-sierra.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-simtech-port-types.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-telit-port-types.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-tplink-port-types.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-ublox-port-types.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-x22x-port-types.rules
        Reading rules file: /usr/lib/udev/rules.d/77-mm-zte-port-types.rules
        Reading rules file: /usr/lib/udev/rules.d/78-sound-card.rules
        Reading rules file: /usr/lib/udev/rules.d/80-drivers.rules
        Reading rules file: /usr/lib/udev/rules.d/80-iio-sensor-proxy.rules
        Reading rules file: /usr/lib/udev/rules.d/80-libinput-device-groups.rules
        Reading rules file: /usr/lib/udev/rules.d/80-mm-candidate.rules
        Reading rules file: /usr/lib/udev/rules.d/80-net-setup-link.rules
        Reading rules file: /usr/lib/udev/rules.d/80-udisks2.rules
        Reading rules file: /usr/lib/udev/rules.d/81-kvm-rhel.rules
        Reading rules file: /usr/lib/udev/rules.d/84-nm-drivers.rules
        Reading rules file: /usr/lib/udev/rules.d/85-nm-unmanaged.rules
        Reading rules file: /usr/lib/udev/rules.d/85-regulatory.rules
        Reading rules file: /usr/lib/udev/rules.d/90-alsa-restore.rules
        Reading rules file: /usr/lib/udev/rules.d/90-bolt.rules
        Reading rules file: /usr/lib/udev/rules.d/90-fwupd-devices.rules
        Reading rules file: /usr/lib/udev/rules.d/90-iprutils.rules
        Reading rules file: /usr/lib/udev/rules.d/90-libinput-fuzz-override.rules
        Reading rules file: /usr/lib/udev/rules.d/90-nm-thunderbolt.rules
        Reading rules file: /usr/lib/udev/rules.d/90-pulseaudio.rules
        Reading rules file: /usr/lib/udev/rules.d/90-rdma-hw-modules.rules
        Reading rules file: /usr/lib/udev/rules.d/90-rdma-ulp-modules.rules
        Reading rules file: /usr/lib/udev/rules.d/90-rdma-umad.rules
        Reading rules file: /usr/lib/udev/rules.d/90-vconsole.rules
        Reading rules file: /usr/lib/udev/rules.d/91-drm-modeset.rules
        Reading rules file: /usr/lib/udev/rules.d/95-cd-devices.rules
        Reading rules file: /usr/lib/udev/rules.d/95-dm-notify.rules
        Reading rules file: /usr/lib/udev/rules.d/95-iSM-usbnic-systemd.rules
        Reading rules file: /usr/lib/udev/rules.d/95-upower-csr.rules
        Reading rules file: /usr/lib/udev/rules.d/95-upower-hid.rules
        Reading rules file: /usr/lib/udev/rules.d/95-upower-wup.rules
        Reading rules file: /usr/lib/udev/rules.d/98-kexec.rules
        Reading rules file: /usr/lib/udev/rules.d/98-trace-cmd.rules
        Reading rules file: /usr/lib/udev/rules.d/99-qemu-guest-agent.rules
        Reading rules file: /usr/lib/udev/rules.d/99-systemd.rules
        Reading rules file: /usr/lib/udev/rules.d/99-vmware-scsi-udev.rules
        rules contain 393216 bytes tokens (32768 * 12 bytes), 48327 bytes strings
        47890 strings (395708 bytes), 43659 de-duplicated (351613 bytes), 4232 trie nodes used
        GROUP 6 /usr/lib/udev/rules.d/50-udev-default.rules:59
        IMPORT 'scsi_id --export --whitelisted -d /dev/sdc' /usr/lib/udev/rules.d/60-persistent-storage.rules:50
        starting 'scsi_id --export --whitelisted -d /dev/sdc'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_SCSI=1'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_VENDOR=NVMe'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_VENDOR_ENC=NVMe\x20\x20\x20\x20'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_MODEL=Dell_Ent_NVMe_v2'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_MODEL_ENC=Dell\x20Ent\x20NVMe\x20v2'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_REVISION=.2.0'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_TYPE=disk'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_SERIAL=236435330529024150025384100000002'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_SERIAL_SHORT=36435330529024150025384100000002'
        'scsi_id --export --whitelisted -d /dev/sdc'(out) 'ID_SCSI_SERIAL=S6CSNA0R902415      '
        Process 'scsi_id --export --whitelisted -d /dev/sdc' succeeded.
        LINK 'disk/by-id/scsi-236435330529024150025384100000002' /usr/lib/udev/rules.d/60-persistent-storage.rules:52
        IMPORT builtin 'path_id' /usr/lib/udev/rules.d/60-persistent-storage.rules:73
        LINK 'disk/by-path/pci-0000:01:00.0-scsi-0:2:8:0' /usr/lib/udev/rules.d/60-persistent-storage.rules:75
        IMPORT builtin 'blkid' /usr/lib/udev/rules.d/60-persistent-storage.rules:90
        probe /dev/sdc raid offset=0
        IMPORT '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw' /usr/lib/udev/rules.d/61-scsi-sg3_id.rules:17
        starting '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw'(out) 'SCSI_TPGS=0'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw'(out) 'SCSI_TYPE=disk'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw'(out) 'SCSI_VENDOR=NVMe'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw'(out) 'SCSI_VENDOR_ENC=NVMe\x20\x20\x20\x20'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw'(out) 'SCSI_MODEL=Dell_Ent_NVMe_v2'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw'(out) 'SCSI_MODEL_ENC=Dell\x20Ent\x20NVMe\x20v2'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw'(out) 'SCSI_REVISION=.2.0'
        Process '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/inquiry --raw' succeeded.
        IMPORT '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/vpd_pg80 --raw' /usr/lib/udev/rules.d/61-scsi-sg3_id.rules:27
        starting '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/vpd_pg80 --raw'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/vpd_pg80 --raw'(out) 'SCSI_IDENT_SERIAL=S6CSNA0R902415'
        Process '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/vpd_pg80 --raw' succeeded.
        IMPORT '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/vpd_pg83 --raw' /usr/lib/udev/rules.d/61-scsi-sg3_id.rules:30
        starting '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/vpd_pg83 --raw'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/vpd_pg83 --raw'(out) 'SCSI_IDENT_LUN_EUI64=36435330529024150025384100000002'
        '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/vpd_pg83 --raw'(out) 'SCSI_IDENT_PORT_NAA_LOCAL=3bd790c2eff1ebd9'
        Process '/usr/bin/sg_inq --export --inhex=/sys/block/sdc/device/vpd_pg83 --raw' succeeded.
        IMPORT 'fc_wwpn_id /devices/pci0000:00/0000:00:01.1/0000:01:00.0/host0/target0:2:8/0:2:8:0/block/sdc' /usr/lib/udev/rules.d/63-fc-wwpn-id.rules:8
        starting 'fc_wwpn_id /devices/pci0000:00/0000:00:01.1/0000:01:00.0/host0/target0:2:8/0:2:8:0/block/sdc'
        Process 'fc_wwpn_id /devices/pci0000:00/0000:00:01.1/0000:01:00.0/host0/target0:2:8/0:2:8:0/block/sdc' succeeded.
        LINK 'disk/by-id/scsi-SNVMe_Dell_Ent_NVMe_v2_S6CSNA0R902415' /usr/lib/udev/rules.d/63-scsi-sg3_symlink.rules:12
        LINK 'disk/by-id/scsi-236435330529024150025384100000002' /usr/lib/udev/rules.d/63-scsi-sg3_symlink.rules:25
        handling device node '/dev/sdc', devnum=b8:32, mode=0660, uid=0, gid=6
        preserve permissions /dev/sdc, 060660, uid=0, gid=6
        preserve already existing symlink '/dev/block/8:32' to '../sdc'
        found 'b8:32' claiming '/run/udev/links/\x2fdisk\x2fby-id\x2fscsi-236435330529024150025384100000002'
        creating link '/dev/disk/by-id/scsi-236435330529024150025384100000002' to '/dev/sdc'
        preserve already existing symlink '/dev/disk/by-id/scsi-236435330529024150025384100000002' to '../../sdc'
        found 'b8:32' claiming '/run/udev/links/\x2fdisk\x2fby-id\x2fscsi-SNVMe_Dell_Ent_NVMe_v2_S6CSNA0R902415'
        creating link '/dev/disk/by-id/scsi-SNVMe_Dell_Ent_NVMe_v2_S6CSNA0R902415' to '/dev/sdc'
        preserve already existing symlink '/dev/disk/by-id/scsi-SNVMe_Dell_Ent_NVMe_v2_S6CSNA0R902415' to '../../sdc'
        found 'b8:32' claiming '/run/udev/links/\x2fdisk\x2fby-path\x2fpci-0000:01:00.0-scsi-0:2:8:0'
        creating link '/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:8:0' to '/dev/sdc'
        preserve already existing symlink '/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:8:0' to '../../sdc'
        .ID_FS_TYPE_NEW=
        ACTION=add
        DEVLINKS=/dev/disk/by-path/pci-0000:01:00.0-scsi-0:2:8:0 /dev/disk/by-id/scsi-SNVMe_Dell_Ent_NVMe_v2_S6CSNA0R902415 /dev/disk/by-id/scsi-236435330529024150025384100000002
        DEVNAME=/dev/sdc
        DEVPATH=/devices/pci0000:00/0000:00:01.1/0000:01:00.0/host0/target0:2:8/0:2:8:0/block/sdc
        DEVTYPE=disk
        ID_BUS=scsi
        ID_FS_TYPE=
        ID_MODEL=Dell_Ent_NVMe_v2
        ID_MODEL_ENC=Dell\x20Ent\x20NVMe\x20v2
        ID_PATH=pci-0000:01:00.0-scsi-0:2:8:0
        ID_PATH_TAG=pci-0000_01_00_0-scsi-0_2_8_0
        ID_REVISION=.2.0
        ID_SCSI=1
        ID_SCSI_INQUIRY=1
        ID_SCSI_SERIAL=S6CSNA0R902415
        ID_SERIAL=236435330529024150025384100000002
        ID_SERIAL_SHORT=36435330529024150025384100000002
        ID_TYPE=disk
        ID_VENDOR=NVMe
        ID_VENDOR_ENC=NVMe\x20\x20\x20\x20
        MAJOR=8
        MINOR=32
        SCSI_IDENT_LUN_EUI64=36435330529024150025384100000002
        SCSI_IDENT_PORT_NAA_LOCAL=3bd790c2eff1ebd9
        SCSI_IDENT_SERIAL=S6CSNA0R902415
        SCSI_MODEL=Dell_Ent_NVMe_v2
        SCSI_MODEL_ENC=Dell\x20Ent\x20NVMe\x20v2
        SCSI_REVISION=.2.0
        SCSI_TPGS=0
        SCSI_TYPE=disk
        SCSI_VENDOR=NVMe
        SCSI_VENDOR_ENC=NVMe\x20\x20\x20\x20
        SUBSYSTEM=block
        TAGS=:systemd:
        USEC_INITIALIZED=76984220
        Unload module index
        Unloaded link configuration context.
