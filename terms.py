#Terms & Conditions >>
import os
import sys
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

HEADER    = '\033[95m'
OKBLUE    = '\033[94m'
OKGREEN   = '\033[92m'
WARNING   = '\033[93m'
FAIL      = '\033[91m'
END	      = '\033[0m'
BOLD      = '\033[1m'
UNDERLINE = '\033[4m'
#====================
Cyan       ="\033[0;36m"
Cafe       ="\033[0;33m"
xxx		   ="\033[0;35m"
blue       ="\033[1;34m"
trans      ="\e[0m"
BOLDxxx    = "\033[0;35m"+"\033[1m"
purple     ="\033[0;35m"

print"""
{0}this tool can spy on the devices in the local network devices with many options that
can make sniffing on the local network so easy to make it done
this tool take weeks to make it more easier and flexible for all users so we will be thankful
if you can rate our tool on github here :
	https://github.com/DevoOverkill9/the-watcher
Now there is some terms and conditions that maybe helpful and should read:
{1}
[1]you can make some edits on this script but you can make us know first we will be 
   thanked if u do this :D

[2]if you found that you can't use this tool you can see our official vedio tutorial on youtube

[3]we are not responsible for any bad using of this tool
  cause this tool has been made for pentesters and educational purposes only.

[4]if you have faced any kind of problems while using our tool you can inform us to our E_mail : 
	devoohk2016@gmail.com
[5]last thing thanks for reading this and have a nice day :D
""".format(BLUE , OKGREEN)

print("\n{0}>{1}Do you accept these terms & conditions? {2}({3}y{4}/{5}n{2}) {0}:").format(WHITE , WARNING , WHITE , GREEN , WHITE ,WARNING)

try:
	print ("{}").format(BLUE)
	terms = raw_input("\nThe WATCHER > ")
	if terms == "y":
		print("{0}[{1}+{0}]{2}Terms & Conditions has been accepted!").format(WHITE , OKGREEN , BLUE)
	elif terms == "n":
		print("{0}[{1}x{0}]{2}Sorry you can't continue if you don't accept our terms!").format(WHITE , RED , RED)
		os.system(exit)
	else:
		print ("\n{}[x]Wrong Entry").format(RED)
		os.system (exit)

except KeyboardInterrupt:
	print ("""\n{0}[{1}x{0}]{2}Program has been ended
Thanks for stopping by!
		""").format(WHITE , RED , RED)
	os.system(exit)