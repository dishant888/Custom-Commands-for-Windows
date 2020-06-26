# This program arranges or group files based on their extensions
import sys
import os
import shutil

def createFolderAndMove(folder,files,arrangeByExt = True):
	cd = os.getcwd()
	# check if folder is not false because getExtension returns False
	if folder:
		# create folder if not exists
		if not os.path.exists(folder):
			os.makedirs(folder)

		# move files into folder
		for file in files:
			if arrangeByExt:
				if getExtension(file) == folder:
						os.rename(cd + '\\' + file, cd + '\\' + folder + '\\'+file)
			else:
				os.rename(cd + '\\' + file, cd + '\\' + folder + '\\'+file)


		
getExtension = lambda file: os.path.splitext(file)[1][1:] if os.path.isfile(file) else False

def arrangeByExt():

	# change dir to last working dir
	os.chdir(sys.argv[1])

	# get all files of current directory in directory variable
	files = list(os.listdir())
	# print(files)

	# lambda function to get extension from files

	# folder contains all folders to be created
	folders = set(map(getExtension, files))
	for i in os.listdir():
		if os.path.isdir(i):
			folders.add(i)
	# print('\n',folders)
	for folder in folders:
		createFolderAndMove(folder,files)

def arrangeByGroup():
	# change dir to last working dir
	os.chdir(sys.argv[1])

	# get all images of current directory in directory variable
	imageExt = ['.jpg','.jpeg','.png','.gif']
	docExt = ['.xlsx','.docx','.doc','.txt','.ppt','.pdf']
	mediaExt = ['.mp3','.mp4']

	images = []
	docs = []
	medias = []
	others = []

	for file in os.listdir():
		ext = os.path.splitext(file)[1]
		if ext in imageExt: images.append(file)
		elif ext in docExt: docs.append(file)
		elif ext in mediaExt: medias.append(file)
		else: others.append(file)
	# print(images)
	# print(docs)
	# print(medias)
	# print(others)
	createFolderAndMove('Images',images,False)
	createFolderAndMove('Docs',docs,False)
	createFolderAndMove('Medias',medias,False)
	createFolderAndMove('Others',others,False)


if __name__ == '__main__':
	# print(sys.argv[2])
	try:
		if sys.argv[2] == '--by-ext':
			arrangeByExt()

		if sys.argv[2] == '--by-grp':
			arrangeByGroup()

	except IndexError:
		print('Error: Try arrange --by-ext or arrange --by-grp')
