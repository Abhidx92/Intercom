from src.utils.file_operations import FileOperations

INPUT_PATH = "test/data/input_data.txt"


class TestFileOpeartions:

    def test_file_reader(self):
        file_operations = FileOperations(INPUT_PATH)
        input_list = file_operations._read_file()
        assert input_list is not None
