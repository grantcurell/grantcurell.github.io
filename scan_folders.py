import shutil

import yaml
import os
import logging
from shutil import move

with open('mkdocs.yml', 'r') as mkdocs:
    configuration = yaml.load(mkdocs, Loader=yaml.SafeLoader)

    configuration['nav'] = ['index.md']

    current_directory = os.getcwd()

    for directory in os.listdir(os.path.join(current_directory, 'docs')):
        if os.path.isdir(os.path.join(current_directory, 'docs', directory)):
            configuration['nav'].append(directory + '/README.md')
            if not os.path.exists(os.path.join(current_directory, 'docs', directory, 'README.md')):
                logging.warning(directory + " does not have a readme file!")
            else:

                # This block just makes sure the first line of every file has a title that is the same as the directory
                # name so that it appears correctly in the menu
                file_read_success = False
                original_file_path = os.path.join(current_directory, 'docs', directory, 'README.md')
                with open(original_file_path, 'r+') as file:
                    try:
                        first_line = file.readline()
                        new_file_path = os.path.join(current_directory, 'docs', directory, 'README_temp.md')
                        with open(new_file_path, 'w') as temp_file:
                            temp_file.write('# ' + directory + "\n")
                            shutil.copyfileobj(file, temp_file)
                            file_read_success = True
                    except UnicodeDecodeError as error:
                        logging.error("Reading " + directory + "\'s README.md threw some unicode error. "
                                      "This usually means I copy and pasted funky quotes from a PDF or something. I "
                                      "may also have written something in Chinese: " + str(error))

                if file_read_success:
                    os.remove(original_file_path)
                    move(new_file_path, original_file_path)

with open('mkdocs.yml', 'w') as mkdocs:
    yaml.dump(configuration, mkdocs)
