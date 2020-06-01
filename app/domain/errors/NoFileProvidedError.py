from  app.domain.errors.BaseError import BaseError

class NoFileProvided(BaseError):
    def __init__(self):
        msg = "No file provided."

        super(NoFileProvided, self).__init__(msg, "no_file")