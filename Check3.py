#To check if a number is a multiple of 3 by adding the digits together (and repeating it if it's still not 3, 6, or 9)
#I wanted to test my ability with recursion + see if I could use the str and int functions like this

def check3(num):
    if len(str(num))==1:
        if num==3 or num==6 or num==9:
            return(True)
        else:
            return(False)
    else:
        total=0
        for char in str(num):
            total += (int(char))
        return (check3(total))
        
num = 42
print(check3(num))
