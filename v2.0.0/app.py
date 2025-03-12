from modules.validate import validate
from modules.tutorial import tutorial
from modules.examples import Examples

class LStudio: 
    def __init__(self): 
        print('\n\n' + '***** L-Studio v2.0.0 *****' + '\n')
        self.menu()
            
    def proceed(self):
        print('\n\nContinue by selecting another menu option:' + '\n\n')
        self.menu()
    
    def menu(self):

        print('\t1. Tutorial')
        print('\t2. Example Systems')
        print('\t3. Custom System')
        print('\t3. Plot Settings')

        user = validate(['1', '2', '3', '4'])

        match user: 
            case '1': 
                tutorial()
                self.proceed()
            # case '2':
        #     case '3':
        #     case '4':

if __name__ == '__main__':
    LStudio()
        
