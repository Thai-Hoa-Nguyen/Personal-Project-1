class Scientist:
    def __init__(self, first_name,last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def full_name(self) -> str:
        return f"Full Name: {self.__first_name} {self.__last_name}"
    
#Test
test1 = Scientist("Thai", "Nguyen")


print(test1.full_name)

