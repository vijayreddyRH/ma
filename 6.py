file_name = input("Enter the file name (e.g., myfile.txt): ")
try:
 # Open the file in read mode
 with open(file_name, 'r') as file:
 # Read all the lines into a list
 lines = file.readlines()
 # Get the number of lines to display from the user
 num_lines = int(input("Enter the number of lines to display: "))
 # Display the first N lines
 for line in lines[:num_lines]:
 print(line.strip())
except FileNotFoundError:
 print("File not found. Please make sure the file exists in the specified path.")


 #####################


 import zipfile
import os
# Get the folder path from the user
folder_path = input("Enter the folder path to zip: ")
# Get the ZIP file name from the user
zip_file_name = input("Enter the name of the ZIP file to create: ")
try:
 # Create a new ZIP file
 with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
 # Walk through each file in the folder
 for root, _, files in os.walk(folder_path):
 for file in files:
 # Get the absolute path of the file
 file_path = os.path.join(root, file)
 # Add the file to the ZIP archive
 zipf.write(file_path, arcname=file)
 print(f"The folder '{folder_path}' has been securely zipped into the file '{zip_file_name}'.")
except FileNotFoundError:
 print("Folder not found. Please make sure the folder exists in the specified path.")

