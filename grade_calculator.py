#A=90
#B=80
#c=70
#D=60
#E="failed"
history_grade = int(input("what is your grade in history?\n"))
math_grade = int(input("what is your grade in math?\n"))
science_grade = int(input("what is your grade in science?\n"))
psychology_grade = int(input("what is your grade in psychology?\n"))
art_grade = int(input("what is your grade in art?\n"))

average_grade = (history_grade + math_grade + science_grade + psychology_grade + art_grade)/5

if average_grade >=90:
    print("your grade is: A")
elif average_grade >=80:
    print("your grade is: B")
elif average_grade >=70:
    print("your grade is: C")
elif average_grade >=60:
    print("your grade is: D")
else:
    print("your grade is: E")
