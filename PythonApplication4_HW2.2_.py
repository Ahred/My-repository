
#2.2
number = int(input('Enter 4 digit number''\n'))
if number >= 1000 and number <= 9999:
    print('Your number is ', number)
    res = [int(x) for x in str(number)] 
    print(res)
    print(res[0]*res[1]*res[2]*res[3])
    res.reverse()
    print(res)
    res.sort()
    print(res)
else:
    print('Try again, your number in not 4 digit')




    






    