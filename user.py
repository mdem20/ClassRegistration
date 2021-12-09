class User:

    def __init__(self, user_id, pin):
        self._id = user_id
        self._pin = pin

    def get_id(self):
        return self._id

    def get_pin(self):
        return self._pin
