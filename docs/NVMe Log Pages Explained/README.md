# NVMe Log Pages Explained

## Get Log Page Identifiers

![](images/2022-04-29-13-07-20.png)

[NVMe Express Base Specification](images/NVMe-NVM-Express-2.0a-2021.07.26-Ratified.pdf)

## Error Information (01h)

This log page is used to describe extended error information for a command that completed with error or report an error that is not specific to a particular command. Extended error information is provided when the More (M) bit is set to ‘1’ in the Status Field for the completion queue entry associated with the command that completed with error or as part of an asynchronous event with an Error status type. This log page is global to the controller. This error log may return the last n errors. If host software specifies a data transfer of the size of n error logs, then the error logs for the most recent n errors are returned. The ordering of the entries is based on the time when the error occurred, with the most recent error being returned as the first log entry. Each entry in the log page returned is defined in Figure 206. The log page is a set of 64-byte entries; the maximum number of entries supported is indicated in the ELPE field in the Identify Controller data structure (refer to Figure 275). If the log page is full when a new entry is generated, the controller should insert the new entry into the log and discard the oldest entry. The controller should clear this log page by removing all entries on power cycle and Controller Level Reset.

## SMART / Health Information (02h)

This log page is used to provide SMART and general health information. The information provided is over the life of the controller and is retained across power cycles. To request the controller log page, the namespace identifier specified is FFFFFFFFh or 0h. For compatibility with implementations compliant with NVM Express Base Specification revision 1.4 and earlier, hosts should use a namespace identifier of FFFFFFFFh to request the controller log page. The controller may also support requesting the log page on a per namespace basis, as indicated by bit 0 of the LPA field in the Identify Controller data structure in Figure 275.

## Firmware Slot Information (03h)

This log page is used to describe the firmware revision stored in each firmware slot supported. The firmware revision is indicated as an ASCII string. The log page also indicates the active slot number. The log page returned is defined in Figure 209

### Sample Output

`nvme fw-log /dev/nvme9n1`

## Changed Namespace List (04h)

**NOTE** This command is not currently supported because the drives currently only have one namespace.

This log page is used to describe namespaces attached to the controller that have:

1. changed information in their Identify Namespace data structures (refer to in Figure 146) since the
last time the log page was read;
2. been added; and
3. been deleted.

The log page contains a Namespace List with up to 1,024 entries. If more than 1,024 namespaces have changed attributes since the last time the log page was read, the first entry in the log page shall be set to FFFFFFFFh and the remainder of the list shall be zero filled.

## Commands Supported and Effects (05h)

This log page is used to describe the commands that the controller supports and the effects of those commands on the state of the NVM subsystem. The log page is 4,096 bytes in size. There is one Commands Supported and Effects data structure per Admin command and one Commands Supported and Effects data structure per I/O command based on:

1. the I/O Command Set selected in CC.CSS, if CC.CSS is not set to 110b; and
2. the Command Set Identifier field in CDW 14, if CC.CSS is set to 110b.

### Sample Output

`nvme effects-log /dev/nvme0n1`

## Device Self-test (06h)

This log page is used to indicate: 

1. the status of any device self-test operation in progress and the percentage complete of that operation; and 
2. the results of the last 20 device self-test operations. 

The Self-test Result Data Structure contained in the Newest Self-test Result Data Structure field is always the result of the last completed or aborted self-test operation. The next Self-test Result Data Structure field in the Device Self-test log page contains the results of the second newest self-test operation and so on. If fewer than 20 self-test operations have completed or been aborted, then the Device Self-test Status field shall be set to Fh in the unused Self-test Result Data Structure fields and all other fields in that Self-test Result Data Structure are ignored.

## Other NVMe CLI Commands

### List All NVMe Drives

`nvme list`

Lists all the NVMe SSDs attached: name, serial number, size, LBA format, and serial