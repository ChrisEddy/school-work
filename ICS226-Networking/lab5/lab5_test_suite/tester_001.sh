#!/bin/bash
# Points: 1
rm -rf test_001
mkdir test_001
mkdir test_001/ics226
mkdir test_001/ics226/lab5
cp ClientA.java ServerA.java test_001/ics226/lab5

cd test_001

javac ics226/lab5/*.java

echo 'Version A Test 1: two clients to same server, + 1 2 and + 3 4'
java ics226.lab5.ServerA 21110 &
sleep 1
java ics226.lab5.ClientA localhost 21110 + 1 2
java ics226.lab5.ClientA localhost 21110 + 3 4



