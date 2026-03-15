import time
from authentication import Authentication
from logger import log

# Main Boot menu
class Main:

    def boot(self):
        
        log ("Discrod started.")
        
        print("\n---------------")
        print("  DISCORD v1")
        print("---------------")
        time.sleep(0.8)
        print("Starting...")
        time.sleep(1)
        print("Loading...")
        time.sleep(0.9)
        print("Started") 
    
    #   check before discord start
    def security(self):

        #   first boot discord 
        self.boot()
        
        # run login discord
        auth = Authentication()
        auth.logic()

m = Main() 

if __name__ == "__main__":       # to privent unknow runs
    m.security()