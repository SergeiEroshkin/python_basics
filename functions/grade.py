"""
Your task is to write a Python program that computes the letter grade earned in a fictional course.
The program will prompt the user to enter the grades earned on different components of the course.  The program will
keep prompting for grades until the user types 'end'.
If 4 or more grades are entered, your program will drop (not count) the lowest grade.
After possibly dropping the lowest grade, the program will calculate the course average assuming equal weights
(course average = sum of the grades / number of grades).
The course average will be rounded to 1 decimal.
Then the letter grade will be determined based  on the following scale:
90 and above: A
80 - 89.9:  B
70 - 79.9: C
60 - 69.9: D
below 60: F
In addition to the letter grade, the program will print out the specific grade that was dropped (only if applicable),
the rounded course average and the remaining grades as shown in the expected output below.
"""

grades = []
more_input = True
while more_input:
    user_input = raw_input('Please Enter Grade: ')
    if user_input == 'end':
        more_input = False
    elif len(user_input) == 0:
        break
    else:
        grades.append(float(user_input))
if len(grades) == 0:
    print 'No grades entered.'
else:
    while True:
        if len(grades) == 1:
            break
        elif len(grades) != 3:
            min_value = min(grades)
            grades.remove(min_value)
        else:
            break
    avg_grades = round(sum(grades) / (len(grades)), 1)
    print 'Course average ' + str(round(avg_grades, 1))
    if avg_grades >= 90:
        print 'Letter Grade: A'
    elif avg_grades > 80:
        print 'Letter Grade: B'
    elif avg_grades > 70:
        print 'Letter Grade: C'
    elif avg_grades > 60:
        print 'Letter Grade: D'
    elif avg_grades < 60:
        print 'F'
    print 'Based on following grades: \n' + '\n'.join(map(str, grades))
