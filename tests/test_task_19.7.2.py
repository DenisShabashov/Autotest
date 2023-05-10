
from api import PetFriends
from settings import valid_email, valid_password, invalid_password, invalid_email

pf = PetFriends()


# 1
def test_add_new_pet_with_valid_data(name='Grogu', animal_type='Mandalorian', age='1'):
    """Проверяем что можно добавить питомца с корректным типом данных"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_new_pet(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name

# 2
def test_empty_string_name(name='', animal_type='Котэ', age= '5'):
    """Проверяем что можно ли добавить питомца с пустой строкой в поле name"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.create_new_pet(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == ''

# 3
def test_empty_string_animal_type(name='Мурзик', animal_type='', age='5'):
    """Проверяем что можно ли добавить питомца с пустой строкой в поле animal_type"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_new_pet(auth_key, name, animal_type, age)

    assert status == 200
    assert result['animal_type'] == ''


# 4
def test_string_length_name256(
        name='v0UeoFqyoraHsTbUM6EHCP4ql25FZh7KxHkrF5KvA6NcqHE7QtsCYZ2XeOc9fD5fEunyDhldHvGEiFxvIYlSojwwW1EJKlgMOYQQuszMkpbn3mQfuBipoj9HJsjgcEONcTr7qfRhnNHTaT4qLJFllLt8XZE7jh7Jln08hLdZbzv5oIazgwXiLpVo2ZH8x2lXmqq04wc0zI70X6mkAQ61vrVzt8wB5QFcOHvs9gGtY1vxjvx0dbOTcU9J13usKzF2',
        animal_type='Котэ', age='5'):
    """Проверяем что можно ли добавить имя питомца с длинной строки в 256 символов"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_new_pet(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name

# 5
def test_string_length_name1000(
        name='xTjD1cP3U8UxSbsRGwwItEICPbCxFLOAOZcGReTjYWQa93KhpeDgjrppY9R2O7rfo94HMYIItal0YGM4ndvWFUJ76iSMJU7UV4InHHsejNc75FUQ26MpLNqxKrbZDE7su4hkPs2dqfD7F2V1eAzaadHHpbJY6UqBqb42GKo6HMpFVkWvg3O1Z48fFO0qDIchuElXVch8NPCJIL3oia5nWkxT76xDt0ax4P5jtXpUf7P0qje0z4zGMgfIWPua38TNpsIBTNHTfTTdG2a7EzvE1qHiR3K22tsLoBtnU9eNQlVl98CL9pTbwEbeFhwQBCAmerxeeNi7HmjMwIdjUFQTCBne7jHaTKvxB3Tgjn4Ovp5M6KTKS5Y4wJXitdXZw5pLDk7YpxIRXY4EDkD3H9ekXEPsZOvhZB6os4iFFqpThaehwa96kyY69fR5pCN8Tf48dsTJJHsaAOD6MNrzMXStzmVzW4tkkH2HG1etJYcHbXgiX9OMjYklEHFvPvJkkUXhnTSBDb4lgDXxAl4KCgBVmtSkKESAw0PSeR43Tydzyqyu8Vry6qlSS7whKO4Tyoy6T1Gcurdq7IEfHNDp6LLlO02sRjOEtDnS5no3i1zMSLcuteYrJuRpKzcNcv7bLMI9QYxSAQ7hykSefCsiJEZxtwSmBpVMQ8ISshEmuclyM1YrSZS7nLpoRgBa9y9G9H3HRbcUMJUCI3Px4PMWCsikMzpglqZJQX0fwIl4scMlo0db4mgZvxKXv5VRXB4FY8Wl3JkaxYsl8FfQ9GP5Cj1vfy0ddQTtRLVbQDtBM9UAuFzpKXcsxKr2P9GElcXLJ2MopKKs0s6rb1Ef91tmKkFHo5DnP5DMyWarsc8c93okPA4EMT60oMeQVrMxEDdxNnPEiqXPVH2afkCQkZrq5gZsxhnnL7XnbeVIkSRbyVjLA1GZMd8tTaJ444qLlXsSIVvn3YMGHd5er0Xy087UFGY93QnzZ5nhSMHKNpeN22ca',
        animal_type='Котэ', age='5'):
    """Проверяем что можно ли добавить имя питомца с длинной строки в 1000 символов"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_new_pet(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name

# 6
def test_string_length_name(name=5, animal_type='Котэ', age='5'):
    """Проверяем что можно ли добавить питомца используя в поле name целочисленные значение"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_new_pet(auth_key, name, animal_type, age)

    assert status == 400
    assert int(result['name']) == 5



# 7
def test_update_age_in_string(name='Мурзик', animal_type='Котэ', age='5'):
    """Проверяем возможность изменения возраста в формате строки"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['age'] == '5'
    else:

        raise Exception("Список своих питомцев пуст")

# 8
def test_update_name_integer(name=2, animal_type='Котэ', age=9):
    """ Проверяем возможность изменения имени питомца при вводе целочисленного значения"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert int(result['name']) == 2

# 9
def test_get_api_key_for_invalid_password(email=valid_email, password=invalid_password):
    """ Проверяем что запрос api ключа возвращает статус 403 в результате ввода неправильного пароля"""

    status, result = pf.get_api_key(email, password)

    assert status == 403

# 10
def test_get_api_key_for_invalid_email(email=invalid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 403 в результате ввода неправильного email"""

    status, result = pf.get_api_key(email, password)

    assert status == 403





