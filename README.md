# DigitalForensicsToolset
A toolset of Digital Forensics Tools written in Python 3.

## Tool 1 - DirectoriesTraversor.py

It lists all the directories and the files in a path with their properties including permissions, size, creation/access/modification dates & times and then prints the result in a nice table. I will add later more properties covering more file's metadata.

### Requirements
You need to make sure you install **all** the python modules required by the tool. Per example to install datetime:

``` pip install datetime```

### Usage
To list the current directory's files & sub-directories, you can say:

```python DirectoriesTraversor.py -p .```

or for a certain path:

```python DirectoriesTraversor.py -p C:\```

### Future Improvements
* Fix the tool to show dates and times
* Add more metadata such as exif

## Tool 2 - WindowsRegistryScanner.py

It enumerates all the MS Windows Registry keys under a certain registry key (i.e. all subkeys). It can also query the value of a specific registry key.

### Requirements
You need to make sure you install **all** the python modules required by the tool. Per example to install datetime:

``` pip install datetime```

### Usage
***For enumeration:***

```python WindowsRegistryScanner.py -e 'Software\Microsoft\Windows\CurrentVersion\'```

***For Querying:***

```python WindowsRegistryScanner.py -q 'SOFTWARE\Microsoft\Windows\CurrentVersion\Run' Maliciouskey```

**List of common MS Windows autorun locations to look for any malicious activity**

```
Software\Microsoft\Windows\CurrentVersion\Runonce
Software\Microsoft\Windows\CurrentVersion\policies\Explorer\Run
Software\Microsoft\Windows\CurrentVersion\Run
Software\Microsoft\Windows NT\CurrentVersion\Windows\Run
Software\Microsoft\Windows\CurrentVersion\Run
Software\Microsoft\Windows\CurrentVersion\RunOnce
```
### Future Improvements
* No ideas at the moment

## Tool 3 - hasher.py
It calculates the sha1 hash value of any given file. It then prints the hash and store it in a file with .sha1 extension. It also compares hashes to make sure that the file was not tempered with. This is an essential tool to make sure that the correct chain of custody of digital evidence is adopted.

### Requirements
You need to make sure you install **all** the python modules required by the tool. Per example to install colorterm:

``` pip install colorterm```

### Usage
**Usage 1:** 

* Calculating the hash of the file given, printing it & then storing it in a file with the same filename & with an .sha1 extension

```python hasher.py file.txt```

**Usage 2:** 

* Giving the Hex sha1 hash directly in the terminal to the tool for comparision purpose

```python hasher.py file.txt -c 94bcd8d0e86d4d6f0517c9e80c82b47dc6fe3707```

**Usage 3:**

* Comparing the hash of a given file to a hash stored in a .sha1 extension file. You can use both -c and --compare.

```python hasher.py file.txt -c file.sha1```

or 

```python hasher.py file.txt --compare file.sha1```

### Future Improvements
* No ideas at the moment

# Packaging all the digital forensics tools in this repository as executables
It is recommended to package all the forensics tools as executables. It does not make sense to install python modules on the target machine. If you actually do this: the resulting digital evidence is considered ***tampered with thus inadmissible to courts.*** 

You need the Python module pyinstaller. You can install it via pip or pip3 or via apt package manager.

```pip install pyinstaller```

A program called pyinstaller is installed in the Python directory. On Windows, it would be the executable: pyinstaller.exe

To create an executable of your tool, you can issue the following command. **PS: change "forensics_tool_name.py" with the corresponding tool name**

```
pyinstaller forensics_tool_name.py --onefile
```

--onefile means pyinstaller will package all the python files into a single executable. This is usually important especially when there are many python files. On Windows per example, your .exe file will be found in the dist folder.

## Create a Windows .exe executable out of a python project from a Linux OS/Mac OS
As you probably know that in order to run a Windows .exe or .msi or anything similar on a Linux OS or a Mac OS, you need a program called wine. I would assume you have installed wine on Linux or MacOS. Go to the official Python Website and download the right Python 2.7.x msi installation file or Python 3.x.x version you need. At this moment in time (2018-2019), there is no concern anymore about Python 2.7.x versions since Python2 is deprecated. Navigate on your Linux to the directory of the download folder of this file and then run the following command: (/i is for installing) - X.X.X is the version you want to install:

```wine msiexec /i python-X.X.X.msi```

You will get a normal installation process as you would have on any MS Windows OS. Please follow the instructions to install the Python interpreter. All Programs that are installed in wine, are located in a hidden folder called '.wine' in the Home Folder of the user. So probably your Windows Python will be installed in per example: ~/.wine/drive_c/Python27/ and in there you will find all the executables that are normally installed such as Python.exe, pip.exe .... Navigate to this folder and run via wine the Python interpreter invoking pip in order for you to install as above the 'pyinstaller' module.

**NB: wine does not and can not by default access the pip modules of the Linux OS so this why you need to do this.

```
cd ~/.wine/drive_c/Python27/

wine python.exe -m pip install pyinstaller
```

After the installation of the module completes, you will find the pyinstalller.exe in the Scripts directory. To install pynput - please  issue the following commands: **NB:** why? as I have mentioned before, you need to do that since even if this module is installed on the Linux OS level, the Windows Python interpreter of wine can not access OS-level Python modules

```
wine python.exe -m pip install pynput
```

You can then package your tool into a single executable:

```
wine /root/.wine/drive_c/Python27/Scripts/pyinstaller.exe forensics_tool_name.py --onefile
```

The binary will be stored in the dist folder.

## Creating a Mac OS executable
If you are on a Mac OS, the process is similar to installing 'pyinstaller'. First install pyinstaller through latest pip - with sudo privileges. **NB: it is better to get the latest pip so to avoid errors.**

```
sudo pip install pyinstaller
```

Then run pyinstaller on the python file

```
pyinstaller forensics_tool_name.py --onefile --noconsole
```

The binary will be stored in the dist folder.

## Creating a Linux OS executable
The process is exactly similar. In Linux, resulting binaries should be run from the terminal after chmod +x makes them executable.

# Digital evidence chain of custody
* Do not forget to follow the correct guidelines for digital evidence **chain of custody** so that your evidence is admissible in legal courts
* Do not forget to create hashes for all your images, files, memory dumps etc...
* Always be an impartial and a very meticulous examiner whether you are working for the prosecution or for the defendant team

# License
This program is licensed under MIT License - you are free to distribute, change, enhance and include any of the code of this application in your tools. I only expect adequate attribution and citation of this work. The attribution should include the title of the program, the author (me!) and the site or the document where the program is taken from.
