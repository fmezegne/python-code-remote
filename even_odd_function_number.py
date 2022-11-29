#check if input from user is an even or odd number using function

#define function
def odd_or_even(number):
    if number % 2 !=0:
        print(f"your number {number} is an odd number.")
    else:
     print (f"your number {number} is an even number.")

#main body 
number = int(input("give me a number between 0 and 100\n"))  # this line define the variable client

#call the function 
odd_or_even(number)