# DigitalForensicsToolset
A toolset of Digital Forensics Tools written in Python 3.

## Tool 1 - DirectoriesTraversor.py

It list all the directories and files with their properties including permissions, size creation/Access/Modified times and print the result in a nice tabular way. I will add more properties covering more file metadata later.

### Requirements
You need to make sure you install **all** the python modules needed by the tool. Per example to install datetime:

``` pip install datetime```

### Usage
To list/traverse current directory you can say:
```python DirectoriesTraversor.py -p .```

or for a certain path:
```python DirectoriesTraversor.py -p C:\```

## Tool 2 - WindowsRegistryScanner.py

It enumerates all the MS Windows Registry under a certain registry key (i.e. all subkeys). It can also query the value of a specific registry key.

### Requirements
You need to make sure you install **all** the python modules needed by the tool. Per example to install datetime:
``` pip install datetime```

### Usage
***For enumeration:***

```python WindowsRegistryScanner.py -e 'Software\Microsoft\Windows\CurrentVersion\'```

***For Querying:***

```python WindowsRegistryScanner.py -q 'SOFTWARE\Microsoft\Windows\CurrentVersion\Run' Maliciouskey```

**List of common autorun locations:**
```
Software\Microsoft\Windows\CurrentVersion\Runonce
Software\Microsoft\Windows\CurrentVersion\policies\Explorer\Run
Software\Microsoft\Windows\CurrentVersion\Run
Software\Microsoft\Windows NT\CurrentVersion\Windows\Run
Software\Microsoft\Windows\CurrentVersion\Run
Software\Microsoft\Windows\CurrentVersion\RunOnce
```

## Packaging all the digital forensics tools as executables
It is recommended to package all the forensics tools as executable. It does not make sense to install python modules on the target machine. Actually if you do not do that it is considered tempering with the machine which makes any digital evidence you collect inadmissible in courts. LOL!     


# License
This program is licensed under MIT License - you are free to distribute, change, enhance and include any of the code of this application in your tools. I only expect adequate attribution and citation of this work. The attribution should include the title of the program, the author (me!) and the site or the document where the program is taken from.
