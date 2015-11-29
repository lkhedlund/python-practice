#Name: Lars Hedlund
#ID Number: 00308102
#Tutorial number: 02

#Start of weighted grade point average calculator
print = ("""
Welcome to the Weighted Grade Point Average Calculator

To start, please enter your grades in the following prompts.

Please note: You will be asked for six mini assignment, 
five full assignment, one midterm, and one final exam grades. 

Let's start with the mini assignments:
""")

#Mini assignment prompts
mini1 = float(input("What grade did you receive for the first mini assignment? "))
mini2 = float(input("What grade did you receive for the second mini assignment? "))
mini3 = float(input("What grade did you receive for the third mini assignment? "))
mini4 = float(input("What grade did you receive for the fourth mini assignment? "))
mini5 = float(input("What grade did you receive for the fifth mini assignment? "))
mini6 = float(input("What grade did you receive for the sixth mini assignment? "))
print = ("Thank you. Now, your full assignments?")

#Full assignment prompts
full1 = float(input("What grade did you receive for the first full assignment? "))
full2 = float(input("What grade did you receive for the second full assignment? "))
full3 = float(input("What grade did you receive for the third full assignment? "))
full4 = float(input("What grade did you receive for the fourth full assignment? "))
full5 = float(input("What grade did you receive for the fifth full assignment? "))
print = ("Thank you. Now, your exam grades?")

#Exam assignment prompt
midterm_exam = float(input("What grade did you receive for the midterm exam? "))
final_exam = float(input("What grade did you receive for the final exam? "))
print = ("Thank you.")

#Calculate weighted averages and term grade
mini_weighted = ((mini1+mini2+mini3+mini4+mini5+mini6)/6) * 0.06
full_weighted = ((full1+full2+full3+full4+full5)/5) * 0.29
midterm_weighted = midterm_exam * 0.25
final_weighted = final_exam * 0.40
term_grade = mini_weighted + full_weighted + midterm_weighted + final_weighted

#Display weighted averages
print = ("Weighted mini assignment grade %0.2f" %mini_weighted)
print = ("Weighted assignment grade %0.2f" %full_weighted)
print = ("Weighted midterm grade %0.2f" %midterm_weighted)
print = ("Weighted final exam grade %0.2f" %final_weighted)
print = ("Weighted term grade %0.2f" %term_grade)

