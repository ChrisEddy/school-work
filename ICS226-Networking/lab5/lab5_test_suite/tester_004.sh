#!/bin/bash
# Points: 1
rm -rf test_004
mkdir test_004
mkdir test_004/ics226
mkdir test_004/ics226/lab5
cp ClientA.java ServerA.java test_004/ics226/lab5

cd test_004

javac ics226/lab5/*.java

echo 'Version A Test 4: - 10 3 2'
java ics226.lab5.ServerA 21113 &
sleep 1
java ics226.lab5.ClientA localhost 21113 - 10 3 2


