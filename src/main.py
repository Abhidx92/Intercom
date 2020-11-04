from tabulate import tabulate
from src.utils.file_operations import FileOperations
from src.utils.geo_operations import GeoOperations
from src.constants import INPUT_PATH
import logging

class Main:

    """Main class to invite people
       Author: Abhilash Roy
    """

    def __init__(self, INPUT_PATH):
        self._file_operations = FileOperations(INPUT_PATH)
        self._geo_operations = GeoOperations()
        self._logger = logging.getLogger(__name__)

    def _invite_people(self):
        """
        Invite people based on their distance from Intercom Dublin office
        Prints user_id and name of people invited
        """
        # Reads the user list from input data
        input_list = self._file_operations._read_file()

        # After distance calculation checks if the user is within the specified range
        result = self._geo_operations._check_range(input_list)

        # Finally, print the user_id and names of people invited
        print(tabulate(result, headers=["user_id", "name"]))


if __name__ == "__main__":
    import sys
    sys.argv.append(INPUT_PATH)
    main = Main(sys.argv[1])
    main._invite_people()
