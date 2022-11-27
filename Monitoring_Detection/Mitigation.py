import os
import sys

#paths = "/media/sf_Ransomware_Group8/Action/Victim_machine/Imp"
def deleteProcesses(filePath):
   print("\nFile Path:", filePath)
   com = "for proc in $(lsof -t " + filePath + "); do echo 'Killing process : '$proc; kill $proc; done"
   print(com)
   os.system(com)
   print("\nKilled")
  
#deleteProcesses(paths)
