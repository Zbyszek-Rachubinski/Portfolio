names =  input("Specify the names: ").split(',')
assignments =  input("Specify assignments number: ").split(',')
grade =  input("Specify grades: ").split(',')

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for i in range (len(names)):
    print(message.format(names[i-1], assignments[i-1], grade[i-1],  int(grade[i-1])+(2*int(assignments[i-1]))))
