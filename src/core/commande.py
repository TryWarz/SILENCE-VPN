import src.interface as interface 
import src.db as db
import script
from src.core.download import Zip
import getpass

class Commande:
    def __init__(self):
        pass

    def Commande():
        try:
            Commande = input(f"")
        
            match Commande:
                case "help":
                    interface.ASCII().home()

                case "plans":
                    pass
                
                case "download":
                    if db.User(username=getpass.getuser()).get_plan_by_username()[0] == "free":
                        raise ValueError("You are not allowed to use this command.")
                    else:
                        Zip().send(user=getpass.getuser(), url=input("URL WEBHOOK: "))
                case "adduser":
                    if db.User(username=getpass.getuser()).get_rank_by_username()[0][0] == "admin":
                        user = input("Username: ")
                        rank = input("Rank: ")
                        plan = input("Plan: ")
                        script.subscribe.add_client(user=user, rank=rank, plan=plan)
                    else:
                        raise ValueError("You are not allowed to use this command.")
                case "revoke":
                    if db.User(username=getpass.getuser()).get_rank_by_username()[0][0] == "admin":
                        user = input("Username: ")
                        script.subscribe.revoke(user=user)
                    else:
                        raise ValueError("You are not allowed to use this command.")
        except ValueError as e:
            print(f"{e}")
                    
