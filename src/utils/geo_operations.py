from math import radians, cos, sin, acos
from src.constants import DUBLIN_OFFICE_LATITUDE, DUBLIN_OFFICE_LONGITUDE, DISTANCE_LIMIT_KM, EARTH_RADIUS_KM
import logging

class GeoOperations:

    """Class to perform all the geo operations
       author: Abhilash Roy
    """

    def __init__(self):
        self._logger = logging.getLogger(__name__)

    def _cal_dist_between_coordinates(self, lat_1, lon_1, lat_2, lon_2):
        """
        Calculate the distance in kilometers between two points.
        :param lat_1: Latitude of first location
        :param lon_1: Longitude of first location
        :param lat_2: Latitude of second location
        :param lon_2: Longitude of second location

        :return: Distance between two locations in kilometer
        """

        # Converting the degrees to radians
        lon_1 = radians(lon_1)
        lon_2 = radians(lon_2)
        lat_1 = radians(lat_1)
        lat_2 = radians(lat_2)

        # from source https://en.wikipedia.org/wiki/Great-circle_distance
        # applying  formula to calculate the distance

        delta_longitude = lon_2 - lon_1

        delta_sigma = acos(sin(lat_1) * sin(lat_2) + cos(lat_1) * cos(lat_2) * cos(delta_longitude))

        return EARTH_RADIUS_KM * delta_sigma

    def _check_range(self, input_list):
        """
        Check if the calculated distance is within the specified range.
        :param input_list: List of data entities from the input file
        :return: List of user name and id's within the specified range
        """
        try:
            result = {}
            for data_entity in input_list:
                distance = self._cal_dist_between_coordinates(float(data_entity.latitude), float(data_entity.longitude),
                                                              DUBLIN_OFFICE_LATITUDE, DUBLIN_OFFICE_LONGITUDE)

                # Check if the distance is within the specified range
                if distance < DISTANCE_LIMIT_KM:
                    result[data_entity.user_id] = data_entity.name
            return sorted(result.items())
        except (TypeError, Exception) as error:
            self._logger.error(f"Error while checking range, {error}")

