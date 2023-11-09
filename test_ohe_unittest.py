import unittest
from one_hot_encoder import fit_transform


class TestOneHotEncoder(unittest.TestCase):
    def test_fit_transform_multiple(self):
        result = fit_transform('a', 'b', 'c', 'd', 'b')
        expected = [('a', [0, 0, 0, 1]), ('b', [0, 0, 1, 0]),
                    ('c', [0, 1, 0, 0]), ('d', [1, 0, 0, 0]),
                    ('b', [0, 0, 1, 0])]
        self.assertEqual(result, expected)

    def test_fit_transform_list(self):
        result = fit_transform(['a', 'b', 'c', 'a', 'b', 'c'])
        expected = [('a', [0, 0, 1]), ('b', [0, 1, 0]), ('c', [1, 0, 0]),
                    ('a', [0, 0, 1]), ('b', [0, 1, 0]), ('c', [1, 0, 0])]
        self.assertEqual(result, expected)

    def test_fit_transform_empty(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_fit_transform_multiple_int(self):
        with self.assertRaises(TypeError):
            fit_transform(1, 2, 3, 4)


if __name__ == '__main__':
    unittest.main()

    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)
    print(transformed_cities)
    assert transformed_cities == exp_transformed_cities
