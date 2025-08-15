# # #Question1: Student Grades Processing
# # You need to write a Python program to process a student's grades. The program needs to perform the 
# # following functions:

# # Store information and notes for 10 students using a dictionary. Let each student have their name,
# # surname and grades (Midterm, Final and Oral grades). For example:

# # image

# # 1-Calculate each student's GPA and add it to the dictionary.

# # # 2-Find the student with the highest GPA and print it on the screen.

# 3- Separate each student's name from their surname and store them in a separate tuple and add them to a list.

# 4-Sort the names in alphabetical order and print the sorted list on the screen.

# 5-Keep students with a GPA below 70 in a cluster (set).
dict_student={
    "ahmed ayoub":[85,90,78],
    "mohamad alkhateeb":[92,88.76],
    "razan shamsi":[78,89,95],
    "layth abaz":[65,70,80],
    "mahmoud hamdan":[50,60,55],
    "ali mansour":[88,85,90],
    "omar farzat":[72,68,74],
    "khaled tlass":[95,90,88],
    "abdullah jomaa":[45,50,55],
    "abdulrahman bakkour":[80,75,82]
}
# print(dict_student)
# Grades=dict_student.values()
# print(Grades)
# for x in Grades :
#     GBA=sum(x)/3
#     dict_student={"ahmed ayoub":[85,90,78,GBA],
#     "mohamad alkhateeb":[92,88.76,GBA],
#     "razan shamsi":[78,89,95,GBA],
#     "layth abaz":[65,70,80,GBA],
#     "mahmoud hamdan":[50,60,55,GBA],
#     "ali mansour":[88,85,90,GBA],
#     "omar farzat":[72,68,74,GBA],
#     "khaled tlass":[95,90,88,GBA],
#     "abdullah jomaa":[45,50,55,GBA],
#     "abdulrahman bakkour":[80,75,82,GBA]
# }
# print(dict_student)
# #2
# max_GBA=max(values[-1] for values in dict_student.values())
# print(max_GBA)
# #3
# name_tuple=[]
# for FULL_NAME in dict_student:
#     first_name,sur_name=FULL_NAME.split()
#     name_tuple.append((first_name,sur_name))
#     print(name_tuple)
#     #4
# sort_name=[]
# sort_name.append( sorted(dict_student.keys()))
# print(sort_name)
#5
minimum_GBA=set()
for name,values in dict_student.items():
    GBA=values[-1]
    if GBA<70:
        minimum_GBA.add(name)
print(minimum_GBA)

    
    
    