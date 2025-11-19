#write a program to assign grades to students and display all the grades using key() and get() methods of a dictionary
Grade={"Sahil":"A","Satyam":"B","Shivam":"C"}
for key in Grade.keys():
    print(key," ",Grade.get(key,0))
