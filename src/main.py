import src.core
import src.interface
import src.db as db
import signal, threading, getpass, time
import script 


class Main():
    def __init__(self):
        pass
    
    def run(self):
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        if db.User(username=getpass.getuser()).get_plan_by_username()[0] == "free":
            while True:
                src.interface.ASCII().blocked()
                time.sleep(1)
                src.interface.ASCII().cls()
        else:
            src.interface.ASCII().home()
            while True:
                src.core.Commande.Commande()
            
    

