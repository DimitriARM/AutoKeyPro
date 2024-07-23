# AutoKeyPro™ developed by ARM Industries.

# @author :  SpaghettiSalesman & Dimitri ARM on GitHub


# DEPRECATED: One file implementation, this wont be pretty to look at, but whatever.

# We will be changing this implementation for multi-file one, but whatever.

# leaving this here for our reference
"""
module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME,
CLASS_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name.
"""

import AutomationProfile
import AutomationCommand
from AutoKeyPro import *


def main():
    main_program = AutoKeyPro()

    while 1:
        main_program.display_menu()


# I realized we need these lines for program to run
if __name__ == '__main__':
    main()
