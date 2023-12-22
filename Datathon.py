import os
from deepface import DeepFace
import csv

# Function to process images and extract gender, race, and age
def process_images(folder_path):
    data = []
    
    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Use DeepFace to analyze the image
        try:
            result = DeepFace.analyze(file_path)
            
            # Extract gender, race, and age
            gender = result['gender']
            race = result['race']
            age = result['age']
        except:
            # If an error occurs or data is not available, use filler values
            gender = "unknown"
            race = "unknown"
            age = -1
        
        # Append the data to the list
        data.append([filename, gender, race, age])
    
    return data

# Folder containing images (update the path accordingly)
folder_path = '/home/user/Downloads/faceimages'  # Replace '/path/to/faceimages' with the actual path

# Process images and get the data
image_data = process_images(folder_path)

# Write the data to a CSV file
output_csv = 'output.csv'
with open(output_csv, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the header row
    csv_writer.writerow(['Filename', 'Gender', 'Race/ethnicity', 'Age'])
    
    # Write the image data rows
    csv_writer.writerows(image_data)

print(f"CSV file '{output_csv}' has been created with image data.")
