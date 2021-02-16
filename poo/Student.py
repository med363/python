class Student:
    nbre_of_student=0 #initialiser un occ ou class attribut et ce attribut partage avec tout les objets
    def __init__(this,name='saber',age=17,courses='none'):
        this.name=name
        this.age=age
        this.courses=courses
        Student.nbre_of_student+=1
    def describe(this):
        print(f"the name is {this.name} and the age is {this.age}") #print("the name is {} and the age is {}".format(this.name,this.age))
    
    def olderOrNot(this,num):
        if this.age <=num:
            print('is not older')
        else:
            print('is  older')

ob1 = Student( "amine",23,['python','React'])
ob2 = Student()
ob2.name='mohamed'
print('object1: ',ob1.age,ob1.courses,ob1.name,'||object2: ',ob2.name,ob2.age,ob2.courses )
print("nbre d'object : ", Student.nbre_of_student) #ob1.nbre_of_student
ob2.describe()
ob1.olderOrNot(30)#30 refred num
