# write a code that will automatically translate an input from a user from French to English using FUNCTION

# define your dictionary
french_to_english ={"PRUNE" : "safou",             
"ENFANT": "child",
"HEUREUX": "happy",
"DORMIR": "sleep",
"ORIGINAIRE": "native",
"AFRIQUE": "Africa"
}

#define function
def translator_to_english(user):
    if user in french_to_english:
        print(translation)
    else:
        print(f"{user} does not exist in the dictionary")

#main body 
user = input("ENTER A WORD OF YOUR CHOICE IN FRENCH\n")
user = user.upper()             #this will convert what ever user input to uppercase so that it can match my keys in the dictionary.
translation = french_to_english.get(user)

#call the function 
translator_to_english(user)