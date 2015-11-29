#Name: Lars Hedlund
#ID Number: 00308102
#Tutorial number: 02

#Welcome Message
print ("""
Welcome to Lars Hedlund's Weighted Grade Point Average Calculator.

Please enter your grades in the following prompts.
""")

#Mini assignment prompts
print ("What grade did you receive for the...")
mini1 = float(input("%36.0s" % "first mini assignment? "))
mini2 = float(input("second mini assignment? "))
mini3 = float(input("third mini assignment? "))
mini4 = float(input("fourth mini assignment? "))
mini5 = float(input("fifth mini assignment? "))
mini6 = float(input("sixth mini assignment? "))
print ("Thank you. Now for the full assignments.\n")

#Full assignment prompts
print ("What grade did you receive for the...")
full1 = float(input("first full assignment? "))
full2 = float(input("second full assignment? "))
full3 = float(input("third full assignment? "))
full4 = float(input("fourth full assignment? "))
full5 = float(input("fifth full assignment? "))
print ("Thank you. Now for the exam grades.\n")

#Exam assignment prompt
midterm_exam = float(input("What grade did you receive for the midterm exam? "))
final_exam = float(input("What grade did you receive for the final exam? "))
print ("Thank you.\n")

#Calculate weighted averages and term grade
mini_weighted = ((mini1 + mini2 + mini3 + mini4 + mini5 + mini6)/6) * 0.06
full_weighted = ((full1 + full2 + full3 + full4 + full5)/5) * 0.29
midterm_weighted = midterm_exam * 0.25
final_weighted = final_exam * 0.40
term_grade = mini_weighted + full_weighted + midterm_weighted + final_weighted

#Display weighted averages
print ("Weighted mini assignment grade %0.2f" %mini_weighted)
print ("Weighted assignment grade %0.2f" %full_weighted)
print ("Weighted midterm grade %0.2f" %midterm_weighted)
print ("Weighted final exam grade %0.2f" %final_weighted)
print ("Weighted term grade %0.2f" %term_grade)

