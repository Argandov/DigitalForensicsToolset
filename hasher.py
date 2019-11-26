#!usr/bin/python3

import sys
import os

import io

# for printing arguments help and available options for users
import argparse

from termcolor import cprint

import hashlib

'''
Description: This tool is part of my Python digital forensics toolkit. It calculates the sha1 hash value
of any file given, it then prints the hash and store the latter in a file with .sha1 extension. It also compares hashes to make
sure files were not tempered with. This tool is very essential to make sure that the correct chain of custody of digital
evidence is adopted.

Usage 1: 
-------
* Calculating the hash of the file given, printing it & then storing it in a file with the same filename & .sha1 extension

python hasher.py file.txt

Usage 2: 
-------
* Giving the Hex sha1 hash directly in the terminal for comparision

python hasher.py file.txt -c 94bcd8d0e86d4d6f0517c9e80c82b47dc6fe3707

Usage 3:
--------
* Comparing the has of a given file to a hash stored in a .sha1 extension

python hasher.py file.txt -c file.sha1

or 

python hasher.py file.txt --compare file.sha1

Do not forget to follow the correct guidelines for digital evidence chain of custody so that your evidence is admissible in legal courts
Do not forget to create hash sums for all your images, files, memory dumps etc...

Dr. Hussein Bakri
Enjoy!
'''
class HashClass:
	"""
	A class that contains the functionlity for hashing files for digital forensics purposes:
	
	Class Methods: 
	1) getArguments() to retrieve terminal arguments
	2) open_hash() return the textual representation of the hash - to handle the case where the hash is in a file
	3) compare_hashes() - compare two hashes (one calculated from a file) and one either given directly or via a file
	4) hash_file() - calculates the hash using the sha1() algorithm
	5) main() - logic starts here
	"""

	def __init__(self):
		super(HashClass, self).__init__()
		self.path = None

	@staticmethod
	def getArguments():
		parser = argparse.ArgumentParser(description="Scan all magic files")
		parser.add_argument('path', help="Path to top level directory")
		parser.add_argument('-c', '--compare', help="Provide a hash or hashes to in addition to a file to compare")
		return parser.parse_args()
		

	def open_hash(self, hash_string_or_path):
		'''
		This function opens a text file containing the hexadecimal hash such as 'file.sha1'/file.txt 
		or receives a string representation of a hash
		'''
		digest_hash = hash_string_or_path

		if os.path.isfile(hash_string_or_path):
			with open(hash_string_or_path, 'r') as f:
				# splitline() is used to split the lines at line boundaries without returning them
				hash_text = f.read().splitlines()[0]	#get me first line
				digest_hash = hash_text
		return digest_hash

	def compare_hashes(self, old_hash, new_hash):
		'''
		This function compares the hashes.
		'''
		if old_hash == new_hash:
			cprint("The hashes match: {}".format(old_hash), 'green')
		else:
			cprint("Your two hashes do not match!!! \nThe Hash to compare with: {0}\nActual Hash of your file: {1}".format(old_hash, new_hash),'red')

	def hash_file(self, file):
		# Buffer size in Bytes
		# "Enabling buffering means that you're not directly interfacing with the OS's representation of a file, or its file system API"
		BUFFER_SIZE = 65536

		THE_DEFAULT_BUFFER_SIZE = io.DEFAULT_BUFFER_SIZE

		# Possible Hash Algorithms: sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), blake2s() and md5()
		digest_alg = hashlib.sha1()

		cprint("Calculating the hash of your file....", 'green')
		# rb means read the file in bytes
		with open(file, 'rb') as f:
			while True:
				# Splitting all the data of the file into chuncks equal to the BUFFER_SIZE
				data_chunk = f.read(BUFFER_SIZE)
				if not data_chunk:
					break
				
				# Updating the master digest by hashing the consecutive chunks of data
				digest_alg.update(data_chunk)
		
		# hexdigest() calculates the final digest of the data passed to the update() method so far
		# & returns it as a string containing only hexadecimal digits
		Calculated_hash = digest_alg.hexdigest()
		return Calculated_hash

	def main(self):
		arguments = self.getArguments()
		self.path = arguments.path
		filename = os.path.basename(self.path).split('.')[0]

		# Hash the file that the user has gave us in the argument
		new_calculated_hash = self.hash_file(self.path)

		if arguments.compare:	# if user chose also the argument compare
			old_hash = self.open_hash(arguments.compare)
			self.compare_hashes(old_hash, new_calculated_hash)
		else:
			cprint('The calculated hash is: {}'.format(new_calculated_hash), 'green')
			with open(filename +'.sha1', 'w') as writer:
				writer.write(new_calculated_hash)
				cprint('Stored your calculated hash in file: {}.sha1'.format(filename), 'green')

        

if __name__ == '__main__':
	hash_instance = HashClass()
	hash_instance.main()
