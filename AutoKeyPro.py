
# AutoKeyPro™ developed by ARM Industries.

import keyboard
import os
import time

# todo: add requirements.txt

# --------------------------------------------------------------------------------
# program wide variables (this may be a bad idea)

# changes how fast AutoKeyPro prints to the console
# time.sleep(printSpeed)
printSpeed = 0.6

# --------------------------------------------------------------------------------

def main():

    # program introduction
    print("")
    print("AutoKeyPro™ developed by ARM Industries.")
    print("")

    time.sleep(printSpeed)

    # Main menu
    while 1:

        print("Main Menu:")
        time.sleep(printSpeed)
        print("1 - Learning Mode")
        print("2 - Execution Mode")
        print("3 - Forget Mode")
        print("0 - Exit")
        time.sleep(printSpeed)

        choice = input("Choice: ")
        if choice == '1':
            learning_mode()
        elif choice == '2':
            execution_mode()
        elif choice == '3':
            forget_mode()
        elif choice == '0':
            print("Program terminating...")
            break
        else:
            print("Invalid option")

# --------------------------------------------------------------------------------

def learning_mode():

    # adding time sleeps so it prints nicer
    time.sleep(printSpeed)
    print("Learning Mode")
    time.sleep(printSpeed)

    # create directory to store automations if directory does not exist
    if os.path.exists("Automations"):
        print("Directory exists")
    else:
        os.mkdir("Automations")
        print("Directory created")

    time.sleep(printSpeed)

    print("Press ctrl to start")
    wait_for_start()

    ### create file for automation

    # ask for automation name
    print("What would you like to name this automation?")

    # get automation name
    automationName = input("")

    # validate automation name (check if not empty string

    # todo: implement windows file path naming exceptions
    while automationName == '':
        automationName = input("Invalid name: ")

    print("your automation name is: ", automationName)

    # count how many files are there
    list = os.listdir("Automations")
    numberFiles = len(list)

    # concatenate name with path
    automationLocation = "Automations\\" + automationName

    # create file
    try:
        file = open(automationLocation, "x")
    except:
        print("yo, file exists")




# --------------------------------------------------------------------------------

def execution_mode():
    print("Execution Mode")





# --------------------------------------------------------------------------------

def forget_mode():
    time.sleep(printSpeed)
    print("forgetting functions...")
    time.sleep(printSpeed)

    # exists to hold file names in directory
    directory = []

    print("Select an automation for deletion:")
    time.sleep(printSpeed)

    # prints files in directory
    i = 1
    for file in os.listdir("Automations"):
        directory.append(file)
        print(str(i) + " - " + file)
        i = i + 1

    time.sleep(printSpeed)
    choice = input("Choice: ")

    while choice == '':
        choice = input("Choice: ")

    if int(choice) > len(directory):
        print("out of bounds")
    else:
        filePath = "Automations\\" + str(directory[int(choice) - 1])
        os.remove(filePath)

    time.sleep(printSpeed)
    print("Automation forgotten!")
    time.sleep(printSpeed)


# --------------------------------------------------------------------------------

def wait_for_start():
    while True:
        if keyboard.read_key() == 'ctrl':
            print("Started!")
            break



# --------------------------------------------------------------------------------

main()

# --------------------------------------------------------------------------------
