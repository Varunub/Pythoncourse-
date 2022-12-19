sum3=0
def listadd(x,sum2):
    for i in x:
        if type(i)==int or type(i)==float:
            sum2=sum2+i
        if type(i)==list or type(i)==tuple:
            sum2=sum2+listadd(i,sum3)
    
    return sum2
    
def listtupleaddition(list1):    
    sum1=0
    sum2=0
    for i in list1:
        if type(i)==int or type(i)==float:
            sum1=sum1+i
        if type(i)==list or type(i)==tuple:
            sum1=sum1+listadd(i,sum2)
    return sum1
