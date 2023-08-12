import os
def func():
	opt = int(input("Option: "))
	if opt == 1:
	    os.system("clear")
	    os.system("banner")
	    os.system("zsh")
	elif opt == 2:
	    os.system("clear")
	    os.system("banner")
	    os.system("nethunter")
	elif opt == 3:
	    os.system("clear")
	    os.system("banner")
	    os.system("nh kex")
	elif opt == 4:
	    os.system("clear")
	    os.system("banner")
	    os.system("su")
	elif opt == 5:
	    os.system("close")
	elif opt == 6:
	    os.system("clear")
	    os.system("banner")
	    print("Flashing module...")
	    os.system("su -c magisk --install-module /data/data/com.termux/files/home/custoMUX/zips/DisableFlagSecure.zip")
	    os.system("mainmenu")
	elif opt == 7:
	    os.system("clear")
	    os.system("banner")
	    os.system("su -c magisk --install-module /data/data/com.termux/files/home/custoMUX/zips/EnableFlagSecure.zip")
	    os.system("mainmenu")
	elif opt == 8:
	    os.system("clear)
	    os.system("banner")
	    os.system("su -c magisk --install-module /data/data/com.termux/files/home/custoMUX/zips/battery.zip")
	    os.system("mainmenu")
	elif opt == 9:
	    os.system("clear")
	    os.system("banner")
	    os.system("echo Desinstala el módulo desde magisk manager. Sleeping 10s... | lolcat")
	    os.system ("sleep 10")
	    os.system("mainmenu")
	elif opt == 10:
	    os.system("clear")
	    os.system("banner")
	    os.system("su -c magisk --install-module /data/data/com.termux/files/home/custoMUX/zips/AntiBootloop.zip")
	    os.system("mainmenu")
	else:
	    os.system("echo [!] Invalid option | lolcat")
	    func()
func()
