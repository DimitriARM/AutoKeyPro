
# AutoKeyPro™ developed by ARM Industries.

# @author :  SpaghettiSalesman  on Github


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

    def display_profiles(self):
        for profile in self.macro_profiles:
            print(profile)

    def create_macro_profile(self,profile_name,label_counter):
        retProf = MacroProfile(profile_name,label_counter)
        self.label_counter += 1
        self.macro_profiles.append(retProf)

    def display_menu(self): #will be replaced by a gui later, or something like that
        if self.state == "first_boot" :
            print("Welcome to the menu")

            if(not self.macro_profiles):
                ret = input("You have no automation profiles as of yet, would you like to make one? [y,n]")
                if(ret.lower() == "yes" || ret.lower() == "y"):
                    profile_name = input("Automation name : ")
                    self.create_macro_profile(profile_name,self.label_counter)

        elif self.state == "default":
            pass

    def __main__(self):
        pass
