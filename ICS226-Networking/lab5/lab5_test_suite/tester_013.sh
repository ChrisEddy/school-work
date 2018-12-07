#!/bin/bash
# Points: 1
rm -rf test_013
mkdir test_013
mkdir test_013/ics226
mkdir test_013/ics226/lab5
cp ClientB.java ServerB.java test_013/ics226/lab5

cd test_013

javac ics226/lab5/*.java

echo 'Version B Test 6: * 5 10'
java ics226.lab5.ServerB 31115 &
sleep 1 
java ics226.lab5.ClientB localhost 31115 '*' 5 10


