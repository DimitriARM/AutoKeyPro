
# AutoKeyPro™ developed by ARM Industries.

# @author :  SpaghettiSalesman on Github


#One file implementation, this wont be pretty to look at, but whatever.


class MacroCommand():
    def __init__(self,input_combination,output_action, macro_label):
        self.input_combination = input_combination
        self.output_action = output_action
        self.macro_label = macro_label



class MacroProfile():
    def __init__(self,profile_name,macro_profile_label):
        self.profile_name = profile_name
        self.macro_profile_label = macro_profile_label
        self.macro_commands = {}

    def create_macro(self):
        pass
        #TODO: Get user inputs in a working manner

    def edit_macro(self,macro_label):
        pass
        #TODO: Add the editing functionality.

    def delete_macro(self, macro_label):
        pass
        #TODO: Implement later, also dont forget to de-increment the labels by one.

    def view_commands(self):
        for macro_label in range(1,len(self.macro_commands)):
            print(self.macro_commands[macro_label]+1)




class AUTOKEYPRO():

    def __init__(self):
        self.state = "first_boot"
        self.macro_profiles = []
        self.label_counter = 1
        self.active_profile

    def display_profiles(self):
        for profile in self.macro_profiles:
            print(profile)


#TODO: make this guy save the macros in a file or something.
    def create_macro_profile(self):
        profile_name = input("Automation name : ")
        retProf = MacroProfile(profile_name,self.label_counter)
        self.label_counter += 1
        self.macro_profiles.append(retProf)



#TODO: make the guy below do more stuff.
    def display_menu(self): #will be replaced by a gui later, or something like that
        if self.state == "first_boot" :
            print("Welcome to the menu")

            if(not self.macro_profiles):
                ret = input("You have no automation profiles as of yet, would you like to make one? [y,n]")
                if ret.lower() == "yes" or ret.lower() == "y" :
                    self.create_macro_profile()

        elif self.state == "default":

            print("1. SELECT PROFILE")
            print("2. CREATE PROFILE")
            print("3. EXIT")

            ret = input()

            if ret == "1":
                print("PROFILE SELECTION: \n ")
                self.display_profiles()
                int_ret = int(input())
                self.active_profile = self.macro_profiles[int_ret]


            elif ret == 2:
                self.create_macro_profile()

            else:
                exit()





    def __main__(self):

        main_program = AUTOKEYPRO()

        while 1 :
            main_program.display_menu()

