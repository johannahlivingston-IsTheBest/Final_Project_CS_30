##############################################################################
# Title: input_utils
# Date: 1/8/2026
##############################################################################
"""Module of utility functions to manage user input."""
##############################################################################
# Imports and Global Variables -----------------------------------------------

# Functions and Classes ------------------------------------------------------
def menu(text, actions, keymap="numeric"):
    """Show a general-purpose menu and let the user pick an option.

    Parameters:
        text (str): menu text to show to user
        actions (dict_keys): things the user can do
        keymap (bool): use something to pick other than 1234...

    Returns:
        str: the user's choice
    """
    ordered_actions = list(actions)  # Convert to list
    if keymap == "numeric":
        keymap = {"0": "1", "1": "2", "2": "3", "3": "4", "4": "5", "5": "6", "6": "7", "7": "8", "8": "9"}
    elif keymap == "wasd":
        keymap = {"0": "w", "1": "a", "2": "s", "3": "d"}
    keymap_reverse = {value: key for key, value in keymap.items()}
    # print(ordered_actions)
    # ordered_actions.extend([glob_act for glob_act in global_actions])
    # ordered_actions.remove("Back") if not include_back else ordered_actions
    while True:
        print("\n" + text)
        for index, action in enumerate(ordered_actions):
            print(f"[{keymap[str(index)]}]  {action}")
        choice_num = force_input_dtype("Choice: ", "int")
        if 1 <= choice_num <= len(ordered_actions):
            return ordered_actions[keymap_reverse[choice_num]]
        else:
            print("Not a valid option!")


def force_input_dtype(msg, dtype):
    """Return valid user input."""
    dtypes = {"int": int, "float": float, "str": str, "bool": bool}
    while True:
        user_input = input(f"\n{msg}")
        if dtype == "bool":
            if user_input.lower() == "yes":
                return True
            elif user_input.lower() == "no":
                return False
            else:
                print('Invalid. Type "yes" or "no"')
        else:
            try:
                return dtypes[dtype](user_input)
            except ValueError:
                print(f"\nINVALID: Please ensure your input is of type ({dtype})")

if __name__ == "__main__":
    print(menu("PICK:", ["Option1", "Option2", "Option3", "Option4"], keymap="wasd"))
