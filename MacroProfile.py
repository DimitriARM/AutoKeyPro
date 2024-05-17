class MacroProfile():
    def __init__(self, profile_name, label):
        self.profile_name = profile_name
        self.label = label
        self.macro_commands = {}

    def create_macro(self):
        pass
        #TODO: Get user inputs in a working manner

    def edit_macro(self, macro_label):
        pass
        #TODO: Add the editing functionality.

    def delete_macro(self, macro_label):
        pass
        #TODO: Implement later, also dont forget to de-increment the labels by one.

    def view_commands(self):
        for macro_label in range(1, len(self.macro_commands)):
            print(self.macro_commands[macro_label] + 1)
