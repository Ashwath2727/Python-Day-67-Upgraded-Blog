class ResultMessage:

    def __init__(self, result, state, message, code):
        self.result = result
        self.state = state
        self.message = message
        self.code = code

    def get_message(self):
        return {"result": self.result, "message": {f"{self.state}: {self.message}"}, "code": self.code}
