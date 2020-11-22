class HttpError(Exception):
    def __init__(self, status_code, message):
        super().__init__()
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return {
            'message': self.message,
            'status_code': self.status_code
        }