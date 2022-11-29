# Write a program calculator that will take 2 number and the user will select what kind of operator to use

#define function
def calculator(operation):
    if operator in arithmetic_operator:
        print( f"{operation} = {eval(operation)}")    # The eval function will evaluate or resolve the variable operation
    else:
        print(f" Sorry {operator} is not an arithmetic operator!!! TRY AGAIN.")

#main body
arithmetic_operator = [ '-' , '*', '/' , '% ', '+', '**', '//' ]
numb_1 = int(input("give me an odd number\n"))
numb_2 = int(input("give me an even number\n"))
operator = (input("what type of arithmetic operator would you like to use? \n"))
operation = f"{numb_1}  {operator}  {numb_2}" 
# if operator in arithmetic_operator:
#     print( f"{operation} = {eval(operation)}")
# else:
#     print(f" Sorry {operator} is not an arithmetic operator!!! TRY AGAIN.")

#call the function 
calculator(operation)
