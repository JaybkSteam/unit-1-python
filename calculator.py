def calculate(number1,number2,op):
    #So first i make a function called calucate because the calculate function uses conditional statements which would 
    #allow me to start the code
    if op == '+':
        result = number1+number2
    elif op == '-':
        result = number1-number2
    elif op == '*':
        result =  number1*number2
    elif op == '/':
        result = number1/number2
    elif op=='^':
        result =  number1**number2
    elif op=='%':
        result = number1%number2
    elif op=='//':
        result = number1//number2
    else:
        raise ValueError('Invalid operator')
    #now for this i have the varibale op equal different opertaions like additiona and subtraction and in order to do that
    # I use conitional statements like prevously stated so in order for the math to tak3 place i have it so that if the variable op is any of the 
    # of the  math opertations I choose it will do that math opertaion on variable number 1 and 2.
    
    if result.is_integer():
        result = int(result)
        #now this part is if there is a error with the operations if a a none valid operation is put in the code 
        #the user will be alerted and they can fix the error and put one of the right opertaions/
        
    return result

continue_calculating = True
while continue_calculating is True:
    number1 = float(input('Enter your first number: '))
    op = input('Enter operator (+,-,*,/,^,//,%): ')
    number2 = float(input('Enter your second number: '))
    # for this part of the code this is what will allow the user to input the two number they want to use and the opertaion.
    print(number1,op,number2)
    result=calculate(number1,number2,op)
    print('=',result)
    yes_or_no = input('Continue? (y/n): ')
    if yes_or_no == 'n':
        continue_calculating = False
        # And this part of the code is so that the code repeats itself again if the user wants to continue to do math equations.