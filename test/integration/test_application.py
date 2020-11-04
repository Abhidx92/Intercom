import subprocess
from src.main import Main

OUTPUT = b"""  user_id  name
---------  -----------------
        4  Ian Kehoe
        5  Nora Dempsey
        6  Theresa Enright
        8  Eoin Ahearn
       11  Richard Finnegan
       12  Christina McArdle
       13  Olive Ahearn
       15  Michael Ahearn
       17  Patricia Cahill
       23  Eoin Gallagher
       24  Rose Enright
       26  Stephen McArdle
       29  Oliver Ahearn
       30  Nick Enright
       31  Alan Behan
       39  Lisa Ahearn
"""


class TestApplication:

    def test_invites(self):

        path = "test/data/input_data.txt"
        result = subprocess.run(["python3", "-m", "src.main", path], stdout=subprocess.PIPE)
        assert result.stdout.decode("utf-8") == OUTPUT.decode("utf-8")