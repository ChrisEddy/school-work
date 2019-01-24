#!/bin/bash
# Points: 1
rm -rf test_012
mkdir test_012
mkdir test_012/ics226
mkdir test_012/ics226/lab5
cp ClientB.java ServerB.java test_012/ics226/lab5

cd test_012

javac ics226/lab5/*.java

echo 'Version B Test 5: - 5 10 3'
java ics226.lab5.ServerB 31114 &
sleep 1
java ics226.lab5.ClientB localhost 31114 - 5 10 3


