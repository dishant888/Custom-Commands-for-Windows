@echo off 

rem clear screen
cls

rem set current dir in a variable currentWorkingDir
set currentWorkingDir=%cd%

rem path to directions.py
cd C:\Users\user\CustomCommands\python

rem run directions.py %* takes all arguments passed with commands
python directions.py %*

rem redirect back to previous working directory
pushd %currentWorkingDir%