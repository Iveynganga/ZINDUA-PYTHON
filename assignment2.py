score = int(input ("enter your score: " ))

# assign the students with the grade B
if (score >= 70 and score <=100) :
    print("You've scored an A")

# assign the students with the grade B
elif (score >=60 and score <70) :
   print ("You've scored a B") 

# assign the students with the grade C
elif (score >=50 and score <60) :
   print ("You've scored a C") 

# assign the students with the grade D
elif (score >=40 and score <50) :
   print ("You've scored a D") 

# assign the students with the grade E
elif (score >=30 and score <40) :
   print ("You've scored a E")

elif (score <0 ) :
 print("Invalid")

# students with any other score
else:
   print("Fail")



