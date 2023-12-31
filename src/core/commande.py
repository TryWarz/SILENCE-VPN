import src.interface as interface 
import src.db as db
import script
from src.core.download import Zip
from colorama import Fore as F
import getpass, os , platform
import datetime


class Commande:
    def __init__(self):
        pass

    def Commande():
        try:
            print(f"{F.LIGHTBLACK_EX}┌⎯⎯⎯ [{F.LIGHTWHITE_EX} Silence ∙ {getpass.getuser()} {F.LIGHTBLACK_EX}]")
            Commande = input("└───➤  ").lower()
        
            match Commande:
                case "help":
                    interface.ASCII().home()

                case "plans":
                    interface.ASCII().cls()
                    username = getpass.getuser()
                    rank = db.User(username=username).get_rank_by_username()[0][0]
                    plan = db.User(username=username).get_plan_by_username()[0]
                    duration = db.User(username=username).get_duration_by_username()[0]
                    duration = db.User(username=username).get_duration_by_username()[0][0]  
                    duration_formatted = datetime.datetime.strptime(str(duration), "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y %H:%M:%S")
                    interface.ASCII().plans(user=username, rank=rank, plan=plan, duration=duration_formatted)
                
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
                    
