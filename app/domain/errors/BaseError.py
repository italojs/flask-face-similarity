class BaseError(Exception):
    def __init__(self, msg, type):
        self.msg = msg
        self.type = type

    def __str__(self):
        return (self.msg, self.type)