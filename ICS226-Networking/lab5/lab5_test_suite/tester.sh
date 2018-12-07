# usage: ./tester.sh 0XX
#    - where 0XX is the test you want to run
#    - 001-007 run Version A tests
#    - 008-014 run Version B tests
#
# Run this test with the source .java files in the
# same directory -- you do not need to provide package
# folders etc, as the tester scripts do this for you.
if [ $# -eq 0 ]
	then
		echo usage: ./tester.sh 0XX
		echo     - where 0XX is the test you want to run
		echo     - 001-007 run Version A tests
		echo     - 008-014 run Version B tests
		echo 
		echo  Run this test with the source .java files in the
		echo  same directory -- you do not need to provide package
		echo  folders etc, as the tester scripts do this for you.
	else
		index=$1
		./tester_${index}.sh 
fi
