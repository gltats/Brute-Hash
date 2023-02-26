# Brute-Hash
This script searches for an image file that matches the hash of a target image. It searches for image files in a specified directory and compares the hash of each file with the hash of the target image.

## Requirements
Python 3.x

## Usage
- Place the target image in a location on your system and note the file path.
- Place the directory containing the images you want to search through in another location and note the file path.
- Open a terminal window and navigate to the directory containing the bruteforce_hash.py file.
- Run the command python bruteforce_hash.py.
- Enter the file path of the target image when prompted.
- Enter the file path of the directory containing the images to search through when prompted.
- Wait for the script to finish running. If a matching image file is found, the script will print its file path to the console.  
  -> Example:  
      Suppose you want to find an image file that matches the hash of a target image located at /home/user/target_image.tif. You have a directory of images        located at /home/user/images that you want to search through. You would do the following:  
            - Open a terminal window and navigate to the directory containing the bruteforce_hash.py file.  
            - Run the command python bruteforce_hash.py.  
            - Enter /home/user/target_image.tif when prompted.  
            - Enter /home/user/images when prompted.  
            - Wait for the script to finish running. If a matching image file is found, the script will print its file path to the console.  

## Note
This script uses the SHA256 hash function to compare the hashes of the image files.
The script only searches for image files with the .tif extension.
If multiple image files have the same hash as the target image, the script will print the file path of the first matching image file it finds.
