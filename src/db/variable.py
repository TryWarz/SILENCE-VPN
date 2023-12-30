from src.db.database import MySQL

# get user with MySQL
class User:
    def __init__(self, username=None, password=None ,plan=None, liste_name=None):
        self.username = username
        self.password = password
        self.plan = plan
        self.liste_name = liste_name

    def get_user(self):
        query = "SELECT * FROM users WHERE user=%s AND password=%s"
        return MySQL().execute(query, (self.username, self.password))

    def get_all_users(self):
        query = "SELECT * FROM users"
        return MySQL().execute(query)

    def get_user_by_username(self):
        query = "SELECT * FROM users WHERE user=%s"
        return MySQL().execute(query, (self.username))
    
    def get_plan_by_username(self):
        query = "SELECT plan FROM users WHERE user=%s"
        result = MySQL().execute_one(query, (self.username))
        return result
    
    def get_2fa_by_username(self):
        query = "SELECT 2factive FROM users WHERE user=%s"
        result = MySQL().execute_one(query, (self.username))
        return result

    def get_plans(self):
        query = "SELECT name FROM plans"
        return MySQL().execute(query)

    def plan_exists(self):
        query = "SELECT name FROM plans WHERE name=%s"
        result = MySQL().execute(query, (self.plan))
        return bool(result)

    def get_plans_by_name(self):
        query = "SELECT name FROM plans WHERE name=%s"
        return MySQL().execute(query, (self.plan))
    
    def get_plans_vip_by_name(self):
        query = "SELECT vip FROM plans WHERE name=%s"
        return MySQL().execute(query, (self.plan))

    def get_plans_concurrent_by_name(self):
        query = "SELECT concurrent FROM plans WHERE name=%s"
        return MySQL().execute(query, (self.plan))
    
    def get_plans_maxtime_by_name(self):
        query = "SELECT maxtime FROM plans WHERE name=%s"
        return MySQL().execute(query, (self.plan))

    def get_logs_by_user(self):
        query = "SELECT * FROM logs WHERE `user`=%s"  # Modified query to use backticks around 'user'
        return MySQL().execute(query, (self.username))
    
    def get_rank_by_username(self):
        print(self.username)
        query = "SELECT rank FROM users WHERE `user`=%s"
        return MySQL().execute(query, (self.username,))

    def get_expiration_by_username(self):
        query = "SELECT duration FROM users WHERE `user`=%s"  # Modified query to use backticks around 'user'
        return MySQL().execute(query, (self.username))
    
    def get_2fcode_by_username(self):
        query = "SELECT 2fcode FROM users WHERE user=%s"
        return MySQL().execute(query, (self.username))
    
    def get_vip_by_username(self):
        query = "SELECT vip FROM users WHERE user=%s"
        return MySQL().execute(query, (self.username))
    
    