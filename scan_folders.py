import shutil
import yaml
import os
import logging
from shutil import move

# Open the existing mkdocs.yml file to read its configuration
with open('mkdocs.yml', 'r') as mkdocs:
    # Load the YAML configuration from the file
    configuration = yaml.load(mkdocs, Loader=yaml.SafeLoader)

    # Initialize the navigation structure with README.md as the first item
    configuration['nav'] = ['README.md']

    # Get the current working directory
    current_directory = os.getcwd()
    docs_path = os.path.join(current_directory, 'docs')
    exceptions = ['Load Balance Testing on 4112F-ON', 'VMWare']

    # Retrieve and sort directories excluding the exceptions
    sorted_directories = sorted(
        [d for d in os.listdir(docs_path) if os.path.isdir(os.path.join(docs_path, d)) and d not in exceptions])

    for directory in sorted_directories + exceptions:
        dir_path = os.path.join(docs_path, directory)

        if directory in exceptions:
            # Sort the subdirectories of the exception directory
            subdirectories = sorted(os.listdir(dir_path))
            for subdirectory in subdirectories:
                subdir_path = os.path.join(dir_path, subdirectory)
                if os.path.isdir(subdir_path) and os.path.exists(os.path.join(subdir_path, 'README.md')):
                    # Add the sorted subdirectory's README.md to the navigation
                    configuration['nav'].append(directory + '/' + subdirectory + '/README.md')
                else:
                    # Log a warning for subdirectories without a README.md
                    logging.warning(subdirectory + " in " + directory + " does not have a readme file!")
        else:
            # Handle non-exception directories
            if os.path.exists(os.path.join(dir_path, 'README.md')):
                # Add the directory's README.md to the navigation
                configuration['nav'].append(directory + '/README.md')

                # Code to ensure the first line of README.md matches the directory name

                # This block ensures that the first line of every README.md file
                # starts with a title that matches the directory name
                file_read_success = False
                original_file_path = os.path.join(current_directory, 'docs', directory, 'README.md')
                with open(original_file_path, 'r+') as file:
                    try:
                        # Read the first line of the file
                        first_line = file.readline()
                        new_file_path = os.path.join(current_directory, 'docs', directory, 'README_temp.md')
                        with open(new_file_path, 'w') as temp_file:
                            # Write a new first line with the directory name
                            temp_file.write('# ' + directory + "\n")
                            # Copy the rest of the original file to the temp file
                            shutil.copyfileobj(file, temp_file)
                            file_read_success = True
                    except UnicodeDecodeError as error:
                        # Log an error if there's a Unicode decoding issue
                        logging.error("Reading " + directory + "\'s README.md threw some unicode error. "
                                      "This usually means I copy and pasted funky quotes from a PDF or something. I "
                                      "may also have written something in Chinese: " + str(error))

                # If the file was successfully read and a temporary file created,
                # replace the original README.md with the modified version
                if file_read_success:
                    os.remove(original_file_path)
                    move(new_file_path, original_file_path)

# Write the updated configuration back to mkdocs.yml
with open('mkdocs.yml', 'w') as mkdocs:
    yaml.dump(configuration, mkdocs)
