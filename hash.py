class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    # def showPersonInfo(self):
    #     print(self.name)
    #     print(self.age)
    def __str__(self):
        return f"Name is : {self.name}\t Age is :{self.age}"

#It prints when the argument are not the same in p1,p2,p3
# person1=Person("Max",42)
# person2=Person("Dany",42)
# person3=Person("Tony",18)
# print(person1.__str__())
# set1={person1, person2,person3}
# for person in set1:
#     print(person)
#===It prints when the argument are not the same in p1,p2,p3====================================
# person1=Person("Max",42)
# person2=Person("Dany",42)
# person3=Person("Max",42)
# set1={person1, person2,person3}
# for person in set1:
#     print(person)








