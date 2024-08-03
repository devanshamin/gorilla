class NoAPIKeyError(Exception):
    def __init__(self, missing_key_name):
        self.message = f"❗️Please fill in the {missing_key_name} in the .env file under gorilla/berkeley-function-call-leaderboard folder. They are required for the executable test category evaluation."
        super().__init__(self.message)
        
        
class BadAPIStatusError(Exception):
    def __init__(self, errors, error_rate):
        self.errors = errors
        self.error_rate = error_rate