class Demo:
    def __init__(self,id:int,name:str,age:int):
        self.__id = id
        self.name = name
        self._age = age


    """ JAVA STYLE : NORMAL GETTERS SETTERS"""

    def get_id(self):
        return self.__id

    def set_id(self, id:int):
        self.__id = id

    """ PYTHONIC WAY : USING DECORATORS 
        1. FOR GETTER -> DEFINE ONLY PROPERTY
        2. FOR SETTER -> DEFINE FUNCTION_NAME.setter
    """

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,id:int):
        self.__id = id





if __name__ == '__main__':

    D1 = Demo(id=1,name='D1',age=10)

    print(D1.name)
    # print(D1.age)         # THROW ERROR
    print(D1._age)

    # print(D1.__id)        # THROW ERROR

    # print(D1._Demo__id)     # obj._MyClass__privateVar
    #
    #
    # print(D1.get_id())
    # D1.set_id(99)
    # print(D1.get_id())

    D1.id=999           # USING PYTHONIC SETTER
    print(D1.id)        # USING PYTHONIC GETTER

