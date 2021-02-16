
def fct(n):
    a=0
    b=1
    my_list = []
    while(b<n):
        a, b=b, a+b
        my_list.append(a)
    return my_list
    




n= int(input('donner un nombre'))
print(fct(n))

