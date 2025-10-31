# Test script for comparison assignment
#
# run python test_compare.py <your script name>
#
# Test script will run your file and check the statements for inconsistency
#
# Note there are security issues with code like this.  Calling user-supplied code from your
# own is not recommended.  This is just a workaround to make it easy to assess.
#

from sys import argv
import os
import re
from subprocess import getstatusoutput

# check arguments
if len(argv)==1:
    # if none given, assume default name in same directory as test
    dir_name = os.path.dirname(os.path.abspath(__file__))
    script_name = os.path.join(dir_name, 'ExerciseP1.py')
    print('Assuming script name',script_name)
elif len(argv)==2:
    script_name = argv[1]
    print('Testing script name',script_name)
else:
    print('Usage: python', argv[0], '[script filename]')
    exit(1)

# run supplied script and capture output
print('Running Python script', script_name)
exit_code, output_text = getstatusoutput('python3 ' + script_name)

# print some information if there's an error
if exit_code==0:
    print('Script ran OK')
    print('Output is below')
    print()
    print(output_text)
    print()
else:
    print('Script had error, code', exit_code)
    print('Output is below')
    print()
    print(output_text)
    print()
    raise ValueError('Script terminated with error')

# script ran - extract numbers
numbers_as_text = re.findall('-?[0-9]+.?[0-9]*',
                             output_text)
#print('Things like numbers:',numbers_as_text)

assert len(numbers_as_text)>=3, "Cannot find three numbers"

number_values = [float(n) for n in numbers_as_text]
#print('Number values:', number_values)

if len(number_values)>3:
    print("More than three numbers found - will just take final three")

heading = number_values[-1]
y_pos = number_values[-2]
x_pos = number_values[-3]

print('Got X =',x_pos,'Y =',y_pos,'heading =',heading)

# check close to correct answers
def are_close(a,b,tol=0.001):
    return (a-b)**2 < tol**2

assert are_close(x_pos,8.072), "Wrong X"
assert are_close(y_pos,115.123), "Wrong Y"
assert are_close(heading,0.140), "Wrong heading"

# everything OK if we got to here
print('Test passed: all lines verified')
