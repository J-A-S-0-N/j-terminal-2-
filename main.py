# all import 
import psutil
from datetime import datetime
import platform
import os
from time import sleep
from os import system

# change the diractory to the main 
os.chdir("C:\\Users\\jason\\Desktop")

# get the current direcory for printing it
current_dir = os.getcwd()
# variable for sleeping sleep(2)
timeToSleep = 2

global current_dir_str
# this is the current dirctory its for changing dircory later it will append it and then chdir
current_dir_str = 'C:\\Users\\jason\\Desktop'

#function for changing diracotry
def chdir(dir):
    os.chdir(dir)

#function for deliting a folder *not file
def del_folder(foldername):
    os.remove(current_dir_str + "\\" + foldername)
    # print("it has been successfully deleted")
    # sleep(timeToSleep)

def del_file(filename):
    pass

#function for reading text file not yet docs or pdf 
def read_file(filename):
    while True:
        system("cls")
        file_to_read = open(filename, mode="r")

        contents = file_to_read.read()
        print(contents)

        print("enter 'yes' if you are done")
        read_file_inp = input("")
        if read_file_inp in ["yes", "yup", "y", "Y", "YES"]:
        #if read_file_inp == "yes" or read_file_inp == "Yes" or read_file_inp == "YES":
            file_to_read.close()
            break
        else:
            system("cls")
            print("please enter 'yes'")
            sleep(timeToSleep)

def change_dir_name(additional, current_dirarort = current_dir_str):
    current_dir = current_dir_str + "\\" + additional
    print(current_dir_str)
    # current_dir = current_dir_str
    return current_dir

# get the computer status
def comstatus():
    print("="*30, "System Information", "="*30)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

# print out the help which contains all the command
def tutorial():
    print("res = reset the terminal")
    print("cs = conputer status")
    print("help = print out the tutorial")
    print("echo:string = this will print the string")
    print("time = print out the current time")
    print("help = print out the tutorial")
    print("ls:ff = list the file/folder")
    print("ls:p = list all the path")
    print("cs = get the info about the computer")
    print("cls = clear the screen")
    print("ver = print out the version of you os")
    print("cpuinfo = print out the cpuinfo")
    print("cpuinfo:use")
    print("c:path = change dir")
    print("cr:path = reletive path")
    print("mkfil:name = make an file")
    print("mkfol:name  = make an folder")
    print("delfol:name = delete filder")
    print("delfil:name = delete file")
    print("rnfil:name:newname = rename the name to new name")
    print("rnfol:name:newname = rename the name to new name")

# this creates a file 
def create_file(filename):
    os.mkdir(filename)
    # print("the file has been successfully made")

# not used

# def start():
#     return 0
#     print("J terminal by Jason")
#     sleep(timeToSleep)
#     system("cls")
#     print("* read file can only be txt file")
#     sleep(timeToSleep + 4)
#     system("cls")

# not used

# this get all the available direcoty reletive to your path
def dir_list():
    # print("available directory")
    available_dir = os.listdir()
    for i in range(0,len(available_dir)):
        i_list = list(available_dir[i])
        if "." in i_list:
            i+=1
        else:
            print(available_dir[i])

# this prints current diractoy 
def current_directory():
    print(os.getcwd())

# main loop
def main():
    while True:
        '''
        res = reset the terminal
        cs = conputer status
        help = print out the tutorial
        ls:ff = list the file/folder
        ls = list all the path
        c:path = change dir
        cr:path = reletive path
        mkfil:name = make an file
        mkfol:name  = make an folder
        delfol:name = delete folder
        delfil:name = delete file
        rnfil:name:newname = rename the name to new name
        rnfol:name:newname = rename the name to new name
        echo:string = this i will print the string
        time = print out the current time
        '''
        system("cls")
        print("Jason terminal [Version 0.9 beta]")
        print("(c) 2020 Jason Corporation. All rights reserved.")
        print("\n")
        while True:
            inpSplitFirst = None
            inpSplitSeccond = None
            inpSplitThird = None
            current_dir = os.getcwd()
            inp = input(current_dir + ">")
            inpSplit = inp.split(":")
            inpSplitFirst = inpSplit[0]
            if len(inpSplit) == 3:
                inpSplitSeccond = inpSplit[1]
                inpSplitThird = inpSplit[2]
            elif len(inpSplit) == 2:
                inpSplitSeccond = inpSplit[1]
            if inpSplitFirst == "c" and inpSplitSeccond != None:
                current_dir_str = change_dir_name(inpSplitSeccond)
                print(current_dir_str)
                chdir(current_dir_str)
            elif inpSplitFirst == "mkfil" and inpSplitSeccond != None:
                pass
            elif inpSplitFirst == "mkfol" and inpSplitSeccond != None:
                create_file(inpSplitSeccond)
    
            elif inpSplitFirst == "delfol" and inpSplitSeccond != None:
                del_folder(inpSplitSeccond)
    





            elif inpSplitFirst == "delfil":
                pass
            elif inpSplitFirst == "rnfil":
                pass
            elif inpSplitFirst == "rnfol":
                pass
            elif inpSplitFirst == "help":
                tutorial()
            elif inpSplitFirst == "ls":
                if inpSplitSeccond == "ff":
                    pass
                elif inpSplitSeccond == None:
                    dir_list()
            elif inpSplitFirst == "cls":
                system("cls")
            elif inpSplitFirst == "help":
                tutorial()
            elif inpSplitFirst == "cs":
                comstatus()
            elif inpSplitFirst == "echo":
                print(inpSplitSeccond)
            elif inpSplitFirst == "time":
                currentTime = str(datetime.now())
                print("current time is \"" + currentTime + "\"")
            elif inpSplitFirst == "ver":
                print(platform.system() + " " +platform.release())
            elif inpSplitFirst == "cpuinfo":
                if inpSplitSeccond == "use":
                    print("cup useage : " + str(psutil.cpu_percent()))
                    print("physical memory useage : " + str(psutil.virtual_memory()))
                elif inpSplitSeccond == None:
                    pass
            elif inpSplitFirst == "quit":
                system("cls")
                print("are you sure?")
                quitinp = input("> ")
                if quitinp in ["y", "yes", "Yes"]:
                    quit()
                else:
                    pass
            elif inpSplitFirst == "res":
                system("cls")
                print("reseting")
                print("[::              ]")
                sleep(1.5)
                system("cls")
                print("reseting")
                print("[::::::          ]")
                sleep(1.3)
                system("cls")
                print("reseting")
                print("[::::::::::      ]")
                sleep(1.3)
                system("cls")
                print("reseting")
                print("[::::::::::::::  ]")
                sleep(1)
                system("cls")
                print("reseting")
                print("[::::::::::::::::]")
                sleep(0.4)
                break
            else:
                print("\"" + inp + "\" is not recognized as a command")
            print("\n")
        

if __name__ == "__main__":
    main()