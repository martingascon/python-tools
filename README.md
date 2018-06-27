# python-tools

ListTable.py is a python script to create a list with the size, path, and creation time of all the files in a single directory. The output file is a comma separated file sorted by size and contains the following fields:

* FileName (file name)
* Ctime (creation time)
* FileType (file extension: e.g. exe, mp3, jpg)
* FileSize_MB (file size in MB)
* FilePath (path to the file)

## usage:

python ListTable.py <directory>
  
## examples:
a) python ListTable 
(will run in this directory)

b) python ListTable /Volumes/my_hard_drive
(will run in this directory)

If you have any question, please contact me. 
