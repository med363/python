# classMethode a travers laquell on peut un autre constructor avec autre attribut dans la meme class
from datetime import date
class Student:
    
    def __init__(this,name='saber',age=17,courses='none'):
        this.name=name
        this.age=age
        this.courses=courses

    @classmethod
    def InitBirth(cls,name,birth):
        return cls(name,date.today().year-birth)

    def describe(this):
        print(f"the name is {this.name} and the age is {this.age}")


    
   

ob1 = Student( "amine",23,['python','React'])
ob2=Student.InitBirth('Med salmen',2019)
ob2.describe()


