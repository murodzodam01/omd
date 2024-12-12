import pytest
from one_hot_encoder import fit_transform


def test_fit_transform_multiple():
    result = fit_transform('a', 'b', 'c', 'd', 'b')
    expected = [('a', [0, 0, 0, 1]), ('b', [0, 0, 1, 0]), ('c', [0, 1, 0, 0]),
                ('d', [1, 0, 0, 0]), ('b', [0, 0, 1, 0])]
    assert result == expected


def test_fit_transform_list():
    result = fit_transform(['a', 'b', 'c', 'a', 'b', 'c'])
    expected = [('a', [0, 0, 1]), ('b', [0, 1, 0]), ('c', [1, 0, 0]),
                ('a', [0, 0, 1]), ('b', [0, 1, 0]), ('c', [1, 0, 0])]
    assert result == expected


def test_fit_transform_empty():
    with pytest.raises(TypeError):
        fit_transform()


def test_fit_transform_multiple_int():
    with pytest.raises(TypeError):
        fit_transform(1, 2, 3, 4)


if __name__ == '__main__':
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
