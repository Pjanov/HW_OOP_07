
class Hello:
    def __init__(self, name):
        self.__name = name

    def hi(self):
        print(f"Привет {self.__name}")
