class Response:
    @staticmethod
    def success(data, code=200):
        return {
            "code": code,
            "data": data
        }, code

    @staticmethod
    def error(message, code):
        return {
            "error": {
                "code": code,
                "message": message
            }
        }, code