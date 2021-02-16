class Student:
    nbre_of_student=0 #initialiser un occ ou class attribut et ce attribut partage avec tout les objets
    def __init__(this,name='saber',age=17,courses='none'):
        this.__name=name      # this.name=name
        this.__age=age        # this.age=age
        this.__courses=courses# this.courses=courses
        Student.nbre_of_student+=1
    
    def getName(this):
        return this.__name

    def setName(this,New_name):
        this.__name = New_name

    def getAge(this):
        return this.__age

    def setAge(this,New_age):
        this.__age = New_age

    def describe(this):
        print(f"the name is {this.__name} and the age is {this.__age}")
   

ob1 = Student( "amine",23,['python','React'])

ob1.setName('ahmed')
print(ob1.getName())
ob1.name='mohamed'#on a acces direct sur les attribut puisque il est public attribut pour que les methode get et set soient utiles il faut que les attributs soient priver
print(ob1.getName())
ob1.fullname='med amine blibech'#fullname commetant nauveau variable
print(ob1.fullname)
ob1.setName('islem')
ob1.setAge(22)
ob1.describe()
#nb:si on supprime les methodes getter et setter on ne peut change les variable
# ob1.describe()