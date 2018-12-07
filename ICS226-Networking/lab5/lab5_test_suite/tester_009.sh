#!/bin/bash
# Points: 1
rm -rf test_009
mkdir test_009
mkdir test_009/ics226
mkdir test_009/ics226/lab5
cp ClientB.java ServerB.java test_009/ics226/lab5

cd test_009

javac ics226/lab5/*.java

echo 'Version B Test 2: + 5 4 2 1 10 15 7 0 4'
java ics226.lab5.ServerB 31111 &
sleep 1
java ics226.lab5.ClientB localhost 31111 + 5 4 2 1 10 15 7 0 4

