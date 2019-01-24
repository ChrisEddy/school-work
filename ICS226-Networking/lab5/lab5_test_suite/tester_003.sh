#!/bin/bash
# Points: 1
rm -rf test_003
mkdir test_003
mkdir test_003/ics226
mkdir test_003/ics226/lab5
cp ClientA.java ServerA.java test_003/ics226/lab5

cd test_003

javac ics226/lab5/*.java

echo 'Version A Test 3: + 5 4 2 1 10 15 7 0 4 10'
java ics226.lab5.ServerA 21112 &
sleep 1
java ics226.lab5.ClientA localhost 21112 + 5 4 2 1 10 15 7 0 4 10


