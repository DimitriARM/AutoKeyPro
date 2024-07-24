
class CreateAutomation:

    def __init__(self):
        self.automation_profiles = []
        self.label_counter = 1
    # TODO: make this guy save the automations in a file or something.
    def create_automation_profile(self):
        profile_name = input("Automation name : ")
        retProf = automation_profile(profile_name, self.label_counter)
        self.label_counter += 1
        self.automation_profiles.append(retProf)