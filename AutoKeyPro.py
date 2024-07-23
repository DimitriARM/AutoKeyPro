class AutoKeyPro:

    def __init__(self):
        self.state = "first_boot"
        self.automation_profiles = []
        self.label_counter = 1
        # self.active_profile (python told me to comment this line for now)

    def display_profiles(self):
        for profile in self.automation_profiles:
            print(profile)

    # TODO: make this guy save the automations in a file or something.
    def create_automation_profile(self):
        profile_name = input("Automation name : ")
        retProf = automation_profile(profile_name, self.label_counter)
        self.label_counter += 1
        self.automation_profiles.append(retProf)

    # TODO: make the guy below do more stuff.
    def display_menu(self):  # will be replaced by a gui later, or something like that

        if self.state == "first_boot":  # this line is not working, welcome to menu reprints
            print("Welcome to the menu")

            if not self.automation_profiles:
                ret = input("You have no automations saved as of yet, would you like to make one? [y,n]")
                if ret.lower() == "yes" or ret.lower() == "y":
                    self.create_automation_profile()
                else:
                    exit(0)

        elif self.state == "default":

            print("1. SELECT AUTOMATION")
            print("2. CREATE AUTOMATION")
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
