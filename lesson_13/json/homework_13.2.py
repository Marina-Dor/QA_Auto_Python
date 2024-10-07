import os
import json
import logging

# Logging Config
logging.basicConfig(filename='json_Doroshenko.log',
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


folder_path = 'json_files'


def validate_json_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                json.load(file)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            logging.error(f"File {filename} is invalid. Error: {str(e)}")


validate_json_files(folder_path)
