#!/bin/bash
# Points: 1
rm -rf test_007
mkdir test_007
mkdir test_007/ics226
mkdir test_007/ics226/lab5
cp ClientA.java ServerA.java test_007/ics226/lab5

cd test_007

javac ics226/lab5/*.java

echo 'Version A Test 7: * 6 6 6 6 6 6 6 6 6 6'
java ics226.lab5.ServerA 21116 &
sleep 1
java ics226.lab5.ClientA localhost 21116 '*' 6 6 6 6 6 6 6 6 6 6


