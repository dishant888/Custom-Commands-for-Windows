@echo off 

rem clear screen
cls

rem set current dir in a variable currentWorkingDir
set currentWorkingDir=%cd%

rem path to mapit.py
cd C:\Users\user\CustomCommands\python

rem run mapit.py %* takes all arguments passed with commands
python locate.py %*

rem redirect back to previous working directory
pushd %currentWorkingDir%