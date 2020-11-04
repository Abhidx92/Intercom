from src.utils.file_operations import FileOperations
from src.utils.geo_operations import GeoOperations

INPUT_PATH = "test/data/input_data.txt"
geo_operation = GeoOperations()
file_operations = FileOperations(INPUT_PATH)


class TestRange:

    def test_distance(self):
        lat_1, long_1 = 52.986375, -6.043701
        lat_2, long_2 = 51.92893, -10.27699
        ans = geo_operation._cal_dist_between_coordinates(lat_1, long_1, lat_2, long_2)
        assert ans == 309.9365659534358

    def test_range_success(self):
        result = [(4, 'Ian Kehoe'), (5, 'Nora Dempsey'), (6, 'Theresa Enright'), (8, 'Eoin Ahearn'),
                  (11, 'Richard Finnegan'), (12, 'Christina McArdle'), (13, 'Olive Ahearn'), (15, 'Michael Ahearn'),
                  (17, 'Patricia Cahill'), (23, 'Eoin Gallagher'), (24, 'Rose Enright'), (26, 'Stephen McArdle'),
                  (29, 'Oliver Ahearn'), (30, 'Nick Enright'), (31, 'Alan Behan'), (39, 'Lisa Ahearn')]
        input_list = file_operations._read_file()
        output = geo_operation._check_range(input_list)
        assert output == result
