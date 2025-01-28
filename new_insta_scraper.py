#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install instaloader


# In[ ]:


import instaloader
import os
import pandas as pd

def extract_metadata(username, output_directory):
    # Create an instance of Instaloader class
    loader = instaloader.Instaloader()

    try:
        # Retrieve the profile of the provided username
        profile = instaloader.Profile.from_username(loader.context, username)

        # Create a list to store metadata
        metadata_list = []

        # Iterate over the posts of the profile
        for post in profile.get_posts():
            # Download the media (images and videos) associated with the post
            loader.download_post(post, target=output_directory)

            # Extract metadata
            metadata = {
                "Post URL": post.url,
                "Caption": post.caption,
                "Likes": post.likes,
                "Comments": post.comments,
                "Timestamp": post.date_utc
            }
            metadata_list.append(metadata)
        
        # Convert metadata list to DataFrame
        metadata_df = pd.DataFrame(metadata_list)

        # Save metadata to CSV file
        metadata_csv_path = os.path.join(output_directory, f"{profile.username}_Final.csv")
        metadata_df.to_csv(metadata_csv_path, index=False)

        print("Metadata extraction completed. CSV file saved at:", metadata_csv_path)
    
    except instaloader.exceptions.ProfileNotExistsException:
        print("Error: Profile does not exist.")

if __name__ == "__main__":
    # Instagram username
    username = "travelrealindia"      #instagram_username
    # Output directory
    output_directory = r"2"           

    extract_metadata(username, output_directory)


# In[2]:


import os
import shutil

def filter_and_copy_files(input_directory, output_directory):
    # Create the output directory if it does not exist
    os.makedirs(output_directory, exist_ok=True)

    # Create subdirectories for Images and Videos
    images_directory = os.path.join(output_directory, 'Images')
    videos_directory = os.path.join(output_directory, 'Videos')
    os.makedirs(images_directory, exist_ok=True)
    os.makedirs(videos_directory, exist_ok=True)

    # Iterate through all files in the input directory
    for filename in os.listdir(input_directory):
        # Check if the file is a JPG or MP4 file
        if filename.endswith('.jpg'):
            # Construct the full path of the file
            source_file = os.path.join(input_directory, filename)
            # Copy the file to the Images subdirectory
            shutil.copy(source_file, os.path.join(images_directory, filename))
        elif filename.endswith('.mp4'):
            # Construct the full path of the file
            source_file = os.path.join(input_directory, filename)
            # Copy the file to the Videos subdirectory
            shutil.copy(source_file, os.path.join(videos_directory, filename))

    print("Filtered files copied to:", output_directory)

if __name__ == "__main__":
    # Input directory containing downloaded files
    input_directory = r"2"
    # Output directory for filtered files
    output_directory = r"D:\Python\NYX\Insta_folders\india"

    filter_and_copy_files(input_directory, output_directory)


# In[3]:


get_ipython().system('pip install moviepy')


# In[4]:


import os
import csv
from moviepy.editor import VideoFileClip

def get_video_duration(file_path):
    try:
        clip = VideoFileClip(file_path)
        duration = clip.duration
        clip.close()
        return duration
    except Exception as e:
        print(f"Error extracting duration for {file_path}: {e}")
        return None

def generate_csv(folder_path, csv_filename):
    # Create or open the CSV file for writing
    with open(csv_filename, 'w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Write header to the CSV file
        csv_writer.writerow(['File Name', 'File Type', 'Duration (s)'])

        # Traverse through the folder and its subfolders
        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)

                # Get the file extension
                file_type = file_name.split('.')[-1]

                # Get duration for videos, None for non-video files
                if file_type.lower() in ['mp4', 'avi', 'mkv', 'mov']:
                    duration = get_video_duration(file_path)
                else:
                    duration = None

                # Write information to the CSV file
                csv_writer.writerow([file_name, file_type, duration])

    print(f"CSV file '{csv_filename}' generated successfully.")

# Provide the folder path and desired CSV filename
folder_path = r'D:\Python\NYX\Insta_folders\fogg_india'
csv_filename = 'Fogg_india_metadata.csv'

# Call the function to generate the CSV file
generate_csv(folder_path, csv_filename)


# In[13]:


# import os
# import shutil

# def filter_and_copy_files(input_directory, output_directory):
#     # Create the output directory if it does not exist
#     os.makedirs(output_directory, exist_ok=True)

#     # Iterate through all files in the input directory
#     for filename in os.listdir(input_directory):
#         # Check if the file is a JPG or MP4 file
#         if filename.endswith('.jpg') or filename.endswith('.mp4'):
#             # Construct the full path of the file
#             source_file = os.path.join(input_directory, filename)
#             # Copy the file to the output directory
#             shutil.copy(source_file, output_directory)

#     print("Filtered files copied to:", output_directory)

# if __name__ == "__main__":
#     # Input directory containing downloaded files
#     input_directory = r"D：﹨Python﹨NYX﹨Insta_folders﹨1"
#     # Output directory for filtered files
#     output_directory = r"D:\Python\NYX\Insta_folders\3"

#     filter_and_copy_files(input_directory, output_directory)





