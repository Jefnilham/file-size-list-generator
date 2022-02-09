# file-size-list-generator

A simple script to enumerate file directories and then sort the files from largest to smallest.
This script was made to simplify the user in managing files especially deleting large unwanted files.

I tested for the expected output using the tree command on windows cmd with a pre-made folder named 'C:\walktest':

![image](https://user-images.githubusercontent.com/39832806/147817410-732803eb-e4aa-4425-aa6b-7806821b727d.png)


output of script:

![image](https://user-images.githubusercontent.com/39832806/147817047-147201bc-23eb-4ba4-83e6-6695b793c5d8.png)


The script lists all files correctly (not folders) with the size accurate to bytes.
The chosen filepath in the output can then be easily used as a search term to quickly get to the file for deletion.

# sort by file size according to given filepath.py

- Improved on the formatting so that it is easier to read.
- Improved on removing redundant repeated given file path by slicing it out. Makes it clear to users that it is a subfolder or subsubfolder or a file within that folder.
For example, we can see that there is a subfolder 'Captures' within this 'Videos' folder below and the rest of the files that do not have 'Captures' are files in the 'Videos' folder.
- changed units to MB for easier use
![image](https://user-images.githubusercontent.com/39832806/153185853-ed08ad1f-38f1-4ebe-aa37-28cad0a3d0ae.png)
