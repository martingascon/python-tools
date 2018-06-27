# "The Gasconator" IS A PYTHON SCRIPT TO CALCULATE THE SIZE, CTIME AND PATH FOR EVERY FILE IN A GIVEN DISK. 
# SOME IMPORTS
import os
import pandas as pd
from datetime import datetime
from os.path import getmtime
import sys

import ntpath
ntpath.basename("a/b/c")


# FUNCTIONS TO PROCESS THE DATA
def extract_filename(fullpath):
    head, tail = ntpath.split(fullpath)
    tail.rstrip()
    return tail or ntpath.basename(head)

def extract_filepath(fullpath):
	head, tail = ntpath.split(fullpath)
 	return head.rstrip() 

def extract_extension(file):
	sp = file.split(".")
	return sp.pop().rstrip()

def getSize(fullpath):
	try:
		size = os.path.getsize(str(fullpath))
		return size/(1024*1024)
	except:
		return 0

def getCtime(fullpath):
	try:
		ctime = datetime.fromtimestamp(getmtime(fullpath)).strftime('%d/%m/%Y %H:%M')
		#time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(str(fullpath))))
		return ctime
	except:
		return 0

argc = len(sys.argv)  
 
if argc == 1:
	pwd =  ""
	proc1 = os.system('find "$PWD" -type f > list.txt')

elif argc == 2:
	pwd = sys.argv[1]
	print "SEARCHING IN THIS DIRECTORY: " + pwd
	try:		
		proc1 = os.system('find "$PWD" ' + pwd + ' -type f > list.txt')
	except:
		print " This directory is empty or there is something wrong in it."
		sys.exit()
	
else:
	print "#####################################################################################"
	print "Sorry! Wrong Number of parameters. "
	print "python ListTable.py <path>  (e.g. /Volumes/my_new_hardrive) "
	print "#####################################################################################"
	sys.exit()


print "#####################################################################################"
print "THE GASCONATOR is initializing .... please wait" 
print "#####################################################################################"
print "Generating the list of files within your harddrive ... please wait"
print "#####################################################################################"
print "You may find some files saying Permission denied  ... no worries "
print "#####################################################################################"
print "Separating file from path, calculating size and creating time, extension .. please wait"

# OPEN THE FILE LIST AND REMOVE \n characters
lines2 = [line.rstrip() for line in open('list.txt')]

# Put the full path into a panda
df2 = pd.DataFrame(lines2)

# Rename the column as FilePath
df2.columns = ["FullPath"]

# Add column into panda with only the name of the file
df2['FileName'] = [extract_filename(path) for path in df2['FullPath']]
df2['Ctime']    = [getCtime(path) for path in df2['FullPath']]
df2['FileType'] = [extract_extension(path) for path in df2['FileName']]
df2['FileSize_MB'] = [getSize(path) for path in df2['FullPath']]
df2['FilePath'] = [extract_filepath(path) for path in df2['FullPath']]

# REMOVE THE COLUMN FULLPATH, WE DON'T USE IT ANYMORE
df2 = df2.drop(['FullPath'], axis=1)

# SORT FILES BY SIZE
df2 = df2.sort_values(by=['FileSize_MB'], ascending=False)

print "#####################################################################################"
print "WRITING RESULTS INTO A FILE (WHATYOUWANT.CSV)  .... please wait"

# WRITE PANDAS TO FILE
df2.to_csv('WhatYouWant.csv', index = False)

# DELETE THE LIST FILE
proc2 = os.system('rm -rf list.txt')

# Print the header
# print(df2.head(1))

print "TOTAL SIZE FOR ALL FILES IN THIS DIRECTORY: " + str(df2['FileSize_MB'].sum()/1024) + " GB"
print "Done! "
print "#####################################################################################"
