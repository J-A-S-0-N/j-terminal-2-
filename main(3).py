'''
todo:

list all the direcoty [O]
make it able to change the dir just by entering the next one [O]
show all text file in read file option []
show all folder in the make an folder option to make sure there isnt an duplicate []

due today
change make an file to make an folder []
say error if there is an dulplicate from make an file, delete file, read file []
dont show error if there is for  []

'''

# all import 
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
current_dir_str = "C:\\User\\jason\\Desktop"

#function for changing diracotry
def chdir(dir):
    os.chdir(dir)
    print("the path had been successfully changed")
    sleep(timeToSleep)

#function for deliting a folder *not file
def del_file(filename):
    os.remove(current_dir + "\\" + filename)
    print("it has been successfully deleted")
    sleep(timeToSleep)

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

def tutorial():
    print("""
    1 createing file
    before creating file you need to change the diratory(place)
    by pressing c and pasting the location and you can only
    create text file

    2 reading file
    this will only work if the file is text file
    """)
    sleep(20)


def create_file(filename):
    os.mkdir(filename)
    print("the file has been successfully made")

def start():
    return 0
    print("J terminal by Jason")
    sleep(timeToSleep)
    system("cls")
    print("* read file can only be txt file")
    sleep(timeToSleep + 4)
    system("cls")

def dir_list():
    print("available directory")
    available_dir = os.listdir()
    for i in range(0,len(available_dir)):
        i_list = list(available_dir[i])
        if "." in i_list:
            i+=1
        else:
            print(available_dir[i])


def main():
    system("cls")
    start()
    while True:
        system("cls")
        print("current directror : ", os.getcwd())
        print(" ")
        print("change dir[c]")
        print("make an file[m]")
        print("delete file[d]")
        print("read file[r]")
        print("tutorial[t]")
        print("")
        # print("* read file can only be txt file")
        inp = input(">> ")
        if inp == "c" or inp == "C":
            system("cls")
            dir_list()
            print("current directory : ",os.getcwd())
            print("enter the directory")
            change_dir_input = input(">> ")
            change_dir_name(change_dir_input, )
            chdir(change_dir_input)

        elif inp == "m" or inp == "M":
            system("cls")
            print("enter the folder name")
            file_name_input = input(">> ")
            create_file(file_name_input)

        elif inp == "t" or inp == "T":
            system("cls")
            print(tutorial())

        elif inp == "d" or inp == "D":
            while True:
                system("cls")
                print("folder or file")
                inp = input(">> ")
                if inp in ["folder", "FOLDER", "Folder"]:
                    print("enter the folder name")
                    del_file_input = input(">> ")
                    del_file(del_file_input)
                elif inp in ["file", "FOLDER", "Folder"]:
                    pass
                else:
                    system("cls")
                    print("please enter either \"folder\" or \"file\"")
                    sleep(timeToSleep)

        elif inp == "r" or inp == "R":
            print("enter the text file")
            read_file_inp = input(">> ")
            read_file(read_file_inp)

        else:
            system("cls")
            print("please enter an valid choice")
            sleep(5)
            system("cls")



if __name__ == "__main__":
    main()
