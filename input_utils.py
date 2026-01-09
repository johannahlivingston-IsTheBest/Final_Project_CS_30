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

    The keymap argument is used to specify which keys correspond to which
    options. This function has a few defaults, like 'numeric' and 'wasd'.

    Ex.
    menu("Pick one: ", ["Option1", "Option2", "Option3", "Option4"],
                        keymap="wasd")
    This creates a menu where typing 'w' corresponds to Option1 and so on.

    You may also pass a custom keymap dictionary with this format:
    keymap = {"0": "key1", "1": "key2", ... , "9": "key9"}

    Parameters:
        text (str): menu text to show to user
        actions (dict_keys): things the user can do
        keymap (bool): use keys to pick other than 1234...

    Returns:
        str: the user's choice
    """
    ordered_actions = list(actions)  # Convert to list in case dict keys
    # Set keymap. Auto-set if custom keymap dict is passed
    if keymap == "numeric":
        keymap = {"0": "1", "1": "2", "2": "3", "3": "4", "4": "5", "5": "6", "6": "7", "7": "8", "8": "9"}
    elif keymap == "wasd":
        keymap = {"0": "w", "1": "a", "2": "s", "3": "d"}
    keymap_reverse = {value: key for key, value in keymap.items()}
    # Input loop
    while True:
        print("\n" + text)
        for index, action in enumerate(ordered_actions):  # List options
            print(f"[{keymap[str(index)]}]  {action}")
        choice = input("\nChoice: ")
        try:  # Validate input
            choice_num = int(keymap_reverse[choice])
            return ordered_actions[choice_num]
        except KeyError:
            print("\n--- INVALID INPUT ---\nTry again!")
        except IndexError:
            print("\n--- INVALID INPUT ---\nTry again!")


def force_input_dtype(msg, dtype):
    """Return valid user input.
    
    Parameters:
        msg (str): prompt to user
        dtype (str): required input data type
    
    Returns:
        (dtype): input of required data type
    """
    dtypes = {"int": int, "float": float, "str": str, "bool": bool}
    while True:
        user_input = input(f"\n{msg}")
        if dtype == "bool":  # Handle booleans with "yes"/"no"
            if user_input.lower() == "yes":
                return True
            elif user_input.lower() == "no":
                return False
            else:
                print("\n--- INVALID INPUT ---\nType 'yes' or 'no'!")
        else:
            try:
                return dtypes[dtype](user_input)
            except ValueError:
                print(f"\n--- INVALID INPUT ---\nEnter an input of type ({dtype})!")


if __name__ == "__main__":
    print(menu("PICK:", ["Option1", "Option2", "Option3", "Option4"], keymap="numeric"))
