'''
## Exercise 4 - Boolean Grade Assignment

At the University of CPA, we use the standard university grading scheme:

| Grade| Classification |
|------|------|
| 70+ | First |
| 60-70 | 2.1  |
| 50-60 | 2.2  |
| 40-50 | 3rd  |
| under 40 | Fail |

The "grade" used to calculate your classification is a weighted average of the marks for the two assigments- 
the first worth 20% and the second worth 80%. 
However, we also have an additional rule that you must achieve at least a passing mark (40%) in the second assignment to pass the course.

Write some code that uses Boolean expressions to determine the following students overall classification

| Student | Assignment 1| Assignment 2 |
| ------- | ----------- | -------------|
| Martin  | 100         | 35           |
| Arthur  | 40          | 65           |
| Hemma   | 25          | 80           |
| Josh    | 60          | 45           |
'''

#First make some variable to store Martin's results.
martin_a1 = 100
martin_a2 = 35
#Next we need some variables to store the assessment weightings.
assessment1_weight = 0.2
assessment2_weight = 0.8
#Calculate the weighted average
martin_average = martin_a1 * assessment1_weight + martin_a2 * assessment2_weight
#Check if assessment two is passed
martin_passes_a2 = martin_a2 >= 40
#Use boolean expressions to determine overall grade.
martin_gets_first = (martin_average >= 70) and martin_passes_a2
martin_gets_2_1 = (martin_average >= 60) and (martin_average < 70) and martin_passes_a2
martin_gets_2_2 = (martin_average >= 50) and (martin_average < 60) and martin_passes_a2
martin_gets_third = (martin_average >= 40) and (martin_average < 50) and martin_passes_a2
martin_fails = not (martin_gets_first or martin_gets_2_1 or martin_gets_2_2 or martin_gets_third)

print("Martin:")
print("Average: ", martin_average)
print("Passes A2: ", martin_passes_a2)
print("First: ", martin_gets_first)
print("2.1: ", martin_gets_2_1)
print("2.2: ", martin_gets_2_2)
print("Third: ", martin_gets_third)
print("Fail: ", martin_fails)