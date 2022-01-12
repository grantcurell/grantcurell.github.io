# Using the idrac API to Gather Stats

## Helpful Links

Dell API Docs: https://developer.dell.com/apis/2978/versions/5.xx/docs/0WhatsNew.md

Redfish Telemetry Whitepaper: https://www.dmtf.org/sites/default/files/standards/documents/DSP2051_1.0.0.pdf

Description of the AMQP Messaging Protocol: https://www.ionos.com/digitalguide/websites/web-development/advanced-message-queuing-protocol-amqp/

Setting Up Splunk for the First Time: https://docs.splunk.com/Documentation/Splunk/8.2.4/Installation/StartSplunkforthefirsttime

Integrate iDRAC Telemetry Data Into Splunk: [Link to PDF](integrate-idrac9-telemetry-data-into-splunk-platform.pdf)

## My Test Environment

### RHEL

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

## Installation

### Setup Splunk

1. Download [trial of Splunk](https://www.splunk.com/en_us/download/splunk-enterprise.html?skip_request_page=1)
2. Follow [Splunk installation instructions](https://docs.splunk.com/Documentation/Splunk/8.2.4/Installation/InstallonLinux)
3. By default it will install to /opt/splunk. Run `/opt/splunk/bin/splunk start` (I suggest you do this in tmux or another terminal emulator)
4. Run `firewall-cmd --permanent --zone public --add-port=8000/tcp && firewall-cmd --reload`
5. Make splunk start on boot with `/opt/splunk/bin/splunk enable boot-start`
6. Enter the web UI and install the following two apps:
   1. https://splunkbase.splunk.com/app/5245/#/details
   2. https://splunkbase.splunk.com/app/5228/#/details
7. First we will configure Redfish add-on for Splunk. Begin by opening the app.
8. Go to Configuration->Account->Add. Enter the credentials for the account on iDRAC with access to the telemetry reports.
9. Next, go to Inputs. Click "Create New Input" and enter the following information:
   1.  TODO: ADD THIS. NEED TO GO BACK AND FIGURE OUT METRIC REPORTS

### Configure the iDRAC

1. Download [this script](https://github.com/dell/iDRAC-Telemetry-Scripting/blob/master/ConfigurationScripts/EnableOrDisableAllTelemetryReports.py) which will enable telemetry reports.
2. Run `EnableOrDisableAllTelemetryReports.py -ip $target -u $user -p $password`
   1. This enables telemetry on the target server
3. Next you will need to enable Redfish alerting which will publish the events to Splunk. Download [this script](https://github.com/dell/iDRAC-Telemetry-Scripting/blob/master/ConfigurationScripts/SubscriptionManagementREDFISH.py)
4. Run the following command `SubscriptionManagementREDFISH.py -ip $target -u $user -p $password -c y -D https://$splunkserver/services/collector/raw -E Alert -V Event`
   1. `$target` is the ip address or DNS name of the iDRAC
   2. `$user/$password` are the username and password for iDRAC
   3. `$splunkserver` is the IP address or DNS name of your Splunk HTTP event collector instance

