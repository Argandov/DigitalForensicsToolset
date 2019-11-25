#!usr/bin/python3

import sys
import os
import winreg
from datetime import date

# for printing arguments help and available options for users
import argparse


'''
Description: This simple tool is part of my Python digital forensic toolkit. It enumerates all the MS Windows Registry under a
certain registry key (i.e. all subkeys). It can also query the value of a specific registry key
Requirements: Install datetime by pip install datetime

Usage: 
-----
For enumeration: 
python WindowsRegistryScanner.py -e 'Software\Microsoft\Windows\CurrentVersion\'

For Querying:
python WindowsRegistryScanner.py -q 'SOFTWARE\Microsoft\Windows\CurrentVersion\Run' Maliciouskey

Dr. Hussein Bakri
Enjoy!
'''

# SOFTWARE\Microsoft\Windows\CurrentVersion\
# List of common autorun locations:
# Software\Microsoft\Windows\CurrentVersion\Runonce
# Software\Microsoft\Windows\CurrentVersion\policies\Explorer\Run
# Software\Microsoft\Windows\CurrentVersion\Run
# Software\Microsoft\Windows NT\CurrentVersion\Windows\Run
# Software\Microsoft\Windows\CurrentVersion\Run
# Software\Microsoft\Windows\CurrentVersion\RunOnce

def main():
	parser = argparse.ArgumentParser(description="MS Windows Registry Scanner Tool")
	parser.add_argument('-e', '--enumerate', type=str, help="Enumerate all keys in the registry")
	parser.add_argument('-q', '--query', nargs=2, help="Query Registry Values")
	args = parser.parse_args()

	# Set the hive to HKEY_CURRENT_USER
	hive = winreg.HKEY_CURRENT_USER

	if args.enumerate:
		enumerate(hive, args.enumerate)

	if args.query:
		query(hive, args.query[0], args.query[1])

def enumerate(hive, registry_path):
	try:

		# Open the registry key, returning a handle object
		registry_key = winreg.OpenKey(hive, registry_path, 0, winreg.KEY_READ)
		print(registry_key)
		if(registry_key==None):
			
			sys.exit("==KEY DOES NOT EXIST==")

		# Enumerate all subkeys 
		i=0
		while True:


			# Enumerates subkeys of an open registry key, returning a string
			value = winreg.EnumKey(registry_key, i)
			print(value)
			i+=1

	except OSError:
		print("====END====")

	except  (FileNotFoundError, UnboundLocalError):
		print("==DOES NOT EXIST==")
		
	finally:
		# Closes the opened registry key
		winreg.CloseKey(registry_key)

	

def query(hive, registry_path, value_name):
	try:
		# Open the registry key, returning a handle object
		registry_key = winreg.OpenKey(hive, registry_path, 0, winreg.KEY_READ)

		# Retrieves the type and data for a specified value name associated with an open registry key.
		value = winreg.QueryValueEx(registry_key, value_name)

		print(value)

	except WindowsError as e:
		print("Error loading key: " + e)
	finally:
		# Closes the opened registry key
		winreg.CloseKey(registry_key)


main()
