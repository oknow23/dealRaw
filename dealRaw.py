import os
from metadata import Metadata
import sys

DBG = 0
LEAST_RATING = 4
subnameList = ['.cr2','.nef','.raw','.raf','.pef']

#get file path
if len(sys.argv) > 1:
	photoPath = sys.argv[1].decode('utf8')+'\\'
else:
	# print os.getcwd()
	photoPath = os.getcwd()+'\\'

rawPath = photoPath+"raw\\"

for fileNames in os.listdir(rawPath):
	i = 0
	for subname in subnameList:
		# print subname
		rc = fileNames.find(subname)
		if rc >= 0:
			break
		i = i+1

	if rc >= 0:
		name = fileNames.rstrip(subnameList[i])
		print '\nFind raw file:'+ name
		frc = 0
		for photoName in os.listdir(photoPath):
			rc = photoName.find(name)
			if rc >= 0:
				print photoPath+photoName
				md = Metadata.from_potential_sidecar(photoPath+photoName)
				print 'Photo Rating: '+ str(md.rating)
				if( md.rating < LEAST_RATING ):
					deletePath = rawPath + fileNames
					print 'Delete low rating file: ' + deletePath
					if DBG == 0:
						os.remove(deletePath)

				frc = 1

		#delete not exist raw file from jpeg file
		if frc == 0:
			deletePath = rawPath + fileNames
			print 'Delete not exist ' + deletePath
			if DBG == 0:
				os.remove(deletePath)
if DBG == 0:
	os.system("pause")