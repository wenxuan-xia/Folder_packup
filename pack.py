import os
import sys
import zipfile

path_read = open("path.txt", "r")
path = path_read.readline()
path_read.close()

os.chdir(path)

for i in os.listdir('.'):
	if os.path.isdir(i):
		f = zipfile.ZipFile(i + ".zip", 'w', zipfile.ZIP_DEFLATED)
		for dirpath, dirnames, filenames in os.walk(i):
			for filename in filenames:
				f.write(os.path.join(dirpath,filename))
		f.close();
		print(path + "\\" + i + ".zip ---- finish")

os.system("pause")

