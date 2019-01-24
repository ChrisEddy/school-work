#!/bin/bash
# Points: 1
rm -rf test_014
mkdir test_014
mkdir test_014/ics226
mkdir test_014/ics226/lab5
cp ClientB.java ServerB.java test_014/ics226/lab5

cd test_014

javac ics226/lab5/*.java

echo 'Version B Test 7: * 6 6 6 6 6 6 6 6 6 6'
java ics226.lab5.ServerB 31116 &
sleep 1
java ics226.lab5.ClientB localhost 31116 '*' 6 6 6 6 6 6 6 6 6 6


