import sys

sys.dont_write_bytecode = True

from modules.validation import validate
from modules.tutorial import tutorial
from modules.example import Example
# from modules.custom import Custom
# from modules.plot import Plot


class LStudio: 
    def __init__(self): 
        pass
    
    def menu(self):

        print('\t1. Tutorial')
        print('\t2. Example Systems')
        print('\t3. Custom System')
        print('\t4. Plot Settings')
        print('\t5. Quit')

        user = validate(['1', '2', '3', '4', '5'])

        return user

def main(): 

    print('\n\n' + '***** L-Studio v2.0.0 *****' + '\n')

    while True: 
        app = LStudio()
        user = app.menu()

        match user: 
            case '1': 
                tutorial()
            case '2':
                ex = Example()
                user = ex.menu()
                details = ex.get_details(user)
                ex.print_details(details)
        #     case '3':
        #     case '4':
            case '5': 
                break
        
if __name__ == '__main__':
    main()
        
