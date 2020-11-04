import json
import logging
from src.constants import OUTPUT_PATH
from src.model.data_entity import DataEntity


class FileOperations:

    """Class to perform all the file operations
       author: Abhilash Roy
    """

    def __init__(self, input_path):
        self.input_path = input_path
        self._logger = logging.getLogger(__name__)

    def _read_file(self):
        """
        Read the file line by line and return input data list
        :return: List of dictionaries
        """
        input_list = []
        try:
            with open(self.input_path) as json_file:
                lines = json_file.readlines()
                for line in lines:
                    data = json.loads(line)
                    data_entity = DataEntity(data)
                    input_list.append(data_entity)
            json_file.close()
            return input_list
        except (FileNotFoundError, IOError, Exception) as error:
            self._logger.error(f"Error while reading the file, {error}")

    def _write_file(self, data):
        """
        Write into the file.
        :param data: Data to be written in file
        :return: void
        """
        try:
            with open(OUTPUT_PATH, "w") as json_file:
                for line in data:
                    json_file.write(line)
                json_file.close()
        except (FileNotFoundError, IOError, Exception) as error:
            self._logger.error(f"Error while writing into file, {error}")
