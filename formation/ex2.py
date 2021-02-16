# //fonction trier(classeur, valeur) qui place une valeur dans un dictionnaire en fonction de son signe
classeur ='positive'
def trier(classeur,v):
    my_dect = {}
# v=10

    if classeur =='positive':
        my_dect["positiv"]= [i for i in range(1,v,1)]
    elif classeur =='negative':
        # my_dect["negative"]= [i for i in range(0,v,-1)]
        my_dect["negative"]=[i for i in range(-v,0,1)]
    else:
        print('err!!!')
    print(my_dect)

n=int(input('donner un nnbre: '))
keyy=input('donner la parite en tout lettre')
trier(keyy,n)


        
    