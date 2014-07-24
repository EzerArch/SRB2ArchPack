# (c) EZER'ARCH - Python script
# ArchPack Mini Launcher!

# Message
print ("\nThis is a Python application.")
print ("Created by Ezer'Arch (ezerarch.com and youtube.com/EzerArch)")
print ("Date 2014/03/24")


#### LIBS
from subprocess import call
import webbrowser
import os.path


#### ARGUMENTS
exe = "srb2win"
fil = "-file"
wad = "scmrtf_archpack.wad"
ogl = "-opengl"
con = "-console"
win = "-win"
lstArgs = None # creates empty variable
file = None  # creates empty variable
# os.getcwd() # current directory


### EXECUTION

# Message
print("\n**** ArchPack Mini Launcher ****")
print("\n::idea:: Try startSRB2. The best SRB2 Launcher in town!")
input( "\nHit ENTER to proceed... ")


# Options
option = input('''\nSelect an option to start up SRB2 with ArchPack:
1 = Software Fullscreen
2 = Software Windowed
3 = OpenGL Fullscreen 
4 = OpenGL Windowed
5 = ... or open ArchPack README for what's new!
ENTER = Exit
Enter the number for the option: ''')

if option == '1':
    lstArgs = [exe] + [fil] + [wad] + [con]

elif option == '2':
    lstArgs = [exe] + [fil] + [wad] + [win] + [con]

elif option == '3':
    lstArgs = [exe] + [fil] + [wad] + [ogl] + [con]

elif option == '4':
    lstArgs = [exe] + [fil] + [wad] + [ogl] + [win] + [con]

elif option == '5':
    file = "ArchPack v2.1 readme.txt"
    
else:
    print("Nothing was done.")
    input("\nHit ENTER to close... ")

# Launch
if lstArgs is not None:
    print('Launching: ' + (' '.join(lstArgs)) + '...')
    print("Wait a sec... >>>")
    call(lstArgs)

# Open file
if file is not None:
    if os.path.isfile(file):
        print("Opening: ArchPack readme.")
        print("Wait a sec, it may take a while... >>>")
        webbrowser.open(file)
        print("Done.")
    else:
        print("ArchPack readme not found!")
        input("\nHit ENTER to close... ")

#EOF

