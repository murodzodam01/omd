# Guido van Rossum <guido@python.org>
def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print('Утка-маляр 🦆 решила взять зонтик ☂. '
          'Дождя не было. '
          'Лучше бы она не брала зонт(((')


def step2_no_umbrella():
    print('Утка-маляр 🦆 решила не брать зонтик ☂. '
          'Пошел сильный ливень. '
          'Лучше бы она взяла зонт(((')


if __name__ == '__main__':
    step1()
