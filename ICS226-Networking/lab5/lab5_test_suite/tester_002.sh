#!/bin/bash
# Points: 1
rm -rf test_002
mkdir test_002
mkdir test_002/ics226
mkdir test_002/ics226/lab5
cp ClientA.java ServerA.java test_002/ics226/lab5

cd test_002

javac ics226/lab5/*.java

echo 'Version A Test 2: + 5 4 2 1 10 15 7 0 4'
java ics226.lab5.ServerA 21111 &
sleep 1
java ics226.lab5.ClientA localhost 21111 + 5 4 2 1 10 15 7 0 4

