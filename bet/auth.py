class AuthManager:
    def __init__(self):
        self.users_db = {}
        self.current_users = None
    def sign_up(self, username, password, confirm):
        if username in self.users_db:
            return False
        if password != confirm:
            return False
        self.users_db[username] = {
            "password": password
        }
        return True
    def log_in(self, username, password):
        if username not in self.users_db:
            return False
        if self.users_db[username]["password"] != password:
            return False
        self.current_users = username
        return True
    def log_out(self):
        username = self.current_users
        self.current_users = None
        return username 
    def is_login(self):
        return self.current_users is not None
    def get_current_user(self):
        return self.current_users
    def user_exists(self, username):
        return username in self.users_db