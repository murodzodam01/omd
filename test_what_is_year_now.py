import unittest
from what_is_year_now import what_is_year_now
from unittest.mock import patch
import json


class TestWhatIsYearNow(unittest.TestCase):
    @patch('what_is_year_now.urllib.request.urlopen')
    def test_YMD_format(self, mock_urlopen):
        mock_resp = {'currentDateTime': '2019-03-01'}
        mock_urlopen.return_value.__enter__.return_value.read.return_value \
            = json.dumps(mock_resp).encode()

        result = what_is_year_now()
        self.assertEqual(result, 2019)

    @patch('what_is_year_now.urllib.request.urlopen')
    def test_DMY_format(self, mock_urlopen):
        mock_resp = {'currentDateTime': '01.03.2019'}
        mock_urlopen.return_value.__enter__.return_value.read.return_value \
            = json.dumps(mock_resp).encode()

        result = what_is_year_now()
        self.assertEqual(result, 2019)

    @patch('what_is_year_now.urllib.request.urlopen')
    def test_what_is_year_now_invalid_format(self, mock_urlopen):
        mock_resp = {'currentDateTime': '2019/03/01'}
        mock_urlopen.return_value.__enter__.return_value.read.return_value \
            = json.dumps(mock_resp).encode()

        with self.assertRaises(ValueError):
            what_is_year_now()


if __name__ == '__main__':
    year = what_is_year_now()
    exp_year = 2019

    print(year)
    assert year == exp_year
