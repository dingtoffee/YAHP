sudo -u dump tcpdump -p -f port 445 or port 139 or port 3389 or port 80 or port 22 or port 443 or port 7777 -w /var/log/pcap/trace-%Y-%m-%d-%H-%M-%S-%s.pcap -G 3600 -C 50

