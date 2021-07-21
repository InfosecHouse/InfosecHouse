<p align="center">
  <a href="https://github.com/infosechouse/infosechouse">
    <img src="https://raw.githubusercontent.com/InfosecHouse/InfosecHouse/main/img/infosechouse-banner.png">
  </a>
</p>
<h3 align="center">Infosec resource center for offensive and defensive security operations.</h4>
<br>
<p align="center">
  <a href="https://twitter.com/infosechouse" target="_blank">
    <img src="https://img.shields.io/twitter/follow/infosechouse.svg?logo=twitter">
  </a>
</p>
<div align="center">
  <sub>Created by
  <a href="https://twitter.com/m4giktrick">m4giktrick</a>
</div>
<br>
<br>

A curated list of many tools and resources for both offensive and defensive security teams. Please visit [https://infosec.house/](https://infosec.house/) for our website version of this repo. Found a resources that should be on here? Feel free to submit a pull request or drop it in our [Discord](https://discord.gg/FWe9bjDBfY) server.

## Socialize with Us

| Organization | Hyperlink |
| :--- | :---------  |
| Discord | https://discord.gg/FWe9bjDBfY |
| Instagram | https://www.instagram.com/InfosecHouse/ |
| Twitter | https://twitter.com/InfosecHouse |
| Telegram | https://t.me/InfosecHouse |
| Twitch | https://www.twitch.tv/InfosecHouse |
| YouTube | https://www.youtube.com/channel/UC4PgsAu56TSpzH66aIOqbKQ |


## Contents

- [Icon Directory](#-icon-directory)
- [Defensive Security](https://github.com/InfosecHouse/InfosecHouse-Dev#defensive-security)
    - [Asset Management](#-asset-management)
    - [Forensics](#-forensics)
    - [IDS/IPS](#-ids-ips)
    - [Incident Response](#-incident-response)
    - [IOC](#-ioc)
    - [Malware](#-malware)
    - [Monitoring](#-monitoring)
    - [Phishing](#-phishing)
    - [Threat Intel](#-threat-intel)
- [Offensive Security](#-offensive-security)
    - [API](#-api)
    - [Bug Bounty](#-bug-bounty)
    - [Cloud](#-cloud)
    - [Courses](#-courses)
    - [Cracking](#-cracking)
    - [CTF Offensive](#-ctf-offensive)
    - [Exploits](#-exploits)
    - [Hardware](#-hardware)
    - [Linux](#-linux)
    - [Mobile](#-mobile)
    - [Network](#-network)
    - [Reconnaissance](#-reconnaissance)
    - [Social Engineering](#-social-engineering)
    - [Vulnerability Scanners](#-vulnerability-scanners)
    - [Web Application](#-web-application)
    - [Windows](#-windows)
    - [Wireless](#-wireless)
- [Operation Security](#-operation-security)
    - [Anonymity](#-anonymity)
    - [Communication](#-communication)
- [Purple Security](#-purple-security)
    - [Editors & Viewers](#-editor-and-viewers)
    - [Purple Frameworks](#-purple-frameworks)
    - [OSINT](#-osint)
    - [Reverse Engineering](#-reverse-engineering)
    - [Write-Ups](#-write-ups)
- [Xtras](#-xtras)
    - [Video](#-video)
- [Thanks](#-thanks)










## [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) ICON DIRECTORY

*Icon directory used within the tool and resources table*

| Icon | Description |
| :--- | :---------  |
| ![no-recent-update](icons/no-recent-update.png) | Aged Resource - There has not been any update to resource in past 2 years. |
| ![archive](icons/archive.png) | Archived - Tool/Resource is in archived state. No longer updated/maintained. |
| ![freemium-service](icons/freemium-service.png) | Freemium - Tool/Resource is free but offers premium plan/upgrade of service. |
| ![legal](icons/legal.png) | Legality - Accessing this resource can be considered illegal. Check your local laws. |
| ![malware](icons/malware.png) | Malware - Live malware is hosted on this resource and can cause harm/damage to property. Proceed with caution. |
| ![opensource](icons/opensource.png) | Open Source - Source code is freely available and anyone can review it. |
| ![paid-product](icons/paid-product.png) | Payment Required - Tool/Service requires payment for usage. |
| ![recommended-resource](icons/recommended-resource.png) | Recommended - Infosec House recommendation of tool/resource |
| ![register-profile](icons/register-profile.png) | Registration Required - An account is required to access this resource. |
| ![tor-icon](icons/tor-icon.png)  | TOR Access - This resource has a TOR website. The TOR software is required to access it. |
| ![transparency](icons/transparency.png) | Transparency - Resource has provided Infosec House with transparency report/log. |
| ![verified](icons/verified.png) | Verified - Verified resource/organization. |
| ![winner-1](icons/winner.png) | Winner - Resource was a winner in the Infosec House tool battle arena. |





***




## [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Defensive Security

*Defensive Security (Blue Team) tools and resources.*








### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Asset Management

*Keep track of your inventory*

#### 🔵 Endpoint Visibility

| Tool | Description | Directory |
| :------ | :----- | :------ |
| [LANSweeper](https://www.lansweeper.com/) | Build centralized IT asset inventory. | ![freemium-service](icons/freemium-service.png )![opensource](icons/opensource.png) |









### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Forensics

*Uncover the dirty little secrets of a recovered HDD, Image, malware, and more.*

#### 🔵 Browser

| Tool | Description | Directory |
| :------ | :----- | :------ |
| [Hindsight](https://github.com/obsidianforensics/hindsight) | Web browser forensics for Google Chrome/Chromium. | ![opensource](icons/opensource.png) |

#### 🔵 ISO's

| Tool | Description | Directory |
| :------ | :----- | :------ |
| [Bitscout](https://bitscout-forensics.info/) | LiveCD/LiveUSB for remote forensic acquisition and analysis | N/A |
| [SANS Investigative Forensics Toolkit (SIFT)](https://github.com/teamdfir/sift) | Linux distribution for forensic analysis | N/A |
| [Tsurugi](https://tsurugi-linux.org/) | Linux distribution for DFIR | N/A |
| [WinFE](https://www.winfe.net/home) | Windows Forensics | N/A |

#### 🔵 Mobile

| Tool | Description | Directory |
| :------ | :----- | :------ |
| [Andriller](https://github.com/den4uk/andriller) | Performs read-only, forensically sound, non-destructive acquisition from Android devices. | ![opensource](icons/opensource.png) |

#### 🔵 Operating Systems

| Tool | Description | Directory |
| :------ | :----- | :------ |
| [The Sleuth Kit](https://github.com/sleuthkit/sleuthkit) | Forensic toolkit for analyzing Microsoft and UNIX file systems and disks. | ![opensource](icons/opensource.png) |

#### 🔵 Scripts

| Tool | Description | Directory |
| :------ | :----- | :-------- |
| [DissectingMalwa.re Lab](https://github.com/f0wl/MalwareLab_VM-Setup) | Download/setup script for malware analysis/software reverse engineering. | ![opensource](icons/opensource.png) |

#### 🔵 Tools

| Tool | Description | Directory |
| :------ | :----- | :-------- |
| [Beagle](https://github.com/yampelo/beagle) | Digital forensics tool which transforms security logs and data into graphs. | ![opensource](icons/opensource.png) |









### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) IDS/IPS

*Intrusion Detection Systems and Intrusion Prevention Systems.*

#### 🔵 Platform

| Tool | Description | Directory |
| :------ | :----- | :------ |
| [Snort](https://www.snort.org/) | Open Source detection software. | ![opensource](icons/opensource.png) |
| [Suricata](https://suricata.io) | Indpendent open-source threat detection engine. | ![opensource](icons/opensource.png) |







### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Incident Response

*Platforms for defensive security operations.*

#### 🔵 Management Platform

| Tool | Description | Directory |
| :------ | :----- | :------ |
| [Cyphon](https://github.com/cyphonmdr/cyphon) | Platform that receives, processes, and triages events to create a more efficient analytic workflow | ![archive](icons/archive.png) ![opensource](icons/opensource.png) |
| [DFIRTrack](https://github.com/dfirtrack/dfirtrack) | The Incident Response Tracking Application | ![opensource](icons/opensource.png) |
| [FIR](https://github.com/certsocietegenerale/FIR) |  Fast Incident Response allows for easy creation, tracking, and reporting of cybersecurity incidents. | ![opensource](icons/opensource.png) |
| [The Hive](https://github.com/TheHive-Project/TheHive) | A Scalable, Open Source and Free Security Incident Response Platform | ![opensource](icons/opensource.png) |
| [Wazuh](https://github.com/wazuh/wazuh) | Capable of protecting workloads across on-premises, virtualized, containerized, and cloud-based environments. | ![opensource](icons/opensource.png) |

#### 🔵 Reporting

| Tool | Description | Directory |
| :------ | :----- | :------ |
| [Cortex](https://github.com/TheHive-Project/Cortex) | Powerful Observable Analysis and Active Response Engine | ![opensource](icons/opensource.png) |
| [Response](https://github.com/monzo/response) | Real-time incident response and reporting tool. | ![opensource](icons/opensource.png) |
| [Velociraptor](https://github.com/Velocidex/velociraptor) | A tool for collecting host based state information using Velocidex Query Language (VQL) queries. | ![opensource](icons/opensource.png) |









### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) IOC

*Indicators of Compromise.*

#### 🔵 Scanners

| Tool | Description | Directory |
| :------ | :----- | :------ |
| [Fenrir](https://github.com/Neo23x0/Fenrir) | Simple Bash IOC Scanner. | ![opensource](icons/opensource.png) |
| [Loki](https://github.com/Neo23x0/Loki) | Simple IOC and YARA scanner. | ![opensource](icons/opensource.png) |
| [Redline](https://www.fireeye.com/services/freeware/redline.html) | FireEye's premier free endpoint security tool, provides host investigative capabilities.  | ![opensource](icons/opensource.png) |
| [Thor Lite](https://www.nextron-systems.com/thor-lite/) | Free IOC and YARA Scanner. | ![freemium-service](icons/freemium-service.png) ![opensource](icons/opensource.png) |










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Malware

*All the malware you can wish for to reverse engineer.*

#### 🔵 Distribution Centers

| Organization | Description | Directory | 
| :------ | :----- | :------- |
| [Any.Run](https://app.any.run/submissions/) | Interactive online malware analysis service for dynamic and static research of most types of threats using any environments. | ![malware](icons/malware.png) ![register-profile](icons/register-profile.png) |
| [Contagio Malware Dump](https://contagiodump.blogspot.com/) | Password Required. A collection of the latest malware samples, threats, observations, and analyses. | ![malware](icons/malware.png) |
| [Cape Sandbox](https://capesandbox.com/) | A malware sandbox derived from Cuckoo and is designed to automate the process of malware analysis with the goal of extracting payloads and configuration from malware.| ![malware](icons/malware.png) ![register-profile](icons/register-profile.png) |
| [Das Malwerk](https://www.dasmalwerk.eu/) | The daily zip-file aims to serve you a batch of malware ranging from annoying adware to bank trojans and beyond! | ![malware](icons/malware.png) |
| [Hatching Triage](https://tria.ge/) | A malware sandboxing solution. It leverages a unique architecture, developed with scaling in mind from the start! | ![malware](icons/malware.png) ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |
| [Hybrid Analysis](https://www.hybrid-analysis.com/) | A free malware analysis service for the community. Using this service you can submit files for in-depth static and dynamic analysis.  | ![malware](icons/malware.png) ![register-profile](icons/register-profile.png)|
| [InQuest](https://labs.inquest.net/) | A free malware analysis service for the community. Using this service you can submit files for in-depth static and dynamic analysis.  | ![malware](icons/malware.png) ![register-profile](icons/register-profile.png) |
| [KernelMode.Info](https://www.kernelmode.info/forum/)  | A forum for reverse engineerin, OS internals and malware analysis.  | ![malware](icons/malware.png) ![register-profile](icons/register-profile.png) |
| [Malshare](https://www.malshare.com/)  | A free Malware repository providing researchers access to samples, malicious feeds, and Yara results.  | ![malware](icons/malware.png) ![register-profile](icons/register-profile.png) |
| [Malware Bazaar](https://bazaar.abuse.ch/browse/) | Project operated by abuse.ch. A project to collect and share malware samples.  | ![malware](icons/malware.png) ![register-profile](icons/register-profile.png) |
| [Malware Samples](https://github.com/MalwareSamples/Malware-Feed/)  | An ongoing and updated archive of files collected which are associated with specific public malicious threat reports  | ![malware](icons/malware.png) |
| [Malware-DB (theZoo)](https://thezoo.morirt.com/)  | theZoo is a project created to make the possibility of malware analysis open and available to the public. | ![malware](icons/malware.png) |
| [Objective-See](https://objective-see.com/malware.html)  | Mac malware samples collected by the Objective-See team | ![malware](icons/malware.png) |
| [Packet Total](https://packettotal.com/malware-archive.html)  | Simple, free, high-qualityh PCAP file analysis | ![malware](icons/malware.png) |
| [PhishingKitTracker](https://github.com/marcoramilli/PhishingKitTracker)  | An extensible and freshly updated collection of phishingkits for forensics and future analysis topped with simple stats | ![malware](icons/malware.png) |
| [Polyswarm](https://polyswarm.network/)  | Threat Intelligence Marketplace | ![malware](icons/malware.png) ![register-profile](icons/register-profile.png) |
| [SNDBOX](https://app.sndbox.com/) | Malware sandbox platform | ![malware](icons/malware.png) ![register-profile](icons/register-profile.png) |
| [SoReL-20M](https://github.com/sophos-ai/SOREL-20M)  | Sophos-ReversingLabs 20 Million dataset. HUGE dataset. | ![malware](icons/malware.png) |
| [URLhaus](https://urlhaus.abuse.ch/browse/)  | Project operated by abuse.ch. A project to collect and share malware samples. | ![malware](icons/malware.png) ![register-profile](icons/register-profile.png) |
| [VirusBay](https://beta.virusbay.io) | A web-based, collaboration platform that connects security operations center (SOC) professionals with relevant malware researchers. | ![malware](icons/malware.png) ![register-profile](icons/register-profile.png) |
| [VirusShare](https://virusshare.com/) | Because Sharing is Caring | ![malware](icons/malware.png) ![register-profile](icons/register-profile.png) |
| [VirusSign](https://virussign.com/) | A huge collection of high quality malware samples | ![malware](icons/malware.png) ![register-profile](icons/register-profile.png) |
| [Virus Samples](https://www.virussamples.com/)  | Over 150,000+ malicious files, viruses, malware, trojans, executables, scripts, and other forms of malware payloads across a variety of file types and architectures | ![malware](icons/malware.png) ![register-profile](icons/register-profile.png) |
| [VX-Underground](https://vx-underground.org/samples.html) | Over 150,000+ malicious files, viruses, malware, trojans, executables, scripts, and other forms of malware payloads across a variety of file types and architectures | ![malware](icons/malware.png) | 
| [Yori](https://yomi.yoroi.company/upload) | Free sandbox-based file analysis service | ![malware](icons/malware.png) ![register-profile](icons/register-profile.png) |

#### 🔵 Ransomware

| Tool | Description | Directory |
| :------ | :----- | :-------- |
| [GonnaCry](https://github.com/tarcisio-marinho/GonnaCry) | A linux ransomware that encrypts all the user files with a strong encryption scheme. | ![malware](icons/malware.png) |

#### 🔵 Scanners

| Organization | Description | Directory |
| :------ | :----- | :-------- |
| [Hybrid Analysis](https://www.hybrid-analysis.com/) | A free malware analysis service for the community that detects and analyzes unknown threats using a unique Hybrid Analysis technology. | ![malware](icons/malware.png) ![register-profile](icons/register-profile.png) |
| [ID Ransomware](https://id-ransomware.malwarehunterteam.com/index.php) | Upload a ransom note and/or sample encrypted file to identify the ransomware that has encrypted your data. | N/A |
| [Jotti](https://virusscan.jotti.org/) | Free service that lets you scan suspicious files with several anti-virus programs. | ![freemium-service](icons/freemium-service.png) |
| [Kaspersky Threat Portal](https://opentip.kaspersky.com/) | Сheck any suspicious threat indicator, whether it is a file, file hash, IP address or web address. | ![freemium-service](icons/freemium-service.png) ![register-profile](icons/register-profile.png) |
| [Opswat](https://metadefender.opswat.com/) | Simply submit suspicious files to MetaDefender Cloud for analysis. | ![freemium-service](icons/freemium-service.png) ![register-profile](icons/register-profile.png) |
| [VirusTotal](https://www.virustotal.com/gui/) | Analyze suspicious files and URLs to detect types of malware, automatically share them with the security community. | ![freemium-service](icons/freemium-service.png) ![malware](icons/malware.png) ![register-profile](icons/register-profile.png) |









### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Monitoring

*Monitoring tools and resources*

#### 🔵 Network

| Tool | Description | Directory |
| :------ | :----- | :------ |
| [Zeek](https://github.com/zeek/zeek) | A powerful framework for network traffic analysis and security monitoring. | ![opensource](icons/opensource.png) |










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Phishing

*Tools/Resources for analyzing phishing attacks.*

#### 🔵 Frameworks

| Tool | Description | Directory |
| :------ | :----- | :------ |
| [Phishalytics](https://github.com/sjbell/phishalytics) | Collect and analyse large-scale datasets. | ![opensource](icons/opensource.png) |
| [Phishing Tracker](https://github.com/ndejong/phishing-tracker) | Utility to manage sets of phishing links making it easier to track their removal progress over time. | ![opensource](icons/opensource.png) |











### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Threat Intel

*Discover where the threats begin.*

#### 🔵 Forums

| Organization | Description | Directory |
| :------ | :----- | :------ |
| [RAID Forums](https://raidforums.com/Forum-Leaks-Market) | Raid forum known for selling databreach leaks, stolen accounts, etc. | ![freemium-service](icons/freemium-service.png) ![register-profile](icons/register-profile.png) |


#### 🔵 Frameworks/Platforms

| Organization | Description | Directory |
| :------ | :----- | :------ |
| [ARTIF](https://github.com/CRED-CLUB/ARTIF) | An advanced real time threat intelligence framework to identify threats and malicious web traffic on the basis of IP reputation and historical data. | ![opensource](icons/opensource.png) |
| [MISP](https://github.com/MISP/MISP) | MISP (core software) - Open Source Threat Intelligence and Sharing Platform (formely known as Malware Information Sharing Platform). | ![opensource](icons/opensource.png) |

#### 🔵 Pastes

| Organization | Description | Directory |
| :------ | :----- | :------ |
| [Ghostbin](https://ghostbin.com/) | Ghostbin is a website where you can store and share text online. | N/A |
| [Pastebin](https://pastebin.com/) | Pastebin is a website where you can store text online for a set period of time. | N/A |

#### 🔵 Ransomware Group Feeds

| Organization | Description | Directory |
| :------ | :----- | :------ |
| Arvin Club [[TOR](http://3kp6j22pz3zkv76yutctosa6djpj4yib2icvdqxucdaxxedumhqicpad.onion/)] | Arvin ransomware team homepage. | ![legal](icons/legal.png) |
| Avaddon [[TOR](http://avaddongun7rngel.onion)] | Avaddon ransomware team homepage. | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |
| Babuk Locker [[TOR](http://wavbeudogz6byhnardd2lkp2jafims3j7tj6k6qnywchn2csngvtffqd.onion/)] | Babuk Locker ransomware team homepage | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |
| CL0P [[TOR](http://ekbgzchl6x2ias37.onion/)] | CL0P ransomware team homepage. | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |
| [CONTI](https://continews.icu/) [[TOR](http://continewsnv5otx5kaoje7krkto2qbu3gtqef22mnr7eaxw3y6ncz3ad.onion)] | CONTI ransomware team homepage. | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |
| Cuba [[TOR](http://cuba4mp6ximo2zlo.onion/)] | Cuba ransomware team homepage. | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |
| DarkSide [[TOR](http://darksidc3iux462n6yunevoag52ntvwp6wulaz3zirkmh4cnz6hhj7id.onion/)] | Darkside ransomware team homepage. | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |
| DoppelPaymer [[TOR](http://hpoo4dosa3x4ognfxpqcrjwnsigvslm7kv6hvmhh2yqczaxy3j6qnwad.onion/)] | DoppelPaymer ransomware team hompage. | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |
| Everest [[TOR](http://ransomocmou6mnbquqz44ewosbkjk3o5qjsl3orawojexfook2j7esad.onion/)] | Everest ransomware team homepage. | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |
| Lorenz [[TOR](http://lorenzmlwpzgxq736jzseuterytjueszsvznuibanxomlpkyxk6ksoyd.onion/)] | Lorenz ransomware team hompage. | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |
| LV [[TOR](http://rbvuetuneohce3ouxjlbxtimyyxokb4btncxjbo44fbgxqy7tskinwad.onion/)] | LV ransomware team homepage. | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |
| Mount Locker [[TOR](http://mountnewsokhwilx.onion)] | Mount Locker ransomware team homepage. | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) | 
| N3tw0rm [[TOR](http://n3twormruynhn3oetmxvasum2miix2jgg56xskdoyihra4wthvlgyeyd.onion/)] | N3tw0rm ransomware team homepage. |  ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |
| Nefilim (Corporate Leaks) [[TOR](http://edteebo2w2bvwewbjb5wgwxksuwqutbg3lk34ln7jpf3obhy4cvkbuqd.onion/)] | Nefilm/Corporate Leaks ransomware team hompage. | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |
| Pay2Key [[TOR](http://pay2key2zkg7arp3kv3cuugdaqwuesifnbofun4j6yjdw5ry7zw2asid.onion/)]  | Pay2Key ransomware team homepage | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |
| PYSA [[TOR](http://pysa2bitc5ldeyfak4seeruqymqs4sj5wt5qkcq7aoyg4h2acqieywad.onion/)] | PYSA ransomware team homepage | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |
| Ragnar Locker [[TOR](http://p6o7m73ujalhgkiv.onion/)] | Ragnar Locker ransomware team homepage. | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |
| Ragnarok [[TOR](http://wobpitin77vdsdiswr43duntv6eqw4rvphedutpaxycjdie6gg3binad.onion/)] | Ragnarok ransomware team homepage. | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |
| RansomEXX [[TOR](http://rnsm777cdsjrsdlbs4v5qoeppu3px6sb2igmh53jzrx7ipcrbjz5b2ad.onion/)] | RansomEXX ransomware team homepage. | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |
| Ranzy Locker [[TOR](http://37rckgo66iydpvgpwve7b2el5q2zhjw4tv4lmyewufnpx4lhkekxkoqd.onion/)] | Ranzy Locker ransomware team hompage. | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |
| Sodinokibi (REvil) [[TOR](http://dnpscnbaix6nkwvystl3yxglz7nteicqrou3t75tpcc5532cztc46qyd.onion)]  | REvil ransomware team hompage. | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png)  |
| Sunscrypt [[TOR](http://nbzzb6sa6xuura2z.onion/)] | Sunscrypt ransomware team homepage. | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png)  |
| SynAck [[TOR](http://xqkz2rmrqkeqf6sjbrb47jfwnqxcd4o2zvaxxzrpbh2piknms37rw2ad.onion/index.html)] | SynAck ransomeware team hompage | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |
| Xing Team [[TOR](http://xingnewj6m4qytljhfwemngm7r7rogrindbq7wrfeepejgxc3bwci7qd.onion/)] | Xing ransomware team hompage | ![legal](icons/legal.png) ![tor-icon](icons/tor-icon.png) |

#### 🔵 TOR Directory Listings

| Organization | Description| Directory |
| :------ | :----- | :----- |
| Dark Dir [[TOR](http://l7vh56hxm3t4tzy75nxzducszppgi45fyx2wy6chujxb2rhy7o5r62ad.onion) | TOR Link Directory  | ![tor-icon](icons/tor-icon.png)  |
| Hidden Links [[TOR](http://wclekwrf2aclunlmuikf2bopusjfv66jlhwtgbiycy5nw524r6ngioid.onion/)] | TOR Link Directory  | ![tor-icon](icons/tor-icon.png)  |
| Onion Link Directory [[TOR](http://torlinkszegvxqb6.onion/)] | TOR Link Directory  | ![tor-icon](icons/tor-icon.png)  |
| Onion Scanner [[TOR](http://4r4zaei5qa7qq5ha.onion/)] | Onion Scanner is a unique deepweb shops crawler which gathers reviews for customers’ convenience.  | ![tor-icon](icons/tor-icon.png)  |
| Paul's Onion Links [[TOR](http://paullzqj3ntil7vyar3gxeks7bz5haiteeehz5vdk5fadvtto7q7liid.onion/)] | TOR Link Directory  | ![tor-icon](icons/tor-icon.png)  |
| Shops Dir [[TOR](http://vxmua4uvg7vp5ssnvx5gexrr2nxso3wwvjwagdub67vcombj4kf4i4qd.onion/)] | ShopsDir is a growing catalogue of all DeepWeb/DarkNet shops, stores and markets  | ![tor-icon](icons/tor-icon.png)  |
| Tornode [[TOR](http://e6wzjohnxejirqa2sgridvymv2jxhrqdfuyxvoxp3xpqh7kr4kbwpwad.onion/)] | TOR Link Directory  | ![tor-icon](icons/tor-icon.png)  |

#### 🔵 TOR Search Engines

| Organization | Description | Directory |
| :------ | :----- | :------- |
| [Ahmia](https://ahmia.fi/) | Ahmia's mission is to create the premier search engine for services residing on the Tor anonymity network  | N/A |
| Hoodle [[TOR](http://nr2dvqdot7yw6b5poyjb7tzot7fjrrweb2fhugvytbbio7ijkrvicuid.onion)] | A DeepWeb search engine with clear interface and accurate link database  | ![tor-icon](icons/tor-icon.png)  |
| Sentor [[TOR](http://e27slbec2ykiyo26gfuovaehuzsydffbit5nlxid53kigw3pvz6uosqd.onion/index.php)] | TOR Search Engine | ![tor-icon](icons/tor-icon.png)  |









***

## [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Offensive Security

*Offensive Security (Red Team) tools and resources.*










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) API

*Tools and resources for pentesting against API endpoints.*

#### 🔴 Cheetsheets/Checklists

| Tool | Description | Directory |
| :------ | :----- | :------ | 
| [API Security Checklist](https://github.com/shieldfy/API-Security-Checklist) | Checklist of the most important security countermeasures when designing, testing, and releasing your API . | ![opensource](icons/opensource.png) |
| [GraphQL OWASP](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html) | OWASP GraphQL cheat sheet. | ![opensource](icons/opensource.png) |
| [Microservices OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Microservices_security.html) | Microservices Security | ![opensource](icons/opensource.png) |
| [OWASP API Top 10](https://apisecurity.io/encyclopedia/content/owasp-api-security-top-10-cheat-sheet-a4.pdf) | OWASP API security Top 10. | ![opensource](icons/opensource.png) |
| [REST Security OWASP](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html) | OWASP REST security cheat sheet. | ![opensource](icons/opensource.png) |
| [REST Assessment OWASP](https://cheatsheetseries.owasp.org/cheatsheets/REST_Assessment_Cheat_Sheet.html) | OWASP REST assessment cheat sheet. | ![opensource](icons/opensource.png) |
| [Web API Pentesting](https://book.hacktricks.xyz/pentesting/pentesting-web/web-api-pentesting) | Web API pentesting GitBook. | ![opensource](icons/opensource.png) |


#### 🔴 Documentation

| Tool | Description | Directory |
| :------ | :----- | :------ | 
| [MindAPI](https://github.com/dsopas/MindAPI) | Organize your API security assessment by using MindAPI. | ![opensource](icons/opensource.png) |

#### 🔴 Manipulation & Testing

| Tool | Description | Directory |
| :------ | :----- | :------ | 
| [Arjun](https://github.com/s0md3v/Arjun) | HTTP parameter discovery suite. | ![opensource](icons/opensource.png) |
| [Astra](https://github.com/flipkart-incubator/Astra) | Automated Security Testing For REST API's  | ![opensource](icons/opensource.png) |
| [Apache JMeter](https://jmeter.apache.org/download_jmeter.cgi) | Java application designed to load test functional behavior and measure performance. |  ![opensource](icons/opensource.png) |
| [Automatic API Attack Tool](https://github.com/imperva/automatic-api-attack-tool) | Imperva's API attack tool takes an API specification as an input, generates and runs attacks that are based on it as an output. |  ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [Burp Suite](https://portswigger.net/burp) | Arm yourself with the leading toolkit for web security testing. Test, find, and exploit vulnerabilities. |  ![freemium-service](icons/freemium-service.png)|
| [Fiddler Everwhere](https://www.telerik.com/fiddler/fiddler-everywhere) | A web debugging proxy for macOS, Windows, and Linux. Capture, inspect, monitor all HTTP(S) traffic between your computer and the Internet, mock requests, and diagnose network issue. | ![freemium-service](icons/freemium-service.png)|
| [Hoppscotch](https://github.com/hoppscotch/hoppscotch) | Open source tool that covers the entire testing spectrum (functional, security, load, mocking). | ![opensource](icons/opensource.png) |
| [HttpMaster](https://www.httpmaster.net/) | Master HTTP testing & debugging. | ![freemium-service](icons/freemium-service.png)|
| [Insomnia](https://insomnia.rest/) | Quickly and easily send REST, SOAP, GraphQL, and GRPC requests directly within Insomnia. | ![freemium-service](icons/freemium-service.png)![opensource](icons/opensource.png) |
| [Karate](https://github.com/intuit/karate) | Test automation made simple. | ![opensource](icons/opensource.png) |
| [Kiterunner](https://github.com/assetnote/kiterunner) |  Contextual Content Discovery Tool. | ![opensource](icons/opensource.png) | 
| [Postman](https://www.postman.com/) | A collaboration platform for API development. Postman's features simplify each step of building an API and streamline collaboration so you can create better APIs—faster. | ![freemium-service](icons/freemium-service.png)|
| [SoapUI](https://www.soapui.org/tools/soapui/) | Open source tool that covers the entire testing spectrum (functional, security, load, mocking). | ![opensource](icons/opensource.png) |
| [Taurus](https://gettaurus.org/) | Taurus improves experience of JMeter, Selenium and others. | ![opensource](icons/opensource.png) |
| [Test Mace](https://testmace.com/) | A modern powerful crossplatform tool for working with an API and creating automated API tests. |  ![freemium-service](icons/freemium-service.png)![opensource](icons/opensource.png) |
| [vRESTng](https://vrest.io) | Automate API Requests as Runnable Test Cases, just by providing Request Details. Also, Validate API Responses using Test Case Assertions. |  ![freemium-service](icons/freemium-service.png)|

#### 🔴 Training

| Tool | Description | Directory |
| :------ | :----- | :------ | 
| [crAPI](https://github.com/OWASP/crAPI) | Completely ridiculous API (crAPI). | ![opensource](icons/opensource.png) |
| [Damn Vulnerable GraphQL App](https://github.com/dolevf/Damn-Vulnerable-GraphQL-Application) | An intentionally vulnerable implementation of Facebook's GraphQL technology, to learn and practice GraphQL Security. | ![opensource](icons/opensource.png) |
| [DVMS](https://github.com/ne0z/DamnVulnerableMicroServices) | This is vulnerable microservice written in many language to demonstrating OWASP API Top Security Risk. | ![opensource](icons/opensource.png) |
| [dvws-node](https://github.com/snoopysecurity/dvws-node) | Damn Vulnerable Web Service is a vulnerable web service/API/application that can be used to learn webservices/API vulnerabilities. | ![opensource](icons/opensource.png) |
| [Kontra](https://application.security/free/owasp-top-10-API) | A series of free interactive application security training modules that teach developers how to identify and mitigate security vulnerabilities in their web API endpoints. | N/A |
| [VAmPI](https://github.com/erev0s/VAmPI) | Vulnerable REST API with OWASP top 10 vulnerabilities for APIs. | ![opensource](icons/opensource.png) |
| [vAPI](https://github.com/roottusk/vapi) | Vulnerable Adversely Programmed Interface which is Self-Hostable PHP Interface that mimics OWASP API Top 10 scenarios in the means of Exercises. | ![opensource](icons/opensource.png) |










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Blogs

*Reading material for offensive security researchers.*

#### 🔴 Corporate

| Organization | Description | Directory |
| :------ | :----- | :------ |
| [Not so Secure](https://notsosecure.com/blog/) | Mix of research | N/A |
| [Orange Cyberdefense](https://sensepost.com/blog/) | Mix of research | N/A |
| [Security Weekly](https://securityweekly.com/blog/) | Mix of research | N/A |
| [Trustwave](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/) | Mix of research | N/A |


#### 🔴 Personal

| Organization | Description | Directory |
| :------ | :----- | :------ |
| [Archangel Amael](http://archangelamael.blogspot.com/) | Mix of research | N/A |
| [Attack and Defense](https://blog.carnal0wnage.com/) | Mix of research | N/A |
| [carnal0wnage](https://blog.carnal0wnage.com/) | CVE research. | N/A |
| [Ch3rn0byl](https://ch3rn0byl.com/) | CVE research. | N/A |
| [Coldwind](https://gynvael.coldwind.pl/?blog=1&lang=en) | Mix of research | N/A |
| [Corelan](https://www.corelan.be/) | Mix of research | N/A |
| [Darknet.org.uk](https://www.darknet.org.uk/) | Mix of research. | N/A |
| [Digi Ninja](https://digi.ninja/blog.php) | Mix of research | N/A |
| [GnuCitizen](https://www.gnucitizen.org/) | Mix of research | N/A |
| [Hacking & Security](https://hackingandsecurity.blogspot.com/) | Mix of research | N/A |
| [ihazomgsecurityskills](http://ihazomgsecurityskillz.blogspot.com/) | Mix of research | N/A |
| [Mad Irish](https://www.madirish.net/) | Mix of research | N/A |
| [Memset](https://memset.wordpress.com/) | Mix of research | N/A |
| [MG.LOL](https://mg.lol/blog/) | Hardware security research. | N/A |
| [Myne-us](http://www.myne-us.com/) | Hardware security research. | N/A |
| [Pentest Blog](https://pentest.blog/) | Mix of research. Vulnerability research team of PRODAFT SARL | N/A |
| [Question Defense](https://www.question-defense.com/) | Mix of research | N/A | 
| [Reusable Security](https://reusablesec.blogspot.com/) | Password Cracking, Crypto, and General Security Research. | N/A |
| [Security Reliks](https://securityreliks.wordpress.com/) | Mix of research | N/A |
| [Security Sift](https://9emin1.github.io/pages/) | CTF Write-ups/Windows Research | N/A |
| [Sirdarckcat](http://sirdarckcat.blogspot.com/) | Web App and Mix of research | N/A |
| [Spy Logic](https://www.spylogic.net/) | Mix of research | N/A |
| [Strolling Infosec](https://9emin1.github.io/pages/) | Mix of research | N/A |
| [Weapons of Mass Analysis](http://wepma.blogspot.com/) | Mix of research | N/A |
| [Wirewatcher](https://wirewatcher.wordpress.com/) | Mix of research | N/A |













### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Bug Bounty

*Global bug bounty platform, crowdsourced security, & vulnerability disclosure.*

#### 🔴 Cheatsheets/Checklists

| Organization | Description | Directory |
| :------ | :----- | :-------- |
| [Bug bounty Roadmaps](https://github.com/1ndianl33t/Bug-Bounty-Roadmaps) | Bug Bounty Roadmaps | ![opensource](icons/opensource.png) |

#### 🔴 Platforms

| Organization | Description | Directory |
| :------ | :----- | :-------- |
| [Bugscrowd](https://bugcrowd.com/programs) | #1 crowdsourcedc security company. | ![register-profile](icons/register-profile.png) |
| [HackerOne](https://hackerone.com/directory/programs/) | The platform is the industry standard for hacker-powered security. | ![register-profile](icons/register-profile.png) |
| [huntr](https://www.huntr.dev/) | Bug bounty board for securing open-source. | ![register-profile](icons/register-profile.png) |
| [Integriti](https://www.intigriti.com/programs) | Europe's #1 ethical hacking and bug bounty platform. | ![register-profile](icons/register-profile.png) |
| [Safe Hats](https://app.safehats.com/signup) | Managed Bug Bounty. | ![register-profile](icons/register-profile.png) |
| [Synack](https://www.synack.com/) | Built by hackers for hackers. | ![register-profile](icons/register-profile.png) |
| [Yes We Hack](https://yeswehack.com/auth/register#create-hunter) | Global bug bounty platform crowdsourced security & vulnerability disclosure. | ![register-profile](icons/register-profile.png) |

#### 🔴 Services

| Organization | Description | Directory |
| :------ | :----- | :-------- |
| [Recon.Dev](https://recon.dev/) | Collects recon data on bounty targets and provides tools to help quickly find targets and discover bugs. | ![freemium-service](icons/freemium-service.png) ![register-profile](icons/register-profile.png) |










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Cloud

*Training and courses to master your craft. Some of the below courses do offer professional certifications as add-ons to course purchase.*

#### 🔴 AWS

| Organization | Description | Directory |
| :------ | :----- | :-------- |
| [pacu](https://github.com/RhinoSecurityLabs/pacu) | The AWS exploitation framework, designed for testing the security of Amazon Web Services environments.  | N/A |

#### 🔴 Docker

| Organization | Description | Directory |
| :------ | :----- | :-------- |
| [Dacker Daemon Attack Surface](https://docs.docker.com/engine/security/#docker-daemon-attack-surface) | There are four major areas to consider when reviewing Docker security | N/A |

#### 🔴 GitHub

| Organization | Description | Directory |
| :------ | :----- | :-------- |
| [gitleaks](https://github.com/zricethezav/gitleaks) | Scan git repos (or files) for secrets using regex and entropy. | ![opensource](icons/opensource.png) |
| [gitrob](https://github.com/michenriksen/gitrob) | Reconnaissance tool for GitHub organizations  | ![archive](icons/archive.png) ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [GitRoller](https://github.com/mansoorr123/GitRoller) |  GitRoller: A Git Recon Tools  | ![opensource](icons/opensource.png) |
| [go-gitaudit](https://github.com/r-pai/go-gitaudit) | Git audit is a go package which can be used to audit git repository to find issues.  | ![opensource](icons/opensource.png) |
| [shhgit](https://github.com/eth0izzle/shhgit) | Find secrets in your code. Secrets detection for your GitHub, GitLab and Bitbucket repositories. | ![opensource](icons/opensource.png) |
| [truffleHog](https://github.com/trufflesecurity/truffleHog) | Searches through git repositories for high entropy strings and secrets, digging deep into commit history. | ![opensource](icons/opensource.png) |
| [Yar](https://github.com/nielsing/yar) | Yar is a tool for plunderin' organizations, users and/or repositories. | ![opensource](icons/opensource.png) |










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Courses

*Training and courses to master your craft. Some of the below courses do offer professional certifications as add-ons to course purchase.*

#### 🔴 Offensive Security Courses/Training

| Organization | Description | Directory |
| :------ | :----- | :-------- |
| [AQ Answers](https://answersq.com/) | Daily updates on free courses, workshopd, interships, and jobs. | N/A |
| [Bug Bounty Hunter](https://www.bugbountyhunter.com/) | Helping you connect the bug to bounty. | ![register-profile](icons/register-profile.png) |
| [Cybrary](https://www.cybrary.it/) | The leading cybersecurity professional development platform. | ![freemium-service](icons/freemium-service.png) ![register-profile](icons/register-profile.png) |
| [eLearn Security](https://elearnsecurity.com/) | Infosec careers are heating up and candidates are doing everything they can to stand out. | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |
| [Hacker101](https://www.hacker101.com/) | A free class for web security. | ![register-profile](icons/register-profile.png) |
| [HTB Academy](https://academy.hackthebox.eu/) | Cyber security trainingp by HackTheBox | ![register-profile](icons/register-profile.png) |
| [INE](https://ine.com/pages/cybersecurity) | The premier provider of online it training. | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |
| [Infosec Institute](https://www.infosecinstitute.com/) | Helps IT and security professionals advance their careers with skills development and certifications | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |
| [Kontra](https://application.security/) | Application Security Training Redefined. | ![freemium-service](icons/freemium-service.png) ![register-profile](icons/register-profile.png) |
| [Offensive Security](https://www.offensive-security.com/) | The tech workforce development company. | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |
| [Pentester Academy](https://www.pentesteracademy.com/) | Courses and Online Labs. | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |
| [Pentester Lab](https://www.pentesterlab.com/) | We make learning web hacking easier! | ![freemium-service](icons/freemium-service.png) ![register-profile](icons/register-profile.png) |
| [PortSwigger](https://portswigger.net/web-security) | Free, online web security training from the creators of Burp Suite | ![register-profile](icons/register-profile.png) |
| [Pluralsight](https://www.pluralsight.com/) | The tech workforce development company. | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |
| [Professor Messer](https://www.professormesser.com/) |  Professor Messer IT Certification Training. | ![register-profile](icons/register-profile.png) |
| [SANS](https://www.sans.org/cyber-security-courses/?&focus-area=penetration-testing-ethical-hacking&training-format=) | SANS Institute is the most trusted resource for cybersecurity training, certifications and research. | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |
| [TCM Security](https://academy.tcm-sec.com/) | SANS Institute is the most trusted resource for cybersecurity training, certifications and research. | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |
| [TestOut](https://w3.testout.com/courses/ethical-hacker-pro) | TestOut Ethical Hacker Pro teaches students to be aware of network attack strategies and common countermeasures. | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |
| [Udemy](https://www.udemy.com/courses/search/?q=penetration+testing&src=sac&kw=pen) | an online learning and teaching marketplace with over 155,000 courses. | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Cracking

*Everything you need to crack all the hashes.*

#### 🔴 Password Cracking

| Tool | Description | Directory |
| :------ | :----- | :----- |
| [Hashcat](https://hashcat.net/wiki/) | Worlds fastest password cracker and only in-kernel rule engine | ![opensource](icons/opensource.png) |
| [John the Ripper](https://www.openwall.com/john/) | An Open Source password security auditing and password recovery tool available for many operating systems | ![opensource](icons/opensource.png) |










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) CTF Offensive

*A CTF event is usually timed, and the points are totaled once the time has expired. The winning player/team will be the one that solved the most challenges, and thus, secured the highest score.*

#### 🔴 Continous

| Organization | Description | Directory |
| :------ | :----- | :----- |
| [Crackmes](https://crackm.es) | A place where you can download crackmes to improve your reverse engineering skills. | ![register-profile](icons/register-profile.png) |
| [Cryptohack](https://cryptohack.org/) | A fun free platform for learning modern cryptography. | ![register-profile](icons/register-profile.png) |
| [CTF Challenge](https://ctflearn.com/) | Collection of 12 vulnerable web applications, each one has its own realistic infrastructure built over several subdomains containing vulnerabilities. | ![register-profile](icons/register-profile.png) |
| [CTFLearn](https://ctflearn.com/) | Learn cybersecurity the most beginner-friendly way to get into hacking. | ![register-profile](icons/register-profile.png) |
| [DomGoat](https://domgo.at/cxss/intro) | DOM security learning platform | N/A |
| [Hack The Box](https://www.hackthebox.eu/) | Massive online cyber security training platform, allowing individuals, companies, universities and all kinds of organizations around the world to level up their hacking skills. | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [pwnable.tw](http://pwnable.tw) | Pwnable.tw is a wargame site for hackers to test and expand their binary exploiting skills. | ![register-profile](icons/register-profile.png) |
| [pwnable.kr](http://pwnable.kr) | A non-commercial wargame site which provides various pwn challenges regarding system exploitation. | ![register-profile](icons/register-profile.png) |
| [Try Hack Me (King of the Hill)](https://tryhackme.com/games/koth) | Making it easier to break into security, all through your browswer. | ![register-profile](icons/register-profile.png) |


#### 🔴 Seasonal

| Organization | Description | Directory |
| :------ | :----- | :---- |
| [Hack-a-Sat](https://www.hackasat.com/) | United States Air Force and United States Space Force jointly presents Hack-A-Sat | ![register-profile](icons/register-profile.png) |










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Exploits

*Gather all your exploits needed to pop that box.*

#### 🔴 Exploit Databases

| Organization | Description | Directory |
| :------ | :----- | :---- |
| [0-Day Today](https://0day.today/)  [[TOR](https://curaj33verawgaddbsdsrzc5krmopfyqnei66io5ldhqwdiqukt4vcyd.onion/)] | The ultimate database of exploits and vulnerabilties and a great resource for researchers. Private exploits, and 0-Days are sold here. | ![freemium-service](icons/freemium-service.png)![malware](icons/malware.png) |
| [Android Kernel](https://github.com/SecWiki/android-kernel-exploits) | Android Kernel Exploits | ![no-recent-update](icons/no-recent-update.png) |
| [Exploit Database](https://www.exploit-db.com/)  | The Exploit Database is maintained by Offensive Security, an information security training company. | ![recommended-resource](icons/recommended-resource.png) ![malware](icons/malware.png) ![opensource](icons/opensource.png) |
| [Linux Kernel](https://github.com/SecWiki/linux-kernel-exploits) | Linux kernel exploits. | ![no-recent-update](icons/no-recent-update.png) |
| [NIST NVD](https://nvd.nist.gov/vuln/search?execution=e2s1) | The National Institute of Standards and Technology. U.S. Department of Commerce | N/A |
| [MacOS Kernel](https://github.com/SecWiki/macos-kernel-exploits) | MacOS Kernel Exploits | ![no-recent-update](icons/no-recent-update.png) |
| [Security Focus](https://www.securityfocus.com/vulnerabilities) | From original news content to detailed technical papers and guest columnists, Security Focus is a great resource for all things security related. | N/A |
| [Windows Kernel](https://github.com/SecWiki/windows-kernel-exploits) | Windows Kernel Exploits | N/A |
| [Windows Rootkits](https://github.com/LycorisGuard/Windows-Rootkits) | Windows Rootkits | N/A |










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Hardware

*Grab some of the most used hardware within the penetration testing industry.*


#### 🔴 Equipment

| Tool | Description | Directory |
| :------ | :----- | :----- |
| [Alfa Card](https://www.amazon.com/s?k=Alfa-AWUS036NHA) | The Atheros chipset supports all 6 WiFi modes. Best success rate of various injection attacks using this Wi-Fi adaptor. | ![paid-product](icons/paid-product.png) |
| [Ardunio](https://www.arduino.cc/) | Open-source electronic prototyping platform enabling users to create interactive electronic objects. | ![paid-product](icons/paid-product.png) |
| [Attify Badge](https://www.attify-store.com/) | A hardware security assessment tool. Used to communicate between a PC and an embedded device over various hardware communication protocols. | ![paid-product](icons/paid-product.png) |
| [DigiSpark](http://digistump.com/products/1) | An Attiny85 based microcontroller development board similar to the Arduino line, only cheaper, smaller, and a bit less powerful. | ![paid-product](icons/paid-product.png) |
| [MultiBlue Dongle](https://www.amazon.com/MultiBlue-Dongle-Bluetooth-Keyboard-BT300KMS/dp/B00CRY5K16) | Can be connected to another computer via a USB port and control the victims computer via bluetooth. | ![paid-product](icons/paid-product.png) |
| [O.MG Cable](https://shop.hak5.org/collections/mischief-gadgets/products/o-mg-cable?variant=29408695582833) | For covert field-use, with features that enhance remote execution, stealth, and forensics evasion. | ![paid-product](icons/paid-product.png) |
| [OpticSpy](https://www.attify-store.com/products/opticspy) | a platform to explore, evaluate, and experiment with optical data transmissions. | ![paid-product](icons/paid-product.png) |
| [Pluggable BT Dongle](https://plugable.com/products/usb-bt4le/) | Survey on nearby bluetooth devices enumerate the services and even send simple data packet to them. | ![paid-product](icons/paid-product.png) |
| [Raspberry Pi](https://www.raspberrypi.org/) | A tiny and affordable computer that you can use to learn programming through fun, practical projects. | ![paid-product](icons/paid-product.png) |
| [Ubertooth One](https://greatscottgadgets.com/ubertoothone/) | Ubertooth One is an open source 2.4 GHz wireless development platform suitable for Bluetooth experimentation. | ![paid-product](icons/paid-product.png) |
| [Wi-fi Pineapple](https://shop.hak5.org/products/wifi-pineapple) | Automate WiFi auditing with all new campaigns and get actionable results from vulnerability assessment reports. | ![paid-product](icons/paid-product.png) |

#### 🔴 Store

| Organization | Description | Directory |
| :------ | :----- | :------ |
| [Hacker Gadgets](https://hacker-gadgets.com/) | One-stop warehouse, for the best Hacking Gadgets, Pentesting Equipment, Hacker Hardware Tools and everyday Swag. | ![paid-product](icons/paid-product.png) |
| [Hacker Warehouse](https://hackerwarehouse.com/) | Your one-stop shop for all your computer security needs from defense to offense. | ![paid-product](icons/paid-product.png) |
| [Hak5](https://shop.hak5.org/) | Pentest tools for authorized auditing/security analysis only where permitted. | ![paid-product](icons/paid-product.png) |









### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Linux

*Tools and resources for pentesting on linux environments.*

#### 🔴 Cheatsheets

| Tool | Description | Directory |
| :------ | :----- | :----- |
| [GTFOBins](https://gtfobins.github.io/) | A curated list of Unix binaries that can be used to bypass local security restrictions in misconfigured systems. | ![opensource](icons/opensource.png) |

#### 🔴 Post Exploitation

| Tool | Description | Directory |
| :------ | :----- | :----- |
| [EggShell](https://github.com/neoneggplant/EggShell) | iOS/macOS/Linux Remote Administration Tool.  | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [Mimipenguin](https://github.com/huntergregal/mimipenguin) | A tool to dump the login password from the current linux user. | ![opensource](icons/opensource.png) |










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Mobile

*Tools and resources for pentesting on mobile applications.*

#### 🔴 App/File Management

| Tool | Description | Directory |
| :------ | :----- | :----- |
| [adb](https://source.android.com/setup/build/adb) | Allows you to install packages and evaluate your changes. | ![opensource](icons/opensource.png) |
| [Airdroid](https://www.airdroid.com/en/pricing/airdroid-personal/) | Transfer files across devices, remote control Android devices, mirror screen, and manage SMS & notification on computer. | ![freemium-service](icons/freemium-service.png) |
| [Android File Transfer](https://www.android.com/filetransfer/) | Browse and transfer files between your Mac computer and your Android device. | ![opensource](icons/opensource.png) |
| [iFunbox](https://www.i-funbox.com/en/index.html) | General file management software for iPhone and other Apple products. | N/A |
| [iMazing](https://imazing.com/) | Powerful user-friendly iOS device manager for Mac and PC. | ![freemium-service](icons/freemium-service.png) |

#### 🔴 Bug Bounty Reports

| Tool | Description | Directory |
| :------ | :----- | :----- |
| [Android Reports & Reports](https://github.com/B3nac/Android-Reports-and-Resources) | Android reports and resources. | ![opensource](icons/opensource.png) |

#### 🔴 Dynamic Analysis

| Tool | Description | Directory |
| :------ | :----- | :----- |
| [Bytecode Viewer](https://github.com/konloch/bytecode-viewer) | A lightweight user friendly Java Bytecode Viewer | ![opensource](icons/opensource.png) |
| [CuckooDroid](https://github.com/idanr1986/cuckoo-droid) | Automated Android Malware Analysis with Cuckoo Sandbox.  | ![opensource](icons/opensource.png) |
| [Cutter](https://github.com/rizinorg/cutter) | Reverse engineering platform powered by rizin. | ![opensource](icons/opensource.png) |
| [DECAF](https://github.com/decaf-project/DECAF) | DECAF (short for Dynamic Executable Code Analysis Framework) is a binary analysis platform based on QEMU. | ![opensource](icons/opensource.png) |
| [Droid-FF](https://github.com/antojoseph/droid-ff) | The android fuzzing framework | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [Drozer](https://github.com/FSecureLABS/drozer) | Security testing framework for Android | ![opensource](icons/opensource.png) |
| [Hooker](https://github.com/AndroidHooker/hooker) | Provides various tools and applications that can be use to automatically intercept and modify any API calls | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [House](https://github.com/nccgroup/house) | A runtime mobile application analysis toolkit with a Web GUI, powered by Frida, written in Python. | ![opensource](icons/opensource.png) |
| [Inspeckage](https://github.com/ac-pm/Inspeckage) | Tool developed to offer dynamic analysis of Android applications | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | An automated, all-in-one mobile application (Android/iOS/Windows) pen-testing, malware analysis and security assessment framework. | ![opensource](icons/opensource.png) |
| [PATDroid](https://github.com/mingyuan-xia/PATDroid) | A collection of tools and data structures for analyzing Android applications and the system itself. | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [ProbeDroid](https://github.com/ZSShen/ProbeDroid) | A dynamic Java code instrumentation for Android apps. Provides APIs for users to craft their own instrumentation tools. | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [radare2](https://github.com/radareorg/radare2) | Set of libraries, tools and plugins to ease reverse engineering tasks. | ![opensource](icons/opensource.png) |
| [Runtime Mobile Security (RMS)](https://github.com/m0bilesecurity/RMS-Runtime-Mobile-Security) | Powered by FRIDA a powerful web interface that helps you to manipulate Android and iOS Apps at Runtime. | ![opensource](icons/opensource.png) |

#### 🔴 Flashing/Sideloading

| Tool | Description | Directory |
| :------ | :----- | :----- |
| [Cydia Impactor](http://www.cydiaimpactor.com/) | Allows you to install packages and evaluate your changes. | N/A |
| [Odin](https://odindownload.com/) | Allows you to install packages and evaluate your changes. | N/A |

#### 🔴 Guides & References

| Tool | Description | Directory |
| :------ | :----- | :----- |
| [Android Application Penetration Testing Checklist](https://www.xmind.net/m/GkgaYH/#) | Android pentesting checklist mindmap. | ![opensource](icons/opensource.png) |
| [iOS Pentesting](https://www.mindmeister.com/1713501700/ios-pentesting?fullscreen=1) | iOS pentesting mindmap. | ![opensource](icons/opensource.png) |

#### 🔴 Jailbreaking/Rooting

| Tool | Description | Directory |
| :------ | :----- | :----- |
| [canijailbreak](http://canijailbreak.com/) | A website which tells you whether you can jailbreak your iOS device. | ![opensource](icons/opensource.png) |
| [Checkra1n](https://checkra.in/) | Jailbreak for iPhone 5s through iPhone X, iOS 12.0 and up. | N/A |
| [Chimera](https://chimera.coolstar.org/) | iOS 12 jailbreak to not only feature a CoreTrust bypass so that binaries don't need to be resigned, but to also support A12 devices, including iPhone Xs, iPhone Xr, and the newest iPads. | N/A |
| [Double H3lix](https://doubleh3lix.tihmstar.net/) | Jailbreak for 64-bit 10.x devices. | N/A |
| [Etason](https://etasonjb.tihmstar.net/) | Jailbreak for all devices running iOS 8.4.1 32 bit. | N/A |
| [Evasi0n](https://www.iphonehacks.com/download-evasi0n) | Jailbreak iPhone, iPad or iPod touch on iOS 7.0 – iOS 7.0.6 | N/A |
| [H3lix](https://h3lix.tihmstar.net/) | Jailbreak for 32-bit 10.x devices. | N/A |
| [Home Depot](http://wall.supplies/) | Jailbreak for iOS 9.x devices | N/A |
| [IPSW](https://ipsw.me/) | Download current and previous versions of Apple's iOS, iPadOS, watchOS, tvOS and audioOS firmware and receive notifications when new firmwares are released.  | N/A |
| [Magisk](https://github.com/topjohnwu/Magisk) | Magisk is a suite of open source software for customizing Android, supporting devices higher than Android 5.0. | N/A |
| [Pangu Jailbreak](http://en.9.pangu.io/) | Jailbreak for iOS 9.0 - 9.1 | N/A |
| [Phoenix](https://phoenixpwn.com/) | Semi-untethered jailbreak for 9.3.5-9.3.6. All 32-bit devices supported. | N/A |
| [p0sixspwn](https://ih8sn0w.com/p0sixspwn.html) | iOS Jailbreak for 6.1.X | N/A |
| [redsn0w](https://ipsw.me/iPhoneDev) | Jailbreak for iOS 3-5 | N/A |
| [TaiG](http://www.taig.com/) | Jailbreak for iOS 8.X. | N/A |
| [unc0ver](https://unc0ver.dev/) | A jail​break tool. | N/A |


#### 🔴 Labs/Practice

| Tool | Description | Directory |
| :------ | :----- | :----- |
| [DIVA](http://www.decompileandroid.com/) | DIVA (Damn insecure and vulnerable App) is an Android App intentionally designed to be insecure. | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [DVHMA](https://github.com/logicalhacking/DVHMA) | Damn Vulnerable Hybrid Mobile App (DVHMA) is an hybrid mobile app (for Android) that intentionally contains vulnerabilities. | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [Injured Android](https://github.com/B3nac/InjuredAndroid) | A vulnerable Android application that shows simple examples of vulnerabilities in a ctf style.  | ![opensource](icons/opensource.png) |
| [InsecureBank v2](https://github.com/dineshshetty/Android-InsecureBankv2) | Vulnerable Android application for developers and security enthusiasts to learn about Android insecurities. | ![opensource](icons/opensource.png) |
| [Oversecured Vulnerable Android App](https://github.com/oversecured/ovaa) | An Android app that aggregates all the platform's known and popular security vulnerabilities. | ![opensource](icons/opensource.png) |
| [UnCrackable Apps](https://github.com/OWASP/owasp-mstg/blob/master/Crackmes/README.md) | A collection of mobile reverse engineering challenges for iOS and Android. | ![opensource](icons/opensource.png) |
| [Vuldroid](https://github.com/jaiswalakshansh/Vuldroid) |  Vuldroid is a Vulnerable Android Application made with security issues in order to demonstrate how they can occur in code. | ![opensource](icons/opensource.png) |
| [VyAPI](https://github.com/appsecco/VyAPI) | The Modern Cloud-Based Vulnerable Hybrid Android App. | ![opensource](icons/opensource.png) |
| [WaTF-Bank](https://github.com/WaTF-Team/WaTF-Bank) |  What a Terrible Failure Mobile Banking Application for Android and iOS.  | ![opensource](icons/opensource.png) |

#### 🔴 Online Services    

| Tool | Description | Directory |
| :------ | :----- | :----- |
| [Android APK Decompiler](http://www.decompileandroid.com/) | Online android decompiler | N/A |
| [Ostorlab](https://oversecured.com/) | Online static taint analysis, 3rd party fingerprinting, and vulnerability analysis. | ![freemium-service](icons/freemium-service.png) |
| [Oversecured](https://oversecured.com/) | Android mobile app analyzer vulnerability scanner, designed for DevOps process integration. | ![freemium-service](icons/freemium-service.png) |
| [Quixxi](https://quixxisecurity.com/) | An intelligent and integrated end-to-end mobile app security solution. | ![freemium-service](icons/freemium-service.png) |

#### 🔴 Post Exploitation

| Tool | Description | Directory |
| :------ | :----- | :----- |
| [EggShell](https://github.com/neoneggplant/EggShell) | iOS/macOS/Linux Remote Administration Tool.  | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |

#### 🔴 Static Analysis

| Tool | Description | Directory |
| :------ | :----- | :----- |
| [Android Check](https://github.com/noveogroup/android-check) | Static code analysis plugin for Android project. | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [Androwarn](https://github.com/maaaaz/androwarn/) | Static code analyzer for malicious Android applications. | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [APKLab](https://github.com/APKLab/APKLab) | A tool for reverse engineering 3rd party, closed, binary Android apps. | ![opensource](icons/opensource.png) |
| [APKLeaks](https://github.com/dwisiswant0/apkleaks) | Scanning APK file for URIs, endpoints & secrets. | ![opensource](icons/opensource.png) |
| [APKScanner](https://github.com/n3k00n3/APKScanner) | The objective of this scanner is to find for misconfiguration, sensitive data and insecure components. | ![opensource](icons/opensource.png) |
| [APK Studio](https://github.com/vaibhavpandeyvpz/apkstudio) | The objective of this scanner is to find for misconfiguration, sensitive data and insecure components. | ![opensource](icons/opensource.png) |
| [APKTool](https://ibotpeaches.github.io/Apktool/) | Seamlessly integrates the best open-source tools right inside VS Code. | ![opensource](icons/opensource.png) |
| [Argus-SAF](https://github.com/arguslab/Argus-SAF) | Static analysis framework | ![opensource](icons/opensource.png) |
| [Checkstyle](https://github.com/checkstyle/checkstyle) | A tool for checking Java source code for adherence to a Code Standard or set of validation rules. | ![opensource](icons/opensource.png) |
| [DeGuard](http://apk-deguard.com/) | Statistical Deobfuscation for Android. | ![opensource](icons/opensource.png) |
| [Deoptfuscator](https://github.com/Gyoonus/deoptfuscator) | Reverse the control-flow obfuscation performed by DexGuard on open-source Android applications. | ![opensource](icons/opensource.png) |
| [Droid-Hunter](https://github.com/hahwul/droid-hunter) | Android application vulnerability analysis and Android pentest tool. | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [Error Prone](https://github.com/google/error-prone) | Error Prone is a static analysis tool for Java that catches common programming mistakes at compile-time. | ![opensource](icons/opensource.png) |
| [FindBugs](http://findbugs.sourceforge.net/downloads.html) | Uses static analysis to inspect Java bytecode for occurrences of bug patterns. | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [Find Security Bugs](https://github.com/find-sec-bugs/find-sec-bugs/) | Find Security Bugs is the SpotBugs plugin for security audits of Java web applications. | ![opensource](icons/opensource.png) |
| [FlowDroid](https://github.com/secure-software-engineering/FlowDroid) | Statically computes data flows in Android apps and Java programs. | ![opensource](icons/opensource.png) |
| [Gradle](https://github.com/novoda/gradle-static-analysis-plugin) | Supports many popular static analysis (Checkstyle, PMD, FindBugs, etc) via a set of built-in plugins. | ![opensource](icons/opensource.png) |
| [Infer](https://github.com/facebook/infer) | Infer is a static analysis tool for Java, C++, Objective-C, and C. Infer is written in OCaml. | ![opensource](icons/opensource.png) |
| [JADX](https://github.com/skylot/jadx) | Dex to Java decompiler. | ![opensource](icons/opensource.png) |
| [Mobile Audit](https://github.com/mpast/mobileAudit) | SAST and Malware Analysis for Android Mobile APKs | ![opensource](icons/opensource.png) |
| [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | An automated, all-in-one mobile application (Android/iOS/Windows) pen-testing, malware analysis and security assessment framework. | ![opensource](icons/opensource.png) |
| [PMD](https://github.com/pmd/pmd) | Finds common programming flaws like unused variables, empty catch blocks, unnecessary object creation, and so forth. | ![opensource](icons/opensource.png) |
| [Qark](https://github.com/linkedin/qark) | designed to look for several security related Android application vulnerabilities, either in source code or packaged APKs. | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [Quark](https://github.com/quark-engine/quark-engine) | An Obfuscation-Neglect Android Malware Scoring System. | ![opensource](icons/opensource.png) |
| [Smali](https://github.com/JesusFreke/smali) | An assembler/disassembler for the dex format used by dalvik, Android's Java VM implementation.  | ![opensource](icons/opensource.png) |
| [Smali-CFG](https://github.com/EugenioDelfa/Smali-CFGs) | Smali Control Flow Graph's | ![opensource](icons/opensource.png) |
| [Soot](https://github.com/soot-oss/soot) | Smali Control Flow Graph's | ![opensource](icons/opensource.png) |
| [Sparta](https://github.com/typetools/sparta/) | Static program analysis for reliable trusted apps. | ![opensource](icons/opensource.png) |
| [StaCoAn](https://github.com/vincentcox/StaCoAn) | A crossplatform tool which aids developers, bugbounty hunters and ethical hackers performing static code analysis on mobile applications | ![archive](icons/archive.png) ![opensource](icons/opensource.png) |
| [Trueseeing](https://github.com/monolithworks/trueseeing) | A fast, accurate and resillient vulnerabilities scanner for Android apps. | ![opensource](icons/opensource.png) |
| [Yaazhini](https://www.vegabird.com/yaazhini/) | A fast, accurate and resillient vulnerabilities scanner for Android apps. | N/A |

#### 🔴 Video Content

| Tool | Description | Directory |
| :------ | :----- | :----- |
| [B3nac Sec](https://www.youtube.com/c/B3nacSec/featured) | Dedicated mobile ethical hacking | N/A |

#### 🔴 Virtualization

| Tool | Description | Directory |
| :------ | :----- | :----- |
| [Android Tamer](https://androidtamer.com/) | Live Platform for Android Security professionals. | ![no-recent-update](icons/no-recent-update.png) |
| [AppUse](https://appsec-labs.com/appuse/) | Mobile app security testing, Android and iOS applications. Custom-made tools and scripts created by AppSec Labs. | ![paid-product](icons/paid-product.png) |

#### 🔴 Whitepapers

| Tool | Description | Directory |
| :------ | :----- | :----- |
| [Android Rooting:Methods, Detection, and Evastion](http://lersse-dl.ece.ubc.ca/record/310/files/p3.pdf) | Written by San-Tsai Sun, Andrea Cuadros, and Konstantin Beznosov. | N/A | 










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Network

*Below are some of the most common hardware pieces owned by most security researchers.*

#### 🔴 Denial of Service

| Tool | Description | Directory |
| :----- | :----- | :----- |
| [DAVOSET](https://github.com/MustLive/DAVOSET) | a tool for committing distributed denial of service attacks using execution on other sites. | ![no-recent-update](icons/no-recent-update.png)  ![opensource](icons/opensource.png) |
| [DDOSIM](https://sourceforge.net/projects/ddosim/) | Layer 7 DDoS Simulator | ![no-recent-update](icons/no-recent-update.png)  ![opensource](icons/opensource.png) |
| [GoldenEye](https://github.com/jseidl/GoldenEye) | A HTTP DoS Test Tool | ![archive](icons/archive.png) ![opensource](icons/opensource.png) |
| [HOIC](https://sourceforge.net/projects/highorbitioncannon/) | A network stress testing application | ![no-recent-update](icons/no-recent-update.png) |
| [Http Unbreakable Load King (HULK)](https://packetstormsecurity.com/files/112856/HULK-Http-Unbearable-Load-King.html) | A web server tool generates volumes of unique obfuscated traffic | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [LOIC](https://github.com/NewEraCracker/LOIC) | A network stress testing application | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [PyLoris](https://motoma.io/pyloris/) | Scriptable tool for testing a services level of DoS handling | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [R-U-Dead-Yet (RUDY)](https://github.com/sahilchaddha/rudyjs) | Attack targeted web applications by starvation of available sessions on the web server | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [Slowloris](https://github.com/gkbrk/slowloris) | An HTTP Denial of Service attack that affects threaded servers | ![opensource](icons/opensource.png) |
| [TORs Hammer](https://github.com/Karlheinzniebuhr/torshammer) | Slow POST DoS testing tool ran through TOR | ![opensource](icons/opensource.png) |

#### 🔴 LAN/WAN

| Tool | Description | Directory |
| :----- | :----- | :----- |
| [dpkt](https://github.com/kbandla/dpkt) | Fast, simple packet creation / parsing, with definitions for the basic TCP/IP protocols. | ![opensource](icons/opensource.png) |
| [Ghost Phisher](https://github.com/savio-code/ghost-phisher) | A Wireless and Ethernet security auditing and attack software | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [Impacket](https://github.com/SecureAuthCorp/impacket) | Impacket is a collection of Python classes for working with network protocols. | ![opensource](icons/opensource.png) |
| [Libdnet](https://github.com/ofalk/libdnet) | Provides a simplified, portable interface to several low-level networking routines. | ![opensource](icons/opensource.png) |
| [Scapy](https://github.com/secdev/scapy) | Python-based interactive packet manipulation program & library. | ![opensource](icons/opensource.png) |


#### 🔴 Port/Network Scanning

| Tool | Description | Directory |
| :----- | :----- | :----- |
| [masscan](https://github.com/robertdavidgraham/masscan) | TCP port scanner, spews SYN packets asynchronously, scanning entire Internet in under 5 minutes. | ![opensource](icons/opensource.png) |
| [naabu](https://github.com/projectdiscovery/naabu) | A fast port scanner written in go with a focus on reliability and simplicity. | ![opensource](icons/opensource.png) |
| [NMAP](https://github.com/nmap/nmap) | The Network Mapper. | ![opensource](icons/opensource.png) |
| [RustScan](https://github.com/RustScan/RustScan) | The Modern Port Scanner. | ![opensource](icons/opensource.png) |

#### 🔴 SSL/TLS

| Tool | Description | Directory |
| :----- | :----- | :----- |
| [TLS-DOS](https://github.com/azet/thc-tls-dos) | A tool to stress test the SSL handshake by triggering processor intensive calls on the server side | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Reconnaissance

*Understand your target. Perform in-depth research and discover new attack surfaces.*

#### 🔴 Content Discovery

| Organization | Description | Directory |
| :------ | :------ | :-------- |
| [content-discovery](https://github.com/eauxfolles/content-discovery) | Tool to support with "Content Discovery" during mapping of a web applications/sites. | ![opensource](icons/opensource.png) |
| [dirble](https://github.com/nccgroup/dirble) | Fast directory scanning and scraping tool. | ![opensource](icons/opensource.png) |
| [DirBuster](https://github.com/KajanM/DirBuster) | a multi threaded java application designed to brute force directories and files names on web/application servers. | ![opensource](icons/opensource.png) |
| [dirsearch](https://github.com/maurosoria/dirsearch) | Web path scanner. | ![opensource](icons/opensource.png) |
| [Forexbuster](https://github.com/epi052/feroxbuster) | A fast, simple, recursive content discovery tool written in Rust. | ![opensource](icons/opensource.png) |
| [ffuf](https://github.com/ffuf/ffuf) | Fast web fuzzer written in Go. | ![opensource](icons/opensource.png) |
| [GoBuster](https://github.com/OJ/gobuster) | Directory/File, DNS and VHost busting tool written in Go. | ![opensource](icons/opensource.png) |
| [Kiterunner](https://github.com/assetnote/kiterunner) | Contextual Content Discovery Tool. | ![opensource](icons/opensource.png) |
| [LinkFinder](https://github.com/GerbenJavado/LinkFinder) | A python script that finds endpoints in JavaScript files. | ![opensource](icons/opensource.png) |
| [ParamSpider](https://github.com/devanshbatham/ParamSpider) | Mining parameters from dark corners of Web Archives. | ![opensource](icons/opensource.png) |
| [Raccoon](https://github.com/evyatarmeged/Raccoon) | A high performance offensive security tool for reconnaissance and vulnerability scanning. | ![opensource](icons/opensource.png) |
| [RecurseBuster](https://github.com/C-Sto/recursebuster) | Rapid content discovery tool for recursively querying webservers. | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [Scilla](https://github.com/edoardottt/scilla) | Information Gathering tool - DNS / Subdomains / Ports / Directories enumeration. | ![opensource](icons/opensource.png) |
| [x8](https://github.com/Sh1Yo/x8) | Hidden parameters discovery suite written in Rust. | ![opensource](icons/opensource.png) |


#### 🔴 DNS

| Organization | Description | Directory |
| :------ | :------ | :-------- |
| [aiodnsbrute](https://github.com/blark/aiodnsbrute) | Python 3.5+ DNS asynchronous brute force utility. | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [dnsdumpter](https://dnsdumpster.com/) | dns recon & research, find & lookup dns records | N/A |
| [dnssearch](https://github.com/evilsocket/dnssearch) |  A subdomain enumeration tool.  | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [dnsX](https://github.com/projectdiscovery/dnsx) | Fast and multi-purpose DNS toolkit allow to run multiple DNS queries. | ![opensource](icons/opensource.png) |
| [Fierce](https://github.com/mschwager/fierce) |  A DNS reconnaissance tool for locating non-contiguous IP space. | ![opensource](icons/opensource.png) |
| [MassDNS](https://github.com/blechschmidt/massdns) | A high-performance DNS stub resolver for bulk lookups and reconnaissance | ![opensource](icons/opensource.png) |
| [Raccoon](https://github.com/evyatarmeged/Raccoon) | A high performance offensive security tool for reconnaissance and vulnerability scanning. | ![opensource](icons/opensource.png) |
| [SubBrute](https://github.com/TheRook/subbrute) | A DNS meta-query spider that enumerates DNS records, and subdomains. | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |

#### 🔴 Domains

| Organization | Description | Directory |
| :------ | :------ | :-------- |
| [Altdns](https://github.com/infosec-au/altdns) | Generates permutations, alterations and mutations of subdomains and then resolves them. | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [Amass](https://github.com/OWASP/Amass) | In-depth Attack Surface Mapping and Asset Discovery. | ![opensource](icons/opensource.png) |
| [Assetfinder](https://github.com/tomnomnom/assetfinder) | Find domains and subdomains potentially related to a given domain. | ![opensource](icons/opensource.png) |
| [crt.sh](https://crt.sh/) | Certificate search on domains. | N/A |
| [ctfr](https://github.com/UnaPibaGeek/ctfr) | Abusing Certificate Transparency logs for getting HTTPS websites subdomains. | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [Discover](https://github.com/leebaird/discover) | Custom bash scripts to automate various pentesting tasks including recon. | ![opensource](icons/opensource.png) |
| [findomain](https://github.com/Findomain/Findomain) | The complete solution for domain recognition. | ![freemium-service](icons/freemium-service.png) ![opensource](icons/opensource.png) ![register-profile](icons/register-profile.png) |
| [findsubdomains.com (spyse)](https://spyse.com/tools/subdomain-finder) | subdomain finder in order to make your reconnaissance process faster and effortless. | ![freemium-service](icons/freemium-service.png) ![register-profile](icons/register-profile.png) |
| [Knock](https://github.com/guelfoweb/knock) | Knock Subdomain Scan. | ![opensource](icons/opensource.png) |
| [OneForAll](https://github.com/shmilylty/OneForAll) | A powerful subdomain integration tool | ![opensource](icons/opensource.png) |
| [PD Actions](https://github.com/projectdiscovery/pd-actions) | Continous reconnaissance and vuln assesment using Github Actions | ![opensource](icons/opensource.png) |
| [Raccoon](https://github.com/evyatarmeged/Raccoon) | A high performance offensive security tool for reconnaissance and vulnerability scanning. | ![opensource](icons/opensource.png) |
| [Robtex](https://www.robtex.com/) | Robtex is used for various kinds of research of IP numbers, Domain names, etc. | N/A |
| [Scilla](https://github.com/edoardottt/scilla) | Information Gathering tool - DNS / Subdomains / Ports / Directories enumeration. | ![opensource](icons/opensource.png) |
| [sigurlfind3r](https://github.com/signedsecurity/sigurlfind3r) | A reconnaissance tool, it fetches URLs from AlienVault's OTX, Common Crawl, URLScan, Github and the Wayback Machine. | ![opensource](icons/opensource.png) |
| [subfinder](https://github.com/projectdiscovery/subfinder) | Fast passive subdomian enumeration tool | ![opensource](icons/opensource.png) |
| [sublist3r](https://github.com/aboul3la/Sublist3r) |  Fast subdomains enumeration tool for penetration testers. | ![opensource](icons/opensource.png) |
| [Turbolist3r](https://github.com/aboul3la/Sublist3r) | Subdomain enumeration tool with analysis features for discovered domains. | ![opensource](icons/opensource.png) |

#### 🔴 Dorking

| Tool | Description | Directory |
| :------ | :------ |  :------- |
| [Dorkbot](https://github.com/utiso/dorkbot) |  Command line dorking tool | ![opensource](icons/opensource.png) |

#### 🔴 Frameworks

| Organization | Description | Directory |
| :------ | :------ | :-------- |
| [Osmedeus](https://github.com/j3ssie/Osmedeus) | Fully automated offensive security framework for reconnaissance and vulnerability scanning. | ![freemium-service](icons/freemium-service.png) ![register-profile](icons/register-profile.png) ![opensource](icons/opensource.png) |
| [sn1per](https://github.com/1N3/Sn1per) | Discover the attack surface and prioritize risks with our continuous Attack Surface Management. | ![freemium-service](icons/freemium-service.png) ![register-profile](icons/register-profile.png) ![opensource](icons/opensource.png) |

#### 🔴 Search Engines

| Organization | Description | Directory |
| :------ | :------ | :------- |
| [Censys](https://censys.io/) | Highly-indexed Internet-wide scan data at scale | ![freemium-service](icons/freemium-service.png)|
| [Google Dataset](https://datasetsearch.research.google.com/) | Indexed datasets | N/A |
| [Mamont](https://www.mmnt.ru/int/) | Open FTP Indexer | N/A |
| [Napalm](https://www.searchftps.net/) | Open FTP Indexer | N/A |
| [OCCRP Aleph](https://data.occrp.org/) | Global archive of research material | N/A |
| [OnionScan](https://github.com/s-rah/onionscan) | TOR scanner | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [Shodan](https://shodan.io) | The security search engine. Search everything IoT | ![freemium-service](icons/freemium-service.png)|
| [Wayback Machine](https://archive.org/web/web.php) | Internet archive of saved web pages | N/A |

#### 🔴 Wordlists

| Tool | Description | Directory |
| :------ | :------ |  :------- |
| [API Endpoints & Objects](https://gist.github.com/yassineaboukir/8e12adefbd505ef704674ad6ad48743d) | A list of 3203 common API endpoints and objects designed for fuzzing. | ![opensource](icons/opensource.png) |
| [Funny Fuzzing Wordlist](https://github.com/koaj/ffw-content-discovery) | Funny Fuzzing Wordlist. | ![opensource](icons/opensource.png) |
| [SecLists](https://github.com/danielmiessler/SecLists) | A collection of multiple types of lists used during security assessments, collected in one place. | ![opensource](icons/opensource.png) |










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Social Engineering

*Manipulation techniques that exploits human error to gain private information, access, or valuables.*

#### 🔴 Phishing

| Tool | Description | Directory |
| :----- | :----- | :------- |
| [Evilgnix](https://github.com/kgretzky/evilginx2) |  MITM attack framework used for phishing credentials along with session cookies, which in turn allows to bypass 2-factor authentication protection. | ![opensource](icons/opensource.png) |
| [Fierce Phish](https://github.com/Raikia/FiercePhish) | A full-fledged phishing framework to manage all phishing engagements | ![opensource](icons/opensource.png) |
| [GoPhish](https://getgophish.com/) | Phishing toolkit designed for businesses and penetration testers | ![opensource](icons/opensource.png) |
| [Judas](https://github.com/JonCooperWorks/judas) | A pluggable phishing proxy. | ![opensource](icons/opensource.png) |
| [King Phisher](https://github.com/rsmusllp/king-phisher) | A tool for testing and promoting user awareness by simulating real world phishing attacks.| ![opensource](icons/opensource.png) |
| [Lucy](https://lucysecurity.com/download/) | Allows companies to take on the role of an attacker to discover and eliminate existing weaknesses. | ![freemium-service](icons/freemium-service.png)|
| [Phishing Frenzy](https://github.com/pentestgeek/phishing-frenzy) | Ruby on Rails Phishing Framework | ![opensource](icons/opensource.png) |
| [Shell Phish](https://github.com/suljot/shellphish/) | A Phishing tool to replicate various | ![opensource](icons/opensource.png) |
| [Social Engineering Toolkit](https://github.com/trustedsec/social-engineer-toolkit) | Penetration testing framework designed for social engineering | ![opensource](icons/opensource.png) |
| [Social Fish](https://github.com/UndeadSec/SocialFish) | Phishing framework | ![opensource](icons/opensource.png) |
| [SpeedPhish Framework](https://github.com/tatanus/SPF) | Tool designed to allow for quick recon and deployment of simple social engineering phishing exercises. | ![opensource](icons/opensource.png) |
| [SPT Project](https://github.com/chris-short/sptoolkit) | Phishing education toolkit that aims to help in securing the mind as opposed to securing computers. | ![opensource](icons/opensource.png) |

#### 🔴 SMS

| Tool | Description | Directory |
| :----- | :----- | :----- |
| [SMSSpoof](https://github.com/vpn/SMSSpoof) | Send an SMS message to someone and change who it's from (the Sender) | ![opensource](icons/opensource.png) |










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Vulnerability Scanners

*Discover vulnerabilities fast, and automate some of the heavy loads.*

#### 🔴 Scanners

| Tool | Descrption | Directory |
| :----- | :----- | :------- |
| [Acunetix](https://www.acunetix.com/vulnerability-scanner/) | a complete web application security testing solution that can be used both standalone and as part of complex environments. | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |
| [Alibaba Cloud Security Scanner](https://www.alibabacloud.com/product/avds) | CSS utilizes data, white hat pentesting, and ML to provide an all-in-one security solution for domains and other online assets. | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |
| [Amazon Inspector](https://aws.amazon.com/inspector/pricing/) | Automated security assessment service to help improve the security and compliance of applications deployed on AWS. | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |
| [AT&T Managed Vulnerability Program](https://cybersecurity.att.com/products/managed-vulnerability-program) | Vulnerability management services that fit your business. | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |
| [Burp Suite](https://portswigger.net/burp/vulnerability-scanner) | PortSwigger's world-leading research to help its users find a wide range of vulnerabilities in web applications, automatically.  | ![freemium-service](icons/freemium-service.png) ![register-profile](icons/register-profile.png) |
| [ManageEngine](https://www.manageengine.com/vulnerability-management/) | Gain 360 degree visibility into your security exposure. | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |
| [Nessus](https://www.tenable.com/products/nessus) | Proprietary vulnerability scanner developed by Tenable, Inc. | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |
| [Nexpose](https://www.rapid7.com/products/nexpose/) | Your on-prem vulnerability scanner. | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |
| [nuclei](https://github.com/projectdiscovery/nuclei) | Fast and customisable vulnerability scanner based on simple YAML based DSL. | ![opensource](icons/opensource.png) |
| [OpenVAS](https://openvas.org/) | A full-featured vulnerability scanner. | ![freemium-service](icons/freemium-service.png) ![register-profile](icons/register-profile.png) |
| [ZAP](https://www.zaproxy.org/) | World's most widely used web app scanner. | ![opensource](icons/opensource.png) |










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Windows

*Microsoft Windows pentesting tools/resouces.*

#### 🔴 Active Directory 

| Tool | Descrption | Directory |
| :----- | :----- | :------- |
| [BloodHound](https://github.com/BloodHoundAD/BloodHound) |  Six Degrees of Domain Admin. | ![opensource](icons/opensource.png) |
| [CrackMapExec](https://github.com/byt3bl33d3r/CrackMapExec) | A swiss army knife for pentesting networks. | ![opensource](icons/opensource.png) |

#### 🔴 Bitlocker

| Tool | Descrption | Directory |
| :----- | :----- | :------- |
| [Bitleaker](https://github.com/kkamagui/bitleaker) | This tool can decrypt a BitLocker-locked partition with the TPM vulnerability. | ![opensource](icons/opensource.png) |

#### 🔴 Cheatsheets

| Tool | Description | Directory |
| :------ | :----- | :----- |
| [LOLBAS](https://lolbas-project.github.io/#) | Living Off The Land Binaries and Scripts. | ![opensource](icons/opensource.png) |

#### 🔴 Kerberos

| Tool | Descrption | Directory |
| :----- | :----- | :------- |
| [Kerberoast](https://github.com/nidem/kerberoast) | A series of tools for attacking MS Kerberos implementations. | ![opensource](icons/opensource.png) |
| [Pykek](https://github.com/mubix/pykek) | A python library to manipulate KRB5-related data. | ![opensource](icons/opensource.png) |
| [Rubeus](https://github.com/GhostPack/Rubeus) | A C# toolset for raw Kerberos interaction and abuses. | ![opensource](icons/opensource.png) |


#### 🔴 Memory

| Tool | Descrption | Directory |
| :----- | :----- | :------- |
| [Blackbone](https://github.com/DarthTon/Blackbone) |  DLL scatter manual mapper. | ![opensource](icons/opensource.png) |

#### 🔴 Post Exploitation

| Tool | Descrption | Directory |
| :----- | :----- | :------- |
| [Mimikatz](https://github.com/gentilkiwi/mimikatz) | Experiments with Windows security. | ![opensource](icons/opensource.png) |

#### 🔴 Powershell

| Tool | Descrption | Directory |
| :----- | :----- | :------- |
| [Pentestly](https://github.com/praetorian-inc/pentestly) | Python and Powershell internal penetration testing framework  | ![opensource](icons/opensource.png) |
| [Powershell Suite](https://github.com/FuzzySecurity/PowerShell-Suite) | A collection of PowerShell utilities. | ![opensource](icons/opensource.png) |


#### 🔴 RDP

| Tool | Descrption | Directory |
| :----- | :----- | :------- |
| [SharpRDP](https://github.com/0xthirteen/SharpRDP) | Remote Desktop Protocol .NET Console Application for Authenticated Command Execution. | ![opensource](icons/opensource.png) |

#### 🔴 Scripts

| Tool | Descrption | Directory |
| :----- | :----- | :------- |
| [LOLBAS](https://lolbas-project.github.io/#) | Living Off The Land Binaries and Scripts | ![opensource](icons/opensource.png) |
| [Windows-Pentest](https://github.com/ankh2054/windows-pentest) | Windows Pentest Scripts  | ![opensource](icons/opensource.png) |









### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Web Application

*Discover tools and resources for exploiting Wi-Fi, bluetooth, RFID, and more.*

#### 🔴 Cross-Site Scripting

| Tool | Descrption | Directory |
| :----- | :----- | :------- |
| [XSS'OR](https://github.com/evilcos/xssor2) | XSS'OR - Hack with JavaScript. | ![opensource](icons/opensource.png) |

#### 🔴 Protocols

| Tool | Descrption | Directory |
| :----- | :----- | :------- |
| [http-request-smuggling](https://github.com/anshumanpattnaik/http-request-smuggling) | HTTP Request Smuggling Detection Tool. | ![opensource](icons/opensource.png) |










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Wireless

*Discover tools and resources for exploiting Wi-Fi, bluetooth, RFID, and more.*

#### 🔴 Bluetooth

| Tool | Descrption | Directory |
| :----- | :----- | :------- |
| [bettercap](https://www.bettercap.org/) | Swiss army knife for WiFi, Bluetooth, HID, and ethernet network. | ![opensource](icons/opensource.png) |
| [Bluelog](https://github.com/MS3FGX/Bluelog) | Linux bluetooth scanner | ![opensource](icons/opensource.png) |
| [hcitool](https://github.com/MillerTechnologyPeru/hcitool) | Bluetooth host controller CLI tool for sending HCI commands on MacOS and Linux. | ![opensource](icons/opensource.png) |


#### 🔴 Wi-Fi

| Tool | Descrption | Directory |
| :----- | :----- | :------ |
| [Aircrack-NG](https://www.aircrack-ng.org/) | A complete suite of tools assess WiFi network security. | ![opensource](icons/opensource.png) |
| [bettercap](https://www.bettercap.org/) | Swiss army knife for WiFi, Bluetooth, HID, and ethernet network. | ![opensource](icons/opensource.png) |
| [Reaver](https://github.com/t6x/reaver-wps-fork-t6x) | Brute force attack against  Wi-Fi Protected Setups (WPS) | ![opensource](icons/opensource.png) |










***

## [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Operation Security

*Watch your tracks you leave across the internet. Up your operation security (OpSec) and don't get caught slipping.*










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Anonymity

*The quality or state of being anonymous. Seek out technologies and methods of remaining anonymous in the day and age of mass surveillance.*

#### 👻 Browsing

| Tools | Description | Directory |
| :------ | :----- | :----- |
| [I2P](https://geti2p.net/en/) | An anonymous network layer that allows for censorship resistant, peer to peer communication.  | N/A |
| [Pantoclick](https://coveryourtracks.eff.org/) | See how trackers view your browser | N/A |
| [TOR](https://www.torproject.org/) | Free and open-source software for enabling anonymous communication. | ![opensource](icons/opensource.png) |
| [WEBKAY](https://webkay.robinlinus.com/) | A web app to show what every browser knows about you. | N/A |

#### 👻 Cryptocurrency

| Organization | Description | Directory | 
| :------ | :----- | :----- |
| [Monero](https://www.getmonero.org/) | Secure, private, untraceable. | ![paid-product](icons/paid-product.png) |
| [ZCash](https://z.cash/) | Proxies without limits. Take your business to a higher level. | ![paid-product](icons/paid-product.png) |

#### 👻 Cryptocurrency Wallets

| Organization | Description | Directory | 
| :------ | :----- | :----- |
| [Bitlox](https://www.exodus.com/) | Bitcoin mobile hardware wallet bluetooth low energy high security. | ![opensource](icons/opensource.png) |
| [Exodus](https://www.exodus.com/) | Laptop and Desktop crypto wallet. | ![opensource](icons/opensource.png) |
| [Samourai](https://samouraiwallet.com/) | A bitcoin wallet for the streets | ![opensource](icons/opensource.png) |
| [Wasabi](https://www.wasabiwallet.io/) | Bitcoin privacy wallet with built-in CoinJoin | ![opensource](icons/opensource.png) |

#### 👻 Domain Registrars

| Organization | Description | Directory | 
| :------ | :----- | :----- |
| [Njalla](https://njal.la/) [[TOR]](http://njallalafimoej5i4eg7vlnqjvmb6zhdh27qxcatdn647jtwwwui3nad.onion/) | A privacy-aware domain service.. | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |

#### 👻 Proxies

| Organization | Description | Directory | 
| :------ | :----- | :----- |
| [Proxy Shop](https://proxy.shop/) | Proxy Shop with 8M+ locations, 160+ countries, and 50+ states. | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |
| [Smarter Proxy](https://smartproxy.com/) | Proxies without limits. Take your business to a higher level. | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |

#### 👻 VPN

| Organization | Description | Directory | 
| :------ | :----- | :----- |
| [Comparision Sheet](https://docs.google.com/spreadsheets/d/1V1MFJJqwAtn9O_WgynUMXRbXLhsY2SAViADYsLZy63U/edit#gid=0) | VPN comparision sheet. | ![opensource](icons/opensource.png) |
| [Mullvad VPN](https://mullvad.net/en/) [[TOR](http://xcln5hkbriyklr6n.onion/)] | Service that helps keep your online activity, identity, and location private. | ![opensource](icons/opensource.png) ![tor-icon](icons/tor-icon.png) |
| [ProtonVPN](https://protonvpn.com/) | High-speed Swiss VPN that safeguards your privacy. |  ![freemium-service](icons/freemium-service.png) ![opensource](icons/opensource.png) ![register-profile](icons/register-profile.png) |

#### 👻 Whistleblowing

| Organization | Description | Directory |
| :------ | :----- | :-------|
| [Global Leaks](https://www.globaleaks.org/) [[TOR](sunkfzudgd2lrv6hncwdhnemrm5lcu7ejb6iem5shrliljx7m27mukyd.onion)] | Free and open source whistleblowing software, under the AGPL License |  ![opensource](icons/opensource.png) ![tor-icon](icons/tor-icon.png) |
| [SecureDrop](https://securedrop.org/) [[TOR](http://sdolvtfhatvsysc6l34d65ymdwxcujausv7k5jk4cy5ttzhjoi6fzvyd.onion)] | Share and accept documents securely. |  ![opensource](icons/opensource.png) ![tor-icon](icons/tor-icon.png) |










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Communication

*Protect your SMS messages, voice calls, and e-mails. Big brother is always watching.*

#### 👻 E-Mail Services

| Organization | Description | Directory |
| :------ | :----- | :------- |
| [CTemplar](https://ctemplar.com/) [[TOR](http://ctemplarpizuduxk3fkwrieizstx33kg5chlvrh37nz73pv5smsvl6ad.onion/)] | Anonymous E2EE (End to End Encrypted) email. | ![freemium-service](icons/freemium-service.png) ![register-profile](icons/register-profile.png) ![tor-icon](icons/tor-icon.png) |
| Noxe [[TOR](http://noxe622edajixluakfmma5dolaakdtmhfgtz7ninulfnecsbwoybogyd.onion/)] | E-Mail provider | ![register-profile](icons/register-profile.png) ![tor-icon](icons/tor-icon.png) |
| SecMail [[TOR](http://secmail63sex4dfw6h2nsrbmfz2z6alwxe4e3adtkpd4pcvkhht4jdad.onion/)] | Secure mail service in TOR. | ![freemium-service](icons/freemium-service.png) ![register-profile](icons/register-profile.png) ![tor-icon](icons/tor-icon.png) |
| [Premium Vendor](https://premiumvendor.net/) | E-Mail provider utilized by vendors all around the world. | ![register-profile](icons/register-profile.png) |
| [Protonmail](https://protonmail.com/) | Secure E-Mail based in Switzerland. | ![freemium-service](icons/freemium-service.png) ![register-profile](icons/register-profile.png) |
| [SAFe-mail](https://safe-mail.net) | Bulletproof e-mail service | ![register-profile](icons/register-profile.png) |
| TorBox [[TOR](http://torbox36ijlcevujx7mjb4oiusvwgvmue7jfn2cvutwa6kl6to3uyqad.onion/index-en.php)] | Hidden mail service. | ![register-profile](icons/register-profile.png) ![tor-icon](icons/tor-icon.png) |

#### 👻 Messaging Services

| Organization | Description | Directory |
| :------ | :----- | :----- |
| [Adamant](https://adamant.im/) | Decentralized Messenger. | ![opensource](icons/opensource.png) |
| [Briar](https://briarproject.org/) | Secure messaging, anywhere. | ![opensource](icons/opensource.png) |
| [Element](https://element.io/) | A messenger that gives you the privacy you expect from a conversation in your own home, but with everyone across the globe. | ![freemium-service](icons/freemium-service.png) ![opensource](icons/opensource.png) ![register-profile](icons/register-profile.png)|
| [Ricochet](https://ricochet.im/) | Ricochet is a different approach to instant messaging that doesn’t trust anyone in protecting your privacy. | ![no-recent-update](icons/no-recent-update.png) ![opensource](icons/opensource.png) |
| [Telegram](https://telegram.org/) | A new era of messaging. | ![opensource](icons/opensource.png) |

#### 👻 SMS

| Organization | Description | Directory |
| :------ | :----- | :------ |
| [Signal](https://www.signal.org/) | Speak Freely | ![opensource](icons/opensource.png) ![register-profile](icons/register-profile.png) |


#### 👻 XMPP Services

Want to check compliance status of an XMPP server? Check out https://compliance.conversations.im/.

| Organization | Description | Directory |
| :------ | :----- | :------ |
| [404 City](https://404.city/) | Cipher-punk community in federation XMPP. Our goal is to protect the privacy of personal life. | ![register-profile](icons/register-profile.png) |
| [Creep](https://creep.im) [[TOR](http://creep7nissfumwyx.onion)] | Free XMPP/Jabber server in France. IP's not logged. XSF standards. | ![register-profile](icons/register-profile.png) ![tor-icon](icons/tor-icon.png) |
| [CRIME](https://crime.io) | Secure & Unmonitored XMPP. Encryption Required. Registration Open. | ![register-profile](icons/register-profile.png) |
| [Hella (Shadow)](https://www.hell.la/) | Free XMPP service for secure unmonitored communications. | ![register-profile](icons/register-profile.png) |
| [Hell XMPP](https://4ept.net/xmpp/) | Russian XMPP service | ![register-profile](icons/register-profile.png) |
| [JabberX](https://jabberx.net/) | Free Private XMPP Chat Service. Designed in Sweeded and Hosted in Germany. | ![register-profile](icons/register-profile.png) |








***

## [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Purple Security

*Resources/Tools utilized by both red/blue teams.*






### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Editors and Viewers

*Tools for editing/viewing files.*

#### 🟣 Tools

| Tool | Descrption | Directory |
| :----- | :----- | :------- |
| [CyberChef](https://github.com/mattnotmax/cyberchef-recipes) | A fantastic tool for data transformation, extraction & manipulation in your web-browser. |![opensource](icons/opensource.png) | 
| [Hexed.it](https://hexed.it/) | Browser based online and offline hex editing. | N/A |
| [Hexyl](https://github.com/sharkdp/hexyl) | A command-line hex viewer  | ![opensource](icons/opensource.png) |









 ### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Emulation






#### 🟣 Adversary

| Organization | Description | Directory |
| :------ | :------ | :-------- |
| [Al-Khaser](https://github.com/LordNoteworthy/al-khaser) | Public malware techniques used in the wild: Virtual Machine, Emulation, Debuggers, Sandbox detection. | ![opensource](icons/opensource.png) |
| [DumpsterFire](https://github.com/BishopFox/sliver) | A modular, menu-driven, cross-platform tool for building customized, time-delayed, distributed security events. | ![opensource](icons/opensource.png) |
| [Silver](https://github.com/BishopFox/sliver) | Adversary Emulation Framework. | ![opensource](icons/opensource.png) |












### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Network

*Network tools both offensive and defensive operations can utilize.*

#### 🟣 Analysis

| Organization | Description | Directory |
| :------ | :------ | :-------- |
| [ngrep](https://github.com/jpr5/ngrep/) | A PCAP-based tool that allows you to specify an extended regular or hexadecimal expression to match against data payloads of packets. | ![opensource](icons/opensource.png) |










### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) OSINT

*Open-Source Intel. Get all the information needed for your target.*

#### 🟣 Business

| Organization | Description | Directory |
| :------ | :------ | :-------- |
| [Black Book](https://www.blackbookonline.info/USA-Counties.aspx) | Public records index | N/A |
| [Corporation Wiki](https://www.corporationwiki.com/) | Person and Company Wiki | ![register-profile](icons/register-profile.png) |
| [Government of Canada](https://www.ic.gc.ca/app/scr/cc/CorporationsCanada/fdrlCrpSrch.html?locale=en_CA) | Federal corporation lookup | N/A |
| [Open Gov US](https://opengovus.com/) | Open Government data in U.S. | N/A |
| [Spoke](https://www.spoke.com/) | Business, People, and more | N/A |

#### 🟣 Data Breach Dumps

| Organization | Description | Directory |
| :------ | :----- | :------ |
| [Dehashed](https://dehashed.com/) | DeHashed is constantly obtaining new and private datasets that other services simply do not have. We are always the first to respond. |  ![legal](icons/legal.png) |
| [HaveIBeenPwned](https://haveibeenpwned.com/) |  Have I Been Pwned allows you to search across multiple data breaches to see if your email address has been compromised. | N/A |
| [Leaked source](https://www.leakedsource.ru/) | Leaked Source is a collaboration of data found online in the form of a lookup. |  ![legal](icons/legal.png) |
| [Snusbase](https://www.snusbase.com/) | Snusbase indexes information from websites that have been hacked and had their database leaked. |  ![legal](icons/legal.png) |
| [WeLeakInfo V2 (Un-confirmed official site)](https://weleakinfo.to/) | Another Indexed databreach website. Proceed with caution as this is a reboot version. |  ![legal](icons/legal.png) |

#### 🟣 E-Mail

| Tool | Description | Directory |
| :------ | :----- | :------ |
| [Holehe](https://github.com/megadose/holehe) | Allows you to check if the email is used on different sites and will retrieve information on sites with the forgotten password function.  | ![opensource](icons/opensource.png) |

#### 🟣 Frameworks/Platforms

| Tool | Description | Directory |
| :------ | :----- | :------ |
| [IntelOwl](https://github.com/intelowlproject/IntelOwl) | OSINT solution to get threat intelligence data about a specific file, an IP or a domain from a single API at scale. | ![opensource](icons/opensource.png) |
| [OpenCTI](https://github.com/OpenCTI-Platform/opencti) | Open Cyber Threat Intelligence Platform. | ![opensource](icons/opensource.png) |
| [OSweep](https://github.com/ecstatic-nobel/OSweep) | Don't Just Search OSINT. Sweep It. | ![opensource](icons/opensource.png) |
| [QueryTool](https://github.com/oryon-osint/querytool) | Querytool is an OSINT framework based on Google Spreadsheets. | ![opensource](icons/opensource.png) |


#### 🟣 People

| Organization | Record Opt-Out/Removal | Directory |
| :------ | :----- | :------- |
| [411 (White Pages)](https://www.411.com/) | [CCPA](https://www.whitepages.com/privacy/ccpa) [Suppression Requests](https://www.whitepages.com/suppression-requests) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [Addresses (Intelius)](https://www.addresses.com/) | [CCPA](https://www.intelius.com/ccpa) | ![freemium](https://www.infosec.house/content/images/2021/05/freemium.png)![register-profile](icons/register-profile.png) |
| [Advanced Background Checks](https://www.advancedbackgroundchecks.com/) | [Link](https://www.advancedbackgroundchecks.com/removal) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [AnyWho (Intelius)](https://www.anywho.com/) | [Link](https://www.intelius.com/opt-out/submit/) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [Been Verified](https://www.beenverified.com/) | [Link](https://www.beenverified.com/app/optout/search) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [Black Book](https://www.blackbookonline.info/USA-Counties.aspx) | N/A | N/A |
| [Check Them](https://www.checkthem.com/) | [Link](https://www.checkthem.com/optout/) | ![freemium-service](icons/freemium-service.png)|
| [Classmates (PeopleConnect)](https://www.classmates.com/) | [Link](https://www.intelius.com/opt-out/submit/) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [Corporation Wiki](https://www.corporationwiki.com/) | [Link](https://www.corporationwiki.com/profiles/public) | ![register-profile](icons/register-profile.png) |
| [DOB Search](https://www.dobsearch.com/) | [Link](https://www.dobsearch.com/people-finder/pf_manage_help.php) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [Family Tree Now](https://www.familytreenow.com/) | [Link](https://www.familytreenow.com/privacy?removal=true) | N/A |
| [ID True](https://www.idtrue.com/) | [Link](https://www.idtrue.com/optout/) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [Instant Checkmate](https://www.instantcheckmate.com/) | [Link](https://www.instantcheckmate.com/opt-out/) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [Instant People Finder (Intelius)](https://instantpeoplefinder.com/) | [Link](https://www.intelius.com/opt-out/submit/) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [Intelius](https://www.intelius.com/) | [Link](https://www.intelius.com/opt-out/submit/) | ![freemium-service](icons/freemium-service.png)|
| [Melissa](https://www.melissa.com/v2/lookups/personatorsearch/) | [Link](https://www.melissa.com/privacy") | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [My Life](https://www.mylife.com/) | [CCPA](https://www.mylife.com/privacy-policy#caliResidentsNotice) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [Nuwber](https://nuwber.com/) | [Link](https://nuwber.com/removal/link) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [Open Gov US](https://opengovus.com/) | N/A | N/A |
| [PeekYou](https://www.peekyou.com/) | [Link](https://www.peekyou.com/about/contact/ccpa_optout/do_not_sell/) | ![freemium-service](icons/freemium-service.png)|
| [People Finder (Intelius)](https://www.peoplefinder.com/) | [Link](https://www.intelius.com/optout) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [People Finders](https://www.peoplefinders.com/) | [Link](https://www.peoplefinders.com/opt-out) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [People Search Now](https://www.peoplesearchnow.com/) | [Link](https://www.peoplesearchnow.com/opt-out) | N/A |
| [People Smart (Been Verified)](https://www.peoplesmart.com") | [Link](https://www.beenverified.com/app/optout/search) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [Pipl](https://pipl.com/) | [Link](https://pipl.com/personal-information-removal-request) | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png)|
| [Private Eye](https://www.privateeye.com/) | [Link](https://www.privateeye.com/static/view/optout/) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [Public Info Directory](https://publicrecords.directory/) | [Link](https://publicrecords.directory/contact.php) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [Public Records (Intelius)](https://publicrecords.com/) | [Link](https://www.intelius.com/opt-out/submit/) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [Radaris](https://radaris.com/) | E-Mail | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [Radio Reference](https://www.radioreference.com/apps/ham/) | N/A | N/A |
| [Spokeo](https://spokeo.com/) | [Link](https://www.spokeo.com/optout) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [That's Them](https://thatsthem.com/) | [Link](https://thatsthem.com/optout) | N/A |
| [True People Search](https://www.truepeoplesearch.com) | [Link](https://www.truepeoplesearch.com/removal) | N/A |
| [TruthFinder](https://www.truthfinder.com/) | [Link](https://www.truthfinder.com/opt-out/) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [USSearch](https://www.ussearch.com/) | [Link](https://www.ussearch.com/opt-out/submit/) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [Voter Records](https://voterrecords.com/) | [Link](https://voterrecords.com/contact) | N/A |
| [Webmii](https://webmii.com/) | N/A | N/A |
| [White Pages](https://www.whitepages.com/) | [CCPA](https://www.whitepages.com/privacy/ccpa) [Suppression Request](https://www.whitepages.com/suppression-requests) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [Yasni](http://www.yasni.com/) | datenschutz@yasni.de | N/A |
| [Zaba Search (Intelius)](https://www.zabasearch.com/) | [Link](https://www.intelius.com/opt-out/submit/) | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |

#### 🟣 Phone Numbers

| Organization/Tool | Description | Record Opt-Out/Removal | Directory |
| :------ | :----- | :----- | :----- |
| [Telephone Directories](https://Telephonedirectories.us) | Phone number directoy lookup | [Link](https://www.telephonedirectories.us/Edit_Records) | N/A |
| [Caller Smart](https://Callersmart.com) | Phone number directoy lookup | [Link](https://www.callersmart.com/opt-out) | ![register-profile](icons/register-profile.png) |
| [All Area Codes](https://Allareacodes.com/) | Phone number directoy lookup |  [Link](https://www.allareacodes.com/remove_name.htm) | N/A | 
| [People by Name](https://Peoplebyname.com/) | Phone number directoy lookup |  [Link](http://www.peoplebyname.com/remove.php) | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |
| [PhoneInfoga](https://Peoplebyname.com/) | Advanced information gathering & OSINT framework for phone numbers | N/A | ![opensource](icons/opensource.png) |


#### 🟣 Physical Address

| Organization | Record Opt-Out/Removal | Directory |
| :------ | :----- | :-----  |
| [Neighbor Who (Been Verified)](https://www.neighborwho.com) | [Link](https://www.neighborwho.com/app/optout/search) | ![paid-product](icons/paid-product.png) ![register-profile](icons/register-profile.png) |

#### 🟣 Social Media

| Tool | Description | Directory |
| :------ | :----- | :------ |
| [GeoSocial Footprint](http://geosocialfootprint.com/) | Provides twitter users with an opportunity to view their geosocial footprint. | N/A |
| [One Million Tweet Map](https://onemilliontweetmap.com/) | Displays last 24h geolocalized tweets delivered. Real Time. | N/A |
| [Sherlock](https://github.com/sherlock-project/sherlock) | Hunt down social media accounts by username. | ![opensource](icons/opensource.png) |
| [Social Analyzer](https://github.com/qeeqbox/social-analyzer) | API, CLI & Web App for analyzing & finding a person's profile across +800 social media. | ![opensource](icons/opensource.png) |
| [Social Searcher](https://www.social-searcher.com/) | Social Media Search Engine. | ![freemium-service](icons/freemium-service.png)![register-profile](icons/register-profile.png) |
| [Toutatis](https://github.com/megadose/toutatis) | a tool that allows you to extract information from instagrams accounts such as e-mails, phone numbers and more. | ![opensource](icons/opensource.png) |
| [WhatsMyName](https://github.com/webbreacher/whatsmyname) | Unified data required to perform user and username enumeration on various websites | ![opensource](icons/opensource.png) | 









### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Reverse Engineering

*Reverse engineering tools both offensive and defensive operations can utilize.*

#### 🟣 Mobile

| Tool | Descrption | Directory |
| :----- | :----- | :------- |
| [Quark](https://github.com/quark-engine/quark-engine) | Android Malware Analysis/Scoring System  | ![freemium-service](icons/freemium-service.png) |


#### 🟣 Tools

| Tool | Descrption | Directory |
| :----- | :----- | :------- |
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | Ghidra is a software reverse engineering (SRE) framework. | ![opensource](icons/opensource.png) |
| [IDA Pro](https://hex-rays.com/) | State of the art binary code analysis. | ![freemium-service](icons/freemium-service.png) |

#### 🟣 Videos

| Resource | Descrption | Directory |
| :----- | :----- | :------- |
| [Ghidra Class - HackadayU](https://www.youtube.com/watch?v=d4Pgi5XML8E) | This is Class 1 in Reverse Engineering with Ghidra taught by Matthew Alt. | N/A |

### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Write-Ups

*Write-ups both offensive and defensive operataions can utilize.*

#### 🟣 Documents

| Organization | Description | Directory |
| :------ | :------ | :-------- |
| [Cybercrime Campaign Collections](https://github.com/CyberMonitor/APT_CyberCriminal_Campagin_Collections) | APT & CyberCriminal Campaign Collection. | ![opensource](icons/opensource.png) |



***






## [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Xtras

*Some extra content. Infosec related of course.*









### [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Video

#### 🟢 Livestreamers

| Tool | Description | Directory |
| :------ | :----- | :------ |
| [HackListX](https://hacklistx.github.io/) | A list of Hacking Streamers. | ![opensource](icons/opensource.png) |
| [InfoSec Streamers](https://infosecstreams.github.io/) | InfoSec streamers list sorted based on 14-day activity to help you find active streamers more easily. | ![opensource](icons/opensource.png) |










## [🔝](https://github.com/InfosecHouse/InfosecHouse#contents) Thanks

*Shoutout to the following amazing individuals for suggesting and adding resources!*

[chadb_n00b](https://www.twitch.tv/chadb_n00b), [EightBitOni](https://www.twitch.tv/eightbitoni/), [footpics4sale](https://www.twitch.tv/footpics4sale), [theGwar](https://www.twitch.tv/thegwar).
