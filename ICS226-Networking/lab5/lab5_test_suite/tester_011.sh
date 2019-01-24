#!/bin/bash
# Points: 1
rm -rf test_011
mkdir test_011
mkdir test_011/ics226
mkdir test_011/ics226/lab5
cp ClientB.java ServerB.java test_011/ics226/lab5

cd test_011

javac ics226/lab5/*.java

echo 'Version B Test 4: - 10 3 2'
java ics226.lab5.ServerB 31113 &
sleep 1
java ics226.lab5.ClientB localhost 31113 - 10 3 2


