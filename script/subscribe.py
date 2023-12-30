import src.db
import datetime, time
import os

db = src.db.User()
MySQL = src.db.MySQL()

class subscribe:
    def __init__(self) -> None:
        pass

    def add_client(user, rank, plan):
        # Get the current time
        date_actuelle = datetime.date.today()
        # Add 30 days to the current time
        duration = date_actuelle + datetime.timedelta(days=30)
        # Insert the user into the database
        MySQL.execute_insert("INSERT INTO users (user, rank, plan, duration) VALUES (%s, %s, %s, %s, %s)", (user, rank, plan, duration))

    def revoke_client():
        try:

            
            # Get the current time
            now = datetime.date.today()

            # Get user data from the 'users' table
            sql = 'SELECT id, user, plan, duration FROM users'
            cursor = src.db.MySQL().execute(sql)

            for user_data in cursor:
                if user_data['duration'] is not None and user_data['duration'] < now:
                    # Revoke the user
                    os.system(f"sudo ./openvpn-install.sh -r {user_data['user']}")
            # Create a temporary list of users to delete
            to_delete = []

            # Iterate over users
            for user_data in cursor:
                if user_data['duration'] is not None and user_data['duration'] < now:
                    to_delete.append(user_data['id'])

            # Delete users to delete
            for id in to_delete:
                src.db.MySQL().execute('DELETE FROM users WHERE id = %s', (id,))

        except Exception as e:
            print(f"Error connecting to the database: {e}")


    def auto_check():
        while True:
            revoke_client()
            time.sleep(300)