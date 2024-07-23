class AutomationProfile:
    def __init__(self, profile_name, automation_profile_label):
        self.profile_name = profile_name
        self.automation_profile_label = automation_profile_label
        self.automation_commands = {}

    def create_automation(self):
        pass
        # TODO: Get user inputs in a working manner

    def edit_automation(self, automation_label):
        pass
        # TODO: Add the editing functionality.

    def delete_automation(self, automation_label):
        pass
        # TODO: Implement later, also dont forget to de-increment the labels by one.

    def view_commands(self):
        for automation_label in range(1, len(self.automation_commands)):
            print(self.automation_commands[automation_label] + 1)