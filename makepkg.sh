#!/usr/bin/env bash

PROJECT="uWebScan"
PROJECTVR=$(cat uWebScan.py | grep "VERSION = " | awk -F" = " '{ print $2 }' | sed s/\"//g)

echo -n "Creating package: "
echo $PROJECT $PROJECTVR
echo 
mkdir ../$PROJECT-$PROJECTVR
cp -R *.py ../$PROJECT-$PROJECTVR  
mkdir ../$PROJECT-$PROJECTVR/uws
cp -R uws/*.py ../$PROJECT-$PROJECTVR/uws
cd ..
tar -czf $PROJECT-$PROJECTVR.tar.gz $PROJECT-$PROJECTVR
zip -r -9 -q $PROJECT-$PROJECTVR.zip $PROJECT-$PROJECTVR

rm -rf $PROJECT-$PROJECTVR

echo 
echo All Done!
