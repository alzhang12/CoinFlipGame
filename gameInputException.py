class GameInputException(Exception):
    def __init__(self, message = 'Input Error: please enter \'yes\' or \'no\''):
        print(message)
        super().__init__(message)
