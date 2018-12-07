#!/bin/bash
# Points: 1
rm -rf test_010
mkdir test_010
mkdir test_010/ics226
mkdir test_010/ics226/lab5
cp ClientB.java ServerB.java test_010/ics226/lab5

cd test_010

javac ics226/lab5/*.java

echo 'Version B Test 3: + 5 4 2 1 10 15 7 0 4 10'
java ics226.lab5.ServerB 31112 &
sleep 1
java ics226.lab5.ClientB localhost 31112 + 5 4 2 1 10 15 7 0 4 10


