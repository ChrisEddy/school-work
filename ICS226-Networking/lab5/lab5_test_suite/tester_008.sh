#!/bin/bash
# Points: 1
rm -rf test_008
mkdir test_008
mkdir test_008/ics226
mkdir test_008/ics226/lab5
cp ClientB.java ServerB.java test_008/ics226/lab5

cd test_008

javac ics226/lab5/*.java

echo 'Version B Test 1: two clients to same server, + 1 2 and + 3 4'
java ics226.lab5.ServerB 31110 &
sleep 1
java ics226.lab5.ClientB localhost 31110 + 1 2
java ics226.lab5.ClientB localhost 31110 + 3 4



