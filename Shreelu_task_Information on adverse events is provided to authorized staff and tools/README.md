![image](https://github.com/hiyasharma/Team-Detect-vulnerabilities/assets/94289402/ad370c7c-6259-493a-8165-037b01f8939a)<h1>Task: Information on adverse events is provided to authorized staff and tools</h1>

<h3>Shreelu Santosh - 21BCY10090</h3>

<h2>Table of contents:</h2>

<ol>
  <li><a href="#ir">Tool for Incident Response</a></li>
  <ul>
    <li><a href="#demo-iris">Demo of DFIR IRIS</a></li>
    <li><a href="#banner">Options in Dashboard Banner</a></li>
  </ul>
  <li><a href="#securecomm">Tools for Secure Communication</a></li>
  <ul>
    <li><a href="#signal">Signal</a></li>
    <li><a href="#proton">Proton Mail</a></li>
  </ul>
</ol>

<h3 id="ir">1. Tool for Incident Response: DFIR IRIS</h3>

<p>DFIR-IRIS is an open source collaborative incident response platform, created by incident responders for incident responders. It enables incident responders to share technical details during investigations.</p>

<p>It is shipped in Docker containers, which make it easy to deploy with Docker Compose.</p>

<p>We can run Iris in the following steps:</p>

<ol>
  <li>Clone the Github repository</li>
  <li>Go to the directory where the repo is cloned to</li>
  <li>Build and run Docker container.</li>
</ol>

<p>We require the following to be able to run IRIS:</p>

<ul>
  <li>Docker</li>
</ul>

<h5 id="demo-iris">Demo of DFIR IRIS Dashboard:</h5>
This is the log-in page to IRIS dashboard:

![image](https://github.com/hiyasharma/Team-Detect-vulnerabilities/assets/94289402/d5ece1ac-c96e-44de-baf0-f15695a1f6b9)

On logging in, we get the following:
![image](https://github.com/hiyasharma/Team-Detect-vulnerabilities/assets/94289402/807aab05-ab45-43ab-b8e1-e8e209798cd5)

On clicking '+ Create New Case' in the top right corner, we can fill in some information about our new case:
![image](https://github.com/hiyasharma/Team-Detect-vulnerabilities/assets/94289402/70b67b11-e761-4cb2-a4c7-c1e2d7ca9e75)

After filling in the information about the case, and clicking 'Create', we will switch to our newly created case.
![image](https://github.com/hiyasharma/Team-Detect-vulnerabilities/assets/94289402/c7eed9c8-8701-4a89-9d2d-fb093d46a9fe)

<p id="banner">We see the following banner at the top:</p>

![image](https://github.com/hiyasharma/Team-Detect-vulnerabilities/assets/94289402/599668c6-ee7c-4be8-80e0-8ec87b1fdfea)

Click on each for more information on each button in the banner:
<ul>
  <li><a href="https://github.com/hiyasharma/Team-Detect-vulnerabilities/blob/main/Shreelu_task_Information%20on%20adverse%20events%20is%20provided%20to%20authorized%20staff%20and%20tools/Banner-Notes.md">Notes</a>:</li>
  <li><a href="https://github.com/hiyasharma/Team-Detect-vulnerabilities/blob/main/Shreelu_task_Information%20on%20adverse%20events%20is%20provided%20to%20authorized%20staff%20and%20tools/Banner-Assets.md">Assets</a></li>
  <li><a href="https://github.com/hiyasharma/Team-Detect-vulnerabilities/blob/main/Shreelu_task_Information%20on%20adverse%20events%20is%20provided%20to%20authorized%20staff%20and%20tools/Banner-IOC.md">IOC</a></li>
  <li><a href="https://github.com/hiyasharma/Team-Detect-vulnerabilities/blob/main/Shreelu_task_Information%20on%20adverse%20events%20is%20provided%20to%20authorized%20staff%20and%20tools/Banner-Timeline.md">Timeline</a></li>
  <li><a href="https://github.com/hiyasharma/Team-Detect-vulnerabilities/blob/main/Shreelu_task_Information%20on%20adverse%20events%20is%20provided%20to%20authorized%20staff%20and%20tools/Banner-Graph.md">Graph</a></li>
  <li><a href="https://github.com/hiyasharma/Team-Detect-vulnerabilities/blob/main/Shreelu_task_Information%20on%20adverse%20events%20is%20provided%20to%20authorized%20staff%20and%20tools/Banner-Tasks.md">Tasks</a></li>
  <li><a href="https://github.com/hiyasharma/Team-Detect-vulnerabilities/blob/main/Shreelu_task_Information%20on%20adverse%20events%20is%20provided%20to%20authorized%20staff%20and%20tools/Banner-Evidence.md">Evidence</a></li>
</ul>

<h3 id="securecomm">2. Tools for Secure Communication: Signal, Proton Mail</h3>

The importance of communication in incident response cannot be underestimated. Communication needs to be internal, as well as external. The things to be considered, while implementing a communication plan for incident response, are:
<ul>
  <li><b>Messaging</b>: An organization must agree on and deliver one shared, consistent message. This message should resonate with the audience and align with the particular communications goals and objectives.</li>
  <li><b>Reputation</b>: How and when information is disclosed, and how you handle the situation from a communications perspective, will ultimately affect your organization’s reputation in the industry and community</li>
  <li><b>Stakeholder Management</b>: Your organization should be as transparent as possible with its constituents, and be honest about what is known versus unknown at
any given time</li>
  <li><b>Accuracy and timeliness of information</b>: Any information disclosed during an incident must be both accurate and timely. The timeliness of notifications is critical to stakeholder communication and management. </li>
</ul>

<h4 id="signal">i. Signal</h4>

<p>Signal is a simple, powerful, and secure messenger that uses end-to-end encryption to protect your conversations.</p>

<h4>Application to Task:</h4>
<ul>
  <li><b>End-to-end Encryption</b>: Neither Signal, nor your phone company, nor the government can read your messages. That's why it's remained popular with journalists, government officials, and anyone else who deals with classified materials. Many other popular messaging apps also use this feature, but Signal's source code is publicly available, so experts have been able to poke and prod at its defenses for years, strengthening it in the process.</li>
  <li><b>Ability to disconnect Signal account from phone number</b>: While the platform requires your mobile number to sign up, you can set this up using a Google voice number, while Apple users can stop their history from syncing with the cloud by turning off ‘show calls in recents’ in settings.</li>
</ul>

<h4 id="proton">ii. Proton Mail</h4>

<p>Proton Mail is an encrypted email service based in Switzerland that protects your privacy and data from trackers and scanners.</p>

<h4>Application to Task:</h4>
<ul>
  <li><b>Swiss jurisdiction</b>: All the data and email servers are situated in Switzerland, which is known for better privacy laws compared to those in the US and EU.</li>
  <li><b>Use of various encryption algorithms</b>: All messages are end-to-end encrypted and also remain encrypted in your mailbox until actively being read. The encryption algorithms used are:
    <ul>
      <li>AES-128</li>
<li>TLS 1.0</li>
<li>DHE RSA</li>
<li>SHA 3</li>
    </ul>
  </li>
</ul>
