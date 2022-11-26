#Install the below library
#pip install googletrans==3.1.0a0

from termcolor import colored
import os
import hashlib
from googletrans import Translator
import hmac

#generates a key for the hmac signature
os.system('head -c 256 /dev/urandom > key.bin')

#library funtion which will help us to identify if the file content is plain english or not
detector = Translator()

#target directory path (make change accordingly to your target directory)
rootdir = '/home/sec-lab/Desktop/projectfiles'

#rading the generated key
file_in = open('key.bin', 'rb')
key = file_in.read()

#funtion which help us to get signature of a given file
def get_signature(file):
    f = open(file_path, 'rb')
    bytes = f.read()
    signature = hmac.new(key, msg=bytes, digestmod=hashlib.sha256).hexdigest().upper()
    return signature

#dictionaries which will store the values of signature and file paths of all the existing files
signature_dir = {}
file_paths = {}

#Initial loop which will generate signatures of all the file and store it.
for (subdir, dirs, files) in os.walk(rootdir):
    for file in files:
        print(os.path.join(subdir, file))
        file_path = os.path.join(subdir, file)
        file_paths[file] = file_path
        signature_dir[file] = get_signature(file_path)

print('[+] Just calculated your baseline file signatures')
print('[+] Checking and securing files')

#An infinite loop which will continusly monitor the target directory and look for any possible encryption
while True:
    for (subdir, dirs, files) in os.walk(rootdir):
        for file in files:
            if(file in signature_dir):
                file_path = file_paths[file]
                current_signature = get_signature(file_path)
                
                #if the file signature at the current moment won't match with the past signature
                #then the file become suspicious
                if current_signature != signature_dir[file]:
                    content = ''
                    try:
                    	 #fetching content of the file
                        f = open(file_path, 'r')
                        lines = f.readlines()
                        for line in lines:
                            content += ' ' + line.strip()
                        
                        #using library funtion to check if the content is plain english or not
                        dec_lan = detector.detect(content)
                        
                        #if the probability of english is less than 50% than file is most probably encrypted
                        if dec_lan.confidence < 0.5:
                        
                            #rise an alert and start the mitigation process
                            print(colored('[+] ALERT High Priority - Anonymous encryption in '
                                         + file_path, 'red'))
                            print(colored('Dont worry, mitigation has been started', 'green'))
                            # metigation starts here

                        else:
                            #if the content is in English than it must be changed by the user
                            print('[+] ALERT Low Priority - Someone edited the ' + file_path)

                    except UnicodeDecodeError:
                        pass

                #At the end, updating the signatures of the dictionary with new values if any changes happened
                signature_dir[file] = current_signature
                
            else:
                #if file is not available in the dictionary than it must be a new file
                #storing the new file and its signature
                file_path = os.path.join(subdir, file)
                file_paths[file] = file_path
                signature_dir[file] = get_signature(file_path)

