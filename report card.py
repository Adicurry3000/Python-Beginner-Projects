name=str(input("Enter the Name: "))
grade=int(input("Enter the Grade: "))
father_name=str(input("Enter the Father's Name: "))
mother_name=str(input("Enter the Mother's Name: "))
dob=input("Enter the Date of Birth: ")
english=int(input("Enter English Marks: "))
science=int(input("Enter Science Marks: "))
maths=int(input("Enter Maths Marks: "))
total=english+science+maths
print("Name: ",name)
print("Grade: ",grade)
print("Father's Name: ",father_name)
print("Mother's Name: ",mother_name)
print("Date of Birth: ",dob)
print("English Marks: ",english,". Percentage is",(english/total)*100,".")
print("Science Marks: ",science,". Percentage is",(science/total)*100,".")
print("Maths Marks: ",maths,". Percentage is",(maths/total)*100,".")
print("The total is",english+science+maths,".")
