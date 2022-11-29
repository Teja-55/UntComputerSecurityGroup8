Step 1 : Give full permissions to the source and destination folder
         chmod ugo+rwx "file name"

step 2 : create a .sh file and paste the below command 
          cp -R * Sourcepath/  destinationpath/
         save and exit

Step 3 : Scheduling the cron job
         crontab -e
         60 * * * * /bin/bash/  [path of the .sh file]
         save and exit 

To verify  the crontab entry  crontab -l 
      
             