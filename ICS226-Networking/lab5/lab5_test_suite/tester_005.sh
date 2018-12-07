#!/bin/bash
# Points: 1
rm -rf test_005
mkdir test_005
mkdir test_005/ics226
mkdir test_005/ics226/lab5
cp ClientA.java ServerA.java test_005/ics226/lab5

cd test_005

javac ics226/lab5/*.java

echo 'Version A Test 5: - 5 10 3'
java ics226.lab5.ServerA 21114 &
sleep 1
java ics226.lab5.ClientA localhost 21114 - 5 10 3


