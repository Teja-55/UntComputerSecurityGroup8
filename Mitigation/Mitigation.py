import os
import sys

paths = ["/root/rk031734/python/testdir", "/root/rk031734/python/testdir2"]
def deleteProcesses(filePath):
   print("\nFile Path:", filePath)
   com = "for proc in $(lsof -t " + filePath + "); do echo 'Killing process : '$proc; kill $proc; done"
   print(com)
   os.system(com)
   print("\nKilled")
  
for path in paths:
   deleteProcesses(path)