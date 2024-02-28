import os
import shutil
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the variable from .env
downloads_path = os.getenv("downloads_path")

# Check if the variable is loaded successfully
if downloads_path:
    print(f"Downloads path: {downloads_path}")

    def organize_downloads_folder(download_folder_path):
        # List all files in the Downloads folder
        files = os.listdir(download_folder_path)

        # Create a dictionary to store file types and their corresponding folders
        file_types = {}

        # Iterate through each file
        for file in files:
            # Get the file extension
            _, file_extension = os.path.splitext(file)

            # Remove the dot from the extension
            file_extension = file_extension[1:]

            # Create a folder for the file type if it doesn't exist
            if file_extension not in file_types:
                file_types[file_extension] = os.path.join(download_folder_path, file_extension)
                os.makedirs(file_types[file_extension], exist_ok=True)

            # Move the file to its corresponding folder
            current_file_path = os.path.join(download_folder_path, file)
            new_file_path = os.path.join(file_types[file_extension], file)
            shutil.move(current_file_path, new_file_path)

        print("Downloads folder organized successfully!")

    # Call the function to organize the Downloads folder
    organize_downloads_folder(downloads_path)
else:
    print("Error: 'downloads_path' not found in .env file.")
