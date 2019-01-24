#!/bin/bash
# Points: 1
rm -rf test_006
mkdir test_006
mkdir test_006/ics226
mkdir test_006/ics226/lab5
cp ClientA.java ServerA.java test_006/ics226/lab5

cd test_006

javac ics226/lab5/*.java

echo 'Version A Test 6: * 5 10'
java ics226.lab5.ServerA 21115 &
sleep 1 
java ics226.lab5.ClientA localhost 21115 '*' 5 10


