class LStudio: 
    def __init__(self): 
        self.menu()

    def validate(self, valid): 
        while True: 
            user = input(f'\nEnter choice {[i for i in valid]}: ')
            if user in valid: 
                return user
            else: 
                print('\nInvalid.', end=' ')
            
    def menu(self):
        print(f'\n ***** \tL-Studio v2.0.0\t ***** \n')

        print('\t1. Tutorial')
        print('\t2. Examples')
        print('\t3. Custom')
        print('\t3. Plot Settings')

        user = self.validate(['1', '2', '3', '4'])

        
