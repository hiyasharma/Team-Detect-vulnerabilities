# This file contains details about capturing packets using tcpdump.

Computer's IP information

![target_pc_ip_info](https://github.com/hiyasharma/Team-Detect-vulnerabilities/assets/66080016/6f63b99b-fc61-4f64-968e-7a6051c15f4d)

- Capturing ICMP packets sent by attacker's ping.
![image](https://github.com/hiyasharma/Team-Detect-vulnerabilities/assets/66080016/6af8cacb-13d5-4d41-8a91-6954c5006daf)
Since snort and tcpdump both revealed attacker's IP address. Now we are gonna run tcpdump  specifically filtering attacker's IP.

- Detecting ftp and ssh requests and writing to ftp_log.pcap file.
![image](https://github.com/hiyasharma/Team-Detect-vulnerabilities/assets/66080016/0fa66d12-0494-4700-9edc-1109e08f037c)

- Detecting swaks scan and writing to swaks_log.pcap file.
![image](https://github.com/hiyasharma/Team-Detect-vulnerabilities/assets/66080016/4f0cd8c7-7566-446e-a2b3-880a1612f7c9) 

- Detecting nmap scan from attacker and writing to nmap_log.pcap file.
![image](https://github.com/hiyasharma/Team-Detect-vulnerabilities/assets/66080016/da41e740-ef78-4de1-b90c-8d90562ced32)

- Detecting scans from legion tool and writing to legion_log.pcap file.
![image](https://github.com/hiyasharma/Team-Detect-vulnerabilities/assets/66080016/80374d81-1d48-43bb-91e5-b26047979874)
![image](https://github.com/hiyasharma/Team-Detect-vulnerabilities/assets/66080016/135e68cf-a358-4f58-8f3e-22cce9cfb485)
