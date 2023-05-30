# README

## Welcome!
I lost instagram followers after posting a photo of my dog and was offended,
so I wrote this quick script to find out which of the accounts that I follow
don't follow me back!

This script, like so many great softwares, is a product of laziness and pettiness :^) ♡

## You can use this too!
1. On the instagram app, click on the three bars in the top right corner of your profile page  
2. Click on "Your activity"
3. Scroll to the bottom and select "Download your information"
4. Click on "Request a download"
5. Click on "Select types of information" 
6. Pick whatever you want, and make sure that you select "Followers and following" at some point. 
7. Change the format to "JSON"
8. Change the "Media quality" to Low (I think it will speed up the process a bit)
9. Submit the request
10. In a few days, check the ""Request a download" tab again and you'll have the option to download a zip file with all of the data that you requested. 
11. Copy the two json files with the information about the accounts that you follow and the accounts that follow you into the folder with the "who_to_remove.py" and "name_of_files.txt" files from this repo. 
12. Go into the name_of_files.txt and replace the **1st line** of the name_of_files.txt file with the name of the json file that includes the accounts that you follow and **4th line** with the name of the json file that includes the accounts that follow you. 
    - INCLUDE the .json at the end of the file names 
    - DO NOT add any spaces after the titles
    - DO NOT add any extra lines anywhere 
    - DO NOT add any extra punctuation in the file names