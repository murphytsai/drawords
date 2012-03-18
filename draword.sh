#!/bin/sh
# ./draword.sh alphabet

wordfile='word.txt'
match=$1
allchars='abcdefghijklmnopqrstuvwxyz'
notmatch=`echo $allchars | tr -d [$match]`
possible=`cat $wordfile | grep [$match] | grep -v [$notmatch]`

echo 'Possible Words:' 
echo $possible;
echo ''

