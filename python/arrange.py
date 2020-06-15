import sys
import os
import shutil

def start():
	# change directory to last working dir
	os.chdir(sys.argv[1])

	# save list of items in directory in dirItems
	dirItems = list(os.listdir())
	# print(dirItems)

	# create empty set
	folders = set()

	# save extensions in set (folder)
	for i in dirItems:
		# print(os.path.splitext(i))
		# get extension from filename
		ext = os.path.splitext(i)[1][1:]
		folders.add(ext)
	# print(folders)

	# create folder for each extension
	currentWorkingDirectory = os.getcwd()

	for folderName in folders:

		path = currentWorkingDirectory +'\\'+ folderName
		try:
			# create directory
			print(f'\nCreating directory for {folderName} files......')
			os.mkdir(path,755)
		except Exception as e:
			print(f'Error: {e}')
		finally:
			# move file into directory
			for file in dirItems:
				if os.path.splitext(file)[1][1:] == folderName:
					print(f'\nMoving {file} from {currentWorkingDirectory} to {path}')
					shutil.move(currentWorkingDirectory +'\\'+ file, path +'\\')
			print('\n\nOperation Successfull....')

if __name__ == '__main__':
	start()