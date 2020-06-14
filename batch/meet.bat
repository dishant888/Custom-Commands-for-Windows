@echo off

rem clear screen
cls

rem set current dir in a variable currentWorkingDir
set currentWorkingDir=%cd%

rem path to meet.py
cd C:\Users\user\CustomCommands\python rem EDIT THIS LINE

rem run mapit.py %* takes all arguments passed with commands
python meet.py %*

rem pause
rem redirect back to previous working directory
pushd %currentWorkingDir%