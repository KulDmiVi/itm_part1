def people_info(people):
    """Вывод данных о человеке"""
    for key, value in people.items():
        print(f"{key}: {value}")


def del_key_age(people):
    """Удаление элемента из словаря по ключу"""
    people.pop('age')


def modify_foot_size(people, foot_size):
    """Удаление элемента из словаря по ключу"""
    people['foot_size'] = foot_size


if __name__ == "__main__":
    test_people = {
        'name': 'Василий Василиевич',
        'age': 27,
        'sex': 'м',
        'height': 182,
        'weight': 115,
        'foot_size': 42,
    }

    people_info(test_people)
    del_key_age(test_people)
    print(test_people)
    modify_foot_size(test_people, 39)
    print(test_people)