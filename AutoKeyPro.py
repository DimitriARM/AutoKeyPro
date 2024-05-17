# AutoKeyPro™ developed by ARM Industries.

# @author :  SpaghettiSalesman on Github

class AUTOKEYPRO():
    def __init__(self):
        self.state = "first_boot"
        self.macro_profiles = []
        self.label_counter = 1
        self.active_profile = MacroProfile("", 0)

    def display_profiles(self):
        for macro_profile in self.macro_profiles: #some variables feel too verbose. Might cut down later.
            print(macro_profile.label, macro_profile.profile_name)

    #TODO: make this guy save the macros in a file or something.
    def create_macro_profile(self):
        profile_name = input("Automation name : ")
        retProf = MacroProfile(profile_name, self.label_counter)
        self.label_counter += 1
        self.macro_profiles.append(retProf)

    #TODO: make the guy below do more stuff.
    def display_menu(self):  #will be replaced by a gui later, or something like that
        if self.state == "first_boot":
            print("Welcome to the menu")

            if (not self.macro_profiles):
                ret = input("You have no automation profiles as of yet, would you like to make one? [y,n]\n")
                if ret.lower() == "yes" or ret.lower() == "y":
                    self.create_macro_profile()
                    self.state = "default"

        elif self.state == "default":

            print("1. SELECT PROFILE")
            print("2. EDIT PROFILE") #unimplemented, oops
            print("3. CREATE PROFILE")
            print("4. EXIT")

            ret = input()

            if ret == "1":
                print("PROFILE SELECTION: \n ")
                self.display_profiles()
                int_ret = int(input())
                self.active_profile = self.macro_profiles[int_ret-1]


            elif ret == 2:
                self.create_macro_profile()

            else:
                exit()


def __main__():
    main_program = AUTOKEYPRO()

    while 1:
        main_program.display_menu()


__main__()
