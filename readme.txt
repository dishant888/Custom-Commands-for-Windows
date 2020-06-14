#############################################################

Automate small and common tasks with python for windows

#############################################################

For getting started follow the given steps

1: Setting up path in Environment variable (Windows 10)

	1.1: Right click on This PC icon and select properties
	2.1: Select Advance system settings
	3.1: Click on Environment Variables button on the bottom
	4.1: Under User variables section select path then click on edit
	5.1: Click on new
	6.1: Enter PATH_TO \CustomCommands\batch

2: Downloading the Chrome Driver

	2.1: Goto https://chromedriver.chromium.org/downloads
	2.2: Download only that version of chrome driver that matches your google chrome version

	NOTE: To check version of google chrome; open google chrome and type chrome://version/ in the url box, chrome version will be given on first line, download the same version of chrome driver

	2.3: Extract the downloaded file at any location of your choice


#############################################################

Commands:

1: locate

	go to CustomCommands\batch\locate.bat
	you have to change the path mentioned on line no 10

	Working:
		This command will locate any location on google maps
		Eg command: locate new delhi

2: meet
	
	go to CustomCommands\batch\meet.bat
	you have to change the path mentioned on line no 10

	go to CustomCommands\python\meet.py
	you have to change path mentioned on line no 15 to google chrome profile path,
	to get the profile path open google chrome and type chrome://version in the url box,
	then search for Profile Path copy that path and paste it on line no 15

	after that change executable_path on line no 45 to path where chrome driver is installed

	then create credentials.py in CustomCommands/python and add your,
	email id and password in variables named email and password

	Working:
		This command will log you in your google account and then create a googlle meeting
		and send the meeting invation on whatsapp
		Eg command: meet <contact name>

#############################################################