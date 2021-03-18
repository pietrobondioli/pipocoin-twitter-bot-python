class User:
    def __init__(self, user_id=0, user_name='name', balance=0):
        self._id = self.set_id(user_id)
        self._name = self.set_name(user_name)
        self._balance = self.set_balance(balance)

    def set_id(self, user_id):
        return str(user_id)

    def set_name(self, user_name):
        return user_name.lower()

    def set_balance(self, balance):
        return float(balance)

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_balance(self):
        return self._balance
