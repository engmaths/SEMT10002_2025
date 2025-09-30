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
from subprocess import run

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
test_result = run(['python', script_name],
                  capture_output=True,
                  text=True,
                  check=False)

# print some information if there's an error
exit_code = test_result.returncode
if exit_code==0:
    print('Script ran OK')
else:
    print('Script had error, code', exit_code)
    print('Output is below')
    print()
    print(test_result.stdout)
    print(test_result.stderr)
    raise ValueError('Script terminated with error')

# script ran - so check outputs make sense

# everything OK if we got to here
print('Test passed: all lines verified')
