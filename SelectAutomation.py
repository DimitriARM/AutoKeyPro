class SelectAutomation:

    def __init__(self):
        self.automation_profiles = [1, 2, 3]
        self.label_counter = 1

    # check if automations folder exists
    # if not, ask user if they would like to create a new one
    # else, display automations

    def display_profiles(self):
        print('profiles about to be shown')
        for profile in self.automation_profiles:
            print(profile)
        print('profiles showed')