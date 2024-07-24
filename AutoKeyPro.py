from SelectAutomation import SelectAutomation
from AutomationProfile import *
from CreateAutomation import *


class AutoKeyPro:

    def __init__(self):
        self.state = "default"
        self.active_profile = []

    # TODO: make the guy below do more stuff.
    def display_menu(self):  # will be replaced by a gui later, or something like that

        if self.state == "first_boot":  # this line is not working, welcome to menu reprints
            print("Welcome to the menu")

            '''
            This entire block should go to 1. Select Automations
            
            Program should check for a folder named "Automations"
            if exists: print main menu
            if does not exist: print line below
            '''
            if not SelectAutomation.automation_profiles:
                ret = input("You have no automations saved as of yet, would you like to make one? [y,n]")
                if ret.lower() == "yes" or ret.lower() == "y":
                    CreateAutomation.create_automation_profile()
                else:
                    exit(0)

        elif self.state == "default":
            print('Please make a selection.')

            print("1. SELECT AUTOMATION")
            print("2. CREATE AUTOMATION")
            print("3. EXIT")

            print('Selection:')
            ret = input()

            if ret == "1":
                print("PROFILE SELECTION: \n ")
                selector = SelectAutomation()  # Create instance
                selector.display_profiles()
                int_ret = int(input())
                # self.active_profile = CreateAutomation.automation_profiles[int_ret]


            elif ret == 2:
                CreateAutomation.create_automation_profile()

            else:
                exit()
