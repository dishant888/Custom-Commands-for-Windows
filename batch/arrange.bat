@echo off

rem clear screen
cls

set currentDirectory=%cd%

rem path to arrange.py
cd C:\Users\user\CustomCommands\python

rem run arrange.py and pass last working dir to it
python arrange.py %currentDirectory% %1

rem get back to previous working directory
pushd %currentDirectory%