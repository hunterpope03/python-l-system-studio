def validate(valid): 
    while True: 
        user = input(f'\nEnter choice {[i for i in valid]}: ')
        if user in valid: 
            return user
        else: 
            print('\nInvalid.', end=' ')