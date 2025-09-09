
#Miheret Gebrehans
#caseStudy
#This app determines academic recognition using students GPAs.
def student_awards():
    while True:
        last_name = input("Please enter student's last name(otherwise 'ZZZ'to quit):")
        if last_name.upper() =="ZZZ":
            print("Exiting student record.")
            break

        first_name = input("Please enter student's first_name:")
        
        try:
            gpa = float(input("Please enter student's GPA:"))
        except ValueError:
            print("Please enter a numeric value.")
            continue

        print(f"\nStudent: {first_name}{last_name}")
        if gpa >= 3.5:
            print("Congratulations! You made it to the Dean's List.")
        elif gpa>=3.25:
            print("Well done! You've made to the Honor Roll.")
        else:
            print("Maybe next time,keep trying.")
        
student_awards()

    