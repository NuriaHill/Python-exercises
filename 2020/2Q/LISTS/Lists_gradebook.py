last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
#1. Create a list called subjects
subjects =["physics", "calculus", "poetry", "history"]
#2. Create a list called grades
grades =[98, 97, 85, 88]
#3.Use zip to combine subjects and grades
gradebook = list(zip(subjects, grades))
#4.print gradebook
print(gradebook) #[('physics', 98), ('calculus', 97), ('poetry', 85), ('history', 88)]
#5 Append new subject and score 
subjects.append("computer science")
grades.append(100)

gradebook = list(zip(subjects, grades))

print(gradebook)

#append new subject and grade to gradebook
gradebook = list(zip(subjects, grades))

gradebook.append(("visual arts", 93))

print(gradebook)

# add both gradebooks

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)