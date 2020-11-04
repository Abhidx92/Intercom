class DataEntity:
    """
    Map input data dictionary into objects,
    sets the user attributes to object properties
    :param dictionary: json data of a user from input file
    """
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)