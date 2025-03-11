from modules.tutorial import Tutorial

class LStudio: 
    def __init__(self): 
        print(f'\n***** \tL-Studio v2.0.0\t *****\n')
        self.menu()

    def validate(self, valid): 
        while True: 
            user = input(f'\nEnter choice {[i for i in valid]}: ')
            if user in valid: 
                return user
            else: 
                print('\nInvalid.', end=' ')
            
    def menu(self):

        print('\t1. Tutorial')
        print('\t2. Examples')
        print('\t3. Custom')
        print('\t3. Plot Settings')

        user = self.validate(['1', '2', '3', '4'])

        match user: 
            case '1': 
                print(Tutorial())

if __name__ == '__main__':
    LStudio()
        
