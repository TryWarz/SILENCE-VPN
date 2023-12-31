import src.core
import src.interface
import signal, threading
import script



class Main():
    def __init__(self):
        pass
    
    def run(self):
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        src.interface.ASCII().home()
        while True:
            src.core.Commande.Commande()
            
    

