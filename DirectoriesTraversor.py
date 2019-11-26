#!usr/bin/python3

import sys
import os
import stat
from datetime import date

# for printing arguments help and available options for users
import optparse

# for coloring the terminal
from termcolor import cprint


'''
Description: This tool is part of my Python digital forensics toolset. It travers directories and specifies
file properties including permissions, creation/Access/Modified times
Requirements: Install datetime by pip install datetime
              Install termcolor by pip install termcolor
       
Usage: python DirectoriesTraversor.py -p .

Dr. Hussein Bakri
Enjoy!
'''

def main():
   parser = optparse.OptionParser('Usage of the program: ' + '-p <path>')
   parser.add_option('-p', '--path', dest='targetPath', type='string', help='Specify a target path directory')

   (options, args) = parser.parse_args()
   targetPath = options.targetPath  # taking the targetPath
   
   if (options.targetPath == None):
      parser.print_help()
      exit(0)
   scan_directory(targetPath)
 

def scan_directory(directory):
   dash = '-' * 106
   print(dash)   
   print('{:<40s}{:<15s}{:<10s}{:<15s}{:<15s}{:<15s}'.format('Folder/File','Permissions', 'Size', 'Accessed', 'Modified', 'Created'))
   print(dash)   

   with os.scandir(directory) as iterator_path:
      for path in iterator_path:
         CurrentItem = path.name
         # print(path.name)
         # print(os.stat(path.name))
         # print(os.stat(path.name).st_mode)
         Permissions = os.stat(CurrentItem).st_mode
         st_ino = os.stat(CurrentItem).st_ino
         st_dev = os.stat(CurrentItem).st_dev
         st_nlink = os.stat(CurrentItem).st_nlink
         st_uid = os.stat(CurrentItem).st_uid
         st_gid = os.stat(CurrentItem).st_gid
         size = os.stat(CurrentItem).st_size
         AccessedTime = date.fromtimestamp(os.stat(CurrentItem).st_atime)
         ModifiedTime =  date.fromtimestamp(os.stat(CurrentItem).st_mtime)
         CreatedTime =  date.fromtimestamp(os.stat(CurrentItem).st_ctime)

         # Variable that stores how to show the CurrentItem if Directory append / at the end
         if(os.path.isdir(CurrentItem)):
            CurrentItemPrinted = (CurrentItem + "/").strip()
            cprint('{:<40s}{:<15s}{:<10s}{:<15s}{:<15s}{:<15s}'.format(CurrentItemPrinted, stat.filemode(Permissions), str(size), str(AccessedTime), str(ModifiedTime), str(CreatedTime)))

         if(os.path.isfile(CurrentItem)):
            cprint('{:<40s}{:<15s}{:<10s}{:<15s}{:<15s}{:<15s}'.format(CurrentItem, stat.filemode(Permissions), str(size), str(AccessedTime), str(ModifiedTime), str(CreatedTime)),'green')
         

main()
