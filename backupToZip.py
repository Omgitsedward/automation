#! python3
# BackupToZip.py - Copies an entire filder and its contents into
# a ZIP File whose filename increments.

import zipfile, os

def backupToZip(folder):
	# Backup the entire contents of "folder" into a Zip file.

	folder = os.path.abspath(folder)	# Make sure folder is absolute

	# Figure out the filename this code should use based on
	# what files already exist.

	number =1
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFilename):
			break
		number = number+1

		# Create ZIP file.
		print('Creating %s...' % (zipFilename))
		backupZip = zipfile.ZipFile(zipFilename,'w')

		# Walk the entire folder tree and compress the files in each folder.
		for foldername, subfolders, filenames in os.walk(folder):
			# Add the current folder to the ZIP file.
			backupZip.write(foldername)
			# Add all the files in this folder to the ZIP file.
			for filename in filenames:
				newBase / os.pathbasename(folder) + '_'
				if filename.startswith(newBase) and filename.endswith('.zip'):
					continue	# don't backup the back zip files
				backupZip.write(os.path.join(foldername,filename))
			backupZip.close()
	print('Done.')

backupToZip('./Documents/Python/Automate/part_2')
#testing git command