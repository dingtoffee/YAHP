# Yet Another HoneyPot built on Python
HoneyPot attempts to offer a reliable indicator of compromise with little to no setup or maintenance costs. It could also provide wealth of data in terms of the TTPS of the attackers which could be used for further data analysis.
There are tons of honeypot options out there, most of them are opensource tools like DShields that requires internet connection and catered for external perimeters. Today, I would like to share a simple setup that could cater for internal perimeters with minimal maintenance required.
I decided to build a low interaction HoneyPot that emulated a real service on the devices and generate a “small” attack surface in the internal environment to track any intrusion activities on our internal environment. The setup would be based on different open-source libraries.

# Setup Overview
Raspberry Pi Model 3B ​
- 1GB RAM;​
- 64GB Micro SD card; ​
- Wireless/LAN; ​

Trap Installed (latest library with updates)​

- Cowrie (SSH Honeypot)​
- Lighttpd (HTTP/HTTPS Honeypot) ​
- RDPY Library (Custom RDP Honeypot)​
- Impacket Library (Custom SMB Honeypot) ​

Language ​

- All emulated service ran using python;​
- Non-root environment
- Configuration Monitoring ​
- Supervisord

Logging format​
- Under /var/log each honeypot service will generate text log
- Syslog configured to send over to your SIEM
- Tcpdump to collect packets

Installation Procedure 
https://dingtoffee.medium.com/creating-a-honeypot-on-raspberry-pi-475858a2ba88
