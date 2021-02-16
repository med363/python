from datetime import date
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def describe(self):
        print(f"the name is {self.name} and the age is {self.age}")

    @classmethod
    def InitBirth(cls,name,birth,extra):
        return cls(name,date.today().year-birth,extra)

class Man(Person):
    sex='men'
    nbre_d_homme=0
    def __init__(self,name,age,voice):
        super().__init__(name,age)
        self.voice= voice
        Man.nbre_d_homme+=1

    def display(self):
        ch = super().describe()
        return str(ch)+ f"and voice {self.voice} and gender is {self.sex}"

ob1=Man.InitBirth("sami",1999,'egu')
# ob1=Man('salah',35,'egu')
print(ob1.display())
# print(Man.nbre_de_homme)
