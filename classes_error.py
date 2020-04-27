class BaseError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
class ArgsInputError(BaseError):
    pass

class TableNameError(BaseError):
    pass

class NotFoundDocFile(BaseError):
    pass

class OpenDocFileError(BaseError):
    pass
