'''
## Exercise 4 - Fuzzy logic

We're creating a chatbot to discuss the results of a survey of 100 people.  
To make it feel more conversational, it will use phrases "a few people" and "many people" instead of saying exact numbers.  
This will be achieved using fuzzy logic.The figure at (https://raw.githubusercontent.com/engmaths/SEMT10002_2025/refs/heads/main/media/week_2/fuzzy.png) shows
two _membership functions_ for fuzzy sets labeled "a few" and "many".  
Given a value, the code should calculate both membership functions, and return the label for the set with the highest value of its membership function.

- The function for "a few" is one for values of 5 or smaller (can count on one hand), zero for values of 12 or higher (a dozen) and linear in between.
- The function for "many" is zero for values of 9 or smaller (single figures), one for values of 50 or higher (more than half) and linear in between.

Example: for value 40, the function for "a few" is zero and the function for "many" is about 0.75.  The returned label is "many".

Write some code that takes a value and returns the label "a few" or "many" using the fuzzy logic above.
Also return "none" for the case of zero and show a message for any values that do not make sense.
'''

#replace with trial values
value = 12

# check zero first
if value==0:
    print("none")
# trap errors either end
elif value<0:
    print("error - negative value")
elif value>100:
    print("error - more than total")
else:
    # calculate membership functions
    if value<=5:
        a_few = 1
    elif value>=12:
        a_few = 0
    else:
        a_few = (12 - value)/(12 - 5)
    if value<=9:
        many = 0
    elif value>=50:
        many = 1
    else:
        many = (value - 9)/(50 - 9)
    if many>a_few:
        print('Many')
    else:
        print('A few')