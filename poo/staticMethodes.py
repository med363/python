# Staticmethode est une methode dans un class n'est pas en relation avec aucun attribut et on peut l'appeler dans une methode d'instance
class Math:
    @staticmethod
    def PI():
        return 3.14

class Pizza:
    def __init__(this,ingrediant,rayon):
        this.rayon=rayon
        this.ingrediant=ingrediant

    def interfacesd(this):
        return this.calculInt(this.rayon)
    
    @staticmethod
    def calculInt(r):
        return r**2 * Math.PI()
    
ob1 = Pizza(['pichamelle','fromages','farinne'],20)
print(Pizza.calculInt(10))#appel du static methode
print(ob1.interfacesd())#appel du instance methode