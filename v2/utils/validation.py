def validate_menu(valid_inputs):
    """
    Prompts the user to enter a choice and validates it against a given list of valid inputs.

    Parameters:
    valid_inputs (list): A list of acceptable input values.

    Returns:
    str: The validated user input.
    """
    while True:
        try:
            user = input(f'\nEnter choice {[value for value in valid_inputs]}: ').strip()
            if user in valid_inputs: # check if user input is in the list of valid inputs.
                return user
            else: # if not, repeat the loop.
                print('\nInvalid.', end=' ')
        except Exception as e: # for any other errors, print the error message and prompt the user to try again.
            print(f'\nAn error occurred: {e}. Please try again.', end=' ')