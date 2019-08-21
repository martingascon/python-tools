# Gasconator (ListTable.py)

ListTable.py is a python script to create a list with the size, path, and creation time of all the files in a single directory. The output file is a comma separated file sorted by size and contains the following fields:

* FileName (file name)
* Ctime (creation time)
* FileType (file extension: e.g. exe, mp3, jpg)
* FileSize_MB (file size in MB)
* FilePath (path to the file)

## usage:

HOW TO USE THE GASCONATOR Python Tool for Hard Drive Inventory in 10 (maybe) easy steps:

1) For Mac OSX, make sure you have "Homebrew" installed in your Terminal. The Homebrew project page gives complete instructions on installation: https://brew.sh/

2) Open your Terminal application and install Python. Use the command: 

$ brew install python   

python ListTable.py <directory>

![Image1](/image1.png)

3) The GASCONATOR script requires that you install Pandas. To do so, you need to install a few other dependencies--this will ENTIRELY depend on your Mac computer, the version of OSX you are using, etc., so there may be extra steps required (not outlined, here). You will need "pip" to install Pandas.

3-A) Hopefully, all you will need to do is:  Download the get-pip file

$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py (and hit "Enter")

3-B) Now run this file to install pip

$ python get-pip.py    (and hit "Enter." That should get you "pip") 

3-C) Now, install Pandas: 

$ pip install pandas    (and hit "Enter." It will look like this)

![Image1](/image2.png)

4) Navigate to the WET Labs Mexico GitHub page: https://github.com/WETlabsmexico

5) Click on the "python-tools" Repository: https://github.com/WETlabsmexico/python-tools

6) Select the "RAW" version of the GASCONATOR tool, called "ListTable.py" (https://raw.githubusercontent.com/WETlabsmexico/python-tools/master/ListTable.py)

7) Right-click and save the GASCONATOR code to a folder on your computer. It can be anywhere, but you need to remember where! For example, in your home hard drive in a new folder you make called "Python": /Volumes/Tzutzu-Home/Python  . When you right-click to save the file, save the file as "ListTable.py" (it should automatically save as this...). 
***Now you have a local copy of the GASCONATOR python script that you can use Terminal to run on any hard drive you want.

8) To run the GASCONATOR script, you need to "call directory" so that your Terminal is looking in the correct folder for the python script you want to use (remember, the one you just downloaded, called "ListTable.py"?). To do so, type: $ cd then drag the folder "Python" into Terminal, and hit "Enter." It will look something like this:

![Image1](/image3.png)

Nothing will really happen, and you will get the $ prompt and the flashing cursor, which is the indicator that you are now "inside" that folder.

9) Next, type: python ListTable.py  and drag the Hard Drive you want to analyze (in this example, the Hard Drive is called "Crucial") into the Terminal. It will look like this:

![Image1](/image4.png)

10) Hit "Enter." It should work! Your resulting Excel inventory should appear in the same folder where your "ListTable.py" script is located.

# examples:
a) python ListTable (will run in this directory)

b) python ListTable /Volumes/my_hard_drive (will run in this directory)

If you have any question, please contact me.
