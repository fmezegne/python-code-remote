# write a code that will automatically translate an input from a user to ENGLISH.
# And if that input from user does not exixt in your ditionary, 
# simply return "input" does not exixt in the dictionary.
french_to_english ={"PRUNE" : "safou",
"EST": "is",
"UN": "a",
"FRUIT": "fruit",
"ORIGINAIRE": "native",
"DE": "from",
"AFRIQUE": "Africa"
}

user = input("ENTER A WORF OF YOUR CHOICE IN CAPITAL LETTER\n")
translation = french_to_english.get (user)

if user in french_to_english:
    print(translation)
else:
    print(f"{user} does not exist in the dictionary")

sentence = french_to_english.get("PRUNE") + " " + "is a fruit native from Africa. It is very delicious with roasted corn."
# sentence= french_to_english.get("PRUNE") + " " + french_to_english.get("EST") + " " + french_to_english.get("UN") + " " + french_to_english.get("FRUIT") + " " + french_to_english.get("ORIGINAIRE") + " " + french_to_english.get("DE") + " " + french_to_english.get("AFRIQUE") + "." + "It is very delicious with roasted corn."
print(sentence)

# print("sentence:", sentence)




# inexistant_item = translator.get ("FRUIT")

# if user == "PRUNE":
#     print(translation)
# elif inexistant_item:
#     print(inexistant_item)
# else:
#     print("Fruit does not exist in the dictionary")


# translation = translator.get ( "PRUNE" ) + translator.get ( "EST" ) +  translator.get ( "UN" )
# inexistant_item = translator.get ("FRUIT")
# if translation:
#     print('translation:' , translation)
# elif inexistant_item:
#     print('inexistant_item:', inexistant_items)
# else:
#     print("Fruit does not exist in the dictionary")
# user = input("entre un mot de ton choix\n")

# acd = {"FRUIT": "fruit"}
