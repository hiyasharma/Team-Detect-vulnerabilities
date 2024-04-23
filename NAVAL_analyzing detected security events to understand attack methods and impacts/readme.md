
## Naval Kishor -21BCY10146
## Analyzing Detected Security to Understand Attack Methods and Impacts 
- Data Collection and Integration: Utilizing the advanced capabilities of the security analytics platform like **SPLUNK** , **IBMQradar** , **Log360** to collect and integrate security data from various sources, such as **logs, network traffic, endpoint telemetry, and threat intelligence feeds**. Ensuring that all relevant data sources are properly configured and integrated into the platform.
 - Identify Patterns : Looking For the Patterns in the detected security events. This could include the types of events, their frequency, and any correlations between them. 
			   - For example, if multiple login attempts from different locations are detected within a short period, it could indicate a brute force attack.
## Splunk Steps
- Target - Window 7
- Attacker - Kali 
1. Pinging the target system from Kali

![](https://i.postimg.cc/cCdCRTSS/pinging-the-target-pc.png)
2. Pinging the Kali from system

![Pining kali from Window 7](https://i.postimg.cc/x8h6c6h0/3-pinging-kali-from-target.png)
3. Windows 7 Task Manager Before the Attack

![enter image description here](https://i.postimg.cc/cHWZ8HRg/2window7-machine-task-manager-before-attack.png)
4. Target Window 7 After the Attack using hping3

![enter image description here](https://i.postimg.cc/1zpQ992T/4-taget-pc-after-sending-the-packet-using-hping3.png)

5. Result in kali of Hping3 

![enter image description here](https://i.postimg.cc/xdF4DBT7/5result-of-hping3.png)
6. Data Set in Splunk After the Attack

![enter image description here](https://i.postimg.cc/k4Y9HTkX/dataset-after-hping3.png)
