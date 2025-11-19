#write a program to caluclate the mark of student and check pass and fail-#
sub1=int(input('Enter a 1st Subjact Marks :'))
sub2=int(input('Enter a 2nd Subjact Marks :'))
sub3=int(input('Enter a 3rd Subjact Marks :'))
sub4=int(input('Enter a 4th Subjact Marks :'))
sub5=int(input('Enter a 5th Subjact Marks :'))
Total_marks=sub1+sub2+sub3+sub4+sub5
percentage=Total_marks/500*100

print('The Total Mark :',Total_marks)


if percentage >=90:
 print('Distinction')
elif percentage >= 80:
  print('First Class')
elif percentage>=70: 
 print('Second Class')
elif percentage>=60:
 print('pass')
else:
 print('Fail')