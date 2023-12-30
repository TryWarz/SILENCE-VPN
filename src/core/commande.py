import src.interface as interface 
import src.db as db

from src.core.download import Zip
import getpass

class Commande:
    def __init__(self):
        pass

    def Commande():
        Commande = input(f"")
    
        match Commande:
            case "help":
                interface.ASCII().home()

            case "plans":
                pass

            case "download":
                if db.User(plan=db.User(username=getpass.getuser()).get_plan_by_username).get_plans_by_name() == "free":
                    raise ValueError("You are not allowed to use this command.")
                else:
                    Zip().send(user=getpass.getuser(), url=input("URL WEBHOOK: "))
