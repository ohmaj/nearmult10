def near10():
    number = int(input('enter a number: '))
    if number >=9:
        #should have used modulus
        if ((int(number/10)*10)+8)<=number:
            return (True)
        elif number<=((int(number/10)*10)+2):
            return (True)
        else: 
            return (False)
    else:
        if 8<=number<=12:
            return (True)
        else:
            return (False)
def printResponse():
    boolResponse=near10()
    if boolResponse==True:
        return ('Number is within 2 a multiple of 10')
    else:
        return ('Number is NOT within 2 of a multiple of 10')

print (printResponse())
