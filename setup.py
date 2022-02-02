#!/usr/bin/env python 


from __future__ import print_function
import subprocess
import os 
from time import sleep


print("[*] Figlet Indiriliyor %")
subprocess.Popen("apt-get install figlet", shell=True).wait()
sleep(2)
print("[*] Lolcat Indiriliyor %")
subprocess.Popen("apt-get install lolcat", shell=True).wait()
sleep(2)
print("[*] Nmap Indiriliyor %")
subprocess.Popen("apt-get install nmap", shell=True).wait()
sleep(2)
print("[*] Gobuster Indiriliyor %")
subprocess.Popen("apt-get install gobuster", shell=True).wait()
sleep(2)
print("[*] Nikto Indiriliyor %")
subprocess.Popen("apt-get install nikto", shell=True).wait()
sleep(2)
print("[*] Sqlmap Indiriliyor %")
subprocess.Popen("apt-get install sqlmap", shell=True).wait()
sleep(2)
print("[*] John Indiriliyor %")
subprocess.Popen("apt-get install john", shell=True).wait()
sleep(2)
print("[*] Wpscan Indiriliyor %")
subprocess.Popen("apt-get install wpscan", shell=True).wait()
sleep(2)
print("[*] Msfvenom Indiriliyor %")
subprocess.Popen("apt-get install msfvenom", shell=True).wait()
sleep(2)
print("[*] Hydra Indiriliyor %")
subprocess.Popen("apt-get install hydra", shell=True).wait()
sleep(2)
print("[*] samba Indiriliyor %")
subprocess.Popen("apt-get install samba", shell=True).wait()
sleep(2)
print("[*] smbclient Indiriliyor %")
subprocess.Popen("apt-get install smbclient", shell=True).wait()
sleep(2)

print("[*] Figlet Gerekli Ayarlar Yapiliyor %")
sleep(2)
print("[*] Lolcat Gerekli Ayarlar Yapiliyor %")
sleep(2)
print("[*] Nmap Gerekli Ayarlar Yapiliyor %")
sleep(2)
print("[*] Gobuster Gerekli Ayarlar Yapiliyor %")
sleep(2)
print("[*] Nikto Gerekli Ayarlar Yapiliyor %")
sleep(2)
print("[*] Sqlmap Gerekli Ayarlar Yapiliyor %")
sleep(2)
print("[*] John Gerekli Ayarlar Yapiliyor %")
sleep(2)
print("[*] Wpscan Gerekli Ayarlar Yapiliyor %")
sleep(2)
print("[*] Msfvenom Gerekli Ayarlar Yapiliyor %")
sleep(2)
print("[*] Hydra Gerekli Ayarlar Yapiliyor %")
sleep(2)
print("[*] Samba Gerekli Ayarlar Yapiliyor %")
sleep(2)
print("[*] Smbclient Gerekli Ayarlar Yapiliyor %")
sleep(3)
print("[*] FrSec Bug Bounty Hunting")
os.system("clear")
subprocess.Popen("python3 frsec.py", shell=True).wait()























