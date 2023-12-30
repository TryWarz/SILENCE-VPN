import signal
signal.signal(signal.SIGINT, signal.SIG_IGN)

# Import Packages
import src.db
import src.config
import src.interface
import src.core

class Main:
    def __init__(self):
        pass

    def run(self):
        src.core.Commande().Commande()