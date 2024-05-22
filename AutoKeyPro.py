
# AutoKeyPro™ developed by ARM Industries.

# @author :  SpaghettiSalesman & Dimitri ARM on GitHub


# DEPRECATED: One file implementation, this wont be pretty to look at, but whatever.

# We will be changing this implementation for multi-file one, but whatever.

# leaving this here for our reference
'''module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME,
CLASS_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name.'''


class AutomationCommand:
    def __init__(self, input_combination, output_action, automation_label):
        self.input_combination = input_combination
        self.output_action = output_action
        self.automation_label = automation_label

class AutomationProfile:
    def __init__(self, profile_name, automation_profile_label):
        self.profile_name = profile_name
        self.automation_profile_label = automation_profile_label
        self.automation_commands = {}

    def create_automation(self):
        pass
        #TODO: Get user inputs in a working manner

    def edit_automation(self, automation_label):
        pass
        #TODO: Add the editing functionality.

    def delete_automation(self, automation_label):
        pass
        #TODO: Implement later, also dont forget to de-increment the labels by one.

    def view_commands(self):
        for automation_label in range(1, len(self.automation_commands)):
            print(self.automation_commands[automation_label] + 1)


class AUTOKEYPRO:

    def __init__(self):
        self.state = "first_boot"
        self.automation_profiles = []
        self.label_counter = 1
        # self.active_profile (python told me to comment this line for now)

    def display_profiles(self):
        for profile in self.automation_profiles:
            print(profile)

    #TODO: make this guy save the automations in a file or something.
    def create_automation_profile(self):
        profile_name = input("Automation name : ")
        retProf = automation_profile(profile_name, self.label_counter)
        self.label_counter += 1
        self.automation_profiles.append(retProf)

    #TODO: make the guy below do more stuff.
    def display_menu(self):  #will be replaced by a gui later, or something like that
        if self.state == "first_boot":
            print("Welcome to the menu")

            if (not self.automation_profiles):
                ret = input("You have no automations saved as of yet, would you like to make one? [y,n]")
                if ret.lower() == "yes" or ret.lower() == "y":
                    self.create_automation_profile()

        elif self.state == "default":

            print("1. SELECT PROFILE")
            print("2. CREATE PROFILE")
            print("3. EXIT")

            ret = input()

            if ret == "1":
                print("PROFILE SELECTION: \n ")
                self.display_profiles()
                int_ret = int(input())
                self.active_profile = self.automation_profiles[int_ret]


            elif ret == 2:
                self.create_automation_profile()

            else:
                exit()

    def __main__(self):

        main_program = AUTOKEYPRO()

        while 1:
            main_program.display_menu()
