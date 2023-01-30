from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/cat1.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_add_new_pet_no_photo_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age='4'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_photo_of_pet(pet_photo='images/P1040103.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Запрашиваем ключ api и сохраняем в переменую auth_key и получаем список своих животных
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")


    # Если список не пустой, то пробуем обновить его фото
    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert 'pet_photo' in result
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

def test_get_wrong_information(filter='32'):
    """ Проверяем что запрос всех питомцев ничего не возвращает если ввести в фильтр некорректное значение"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status != 200

def test_add_new_pet_with_wrong_age(name='Барбоскин', animal_type='двортерьер',
                                     age='fd', pet_photo='images/cat1.jpg'):
    """Проверяем что нельзя создать питомца, указывая в возрасте буквы"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key и узнаем число питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets_before = pf.get_list_of_pets(auth_key, "my_pets")
    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    _, my_pets_after = pf.get_list_of_pets(auth_key, "my_pets")
    # Сверяем полученный ответ с ожидаемым результатом
    if len(my_pets_after['pets'])>len(my_pets_before['pets']):
        # если список моих питомцев увеличился, то выдаем ошибку
        raise Exception("You can't create a pet with the wrong type of age")
    else:
        # если список питомцев не изменился, то все хорошо
        assert status == 200

def test_add_new_pet_with_wrong_name(name='', animal_type='двортерьер',
                                     age='12', pet_photo='images/cat1.jpg'):
    """Проверяем что нельзя создать питомца без обязательного поля имя"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets_before = pf.get_list_of_pets(auth_key, "my_pets")
    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    _, my_pets_after = pf.get_list_of_pets(auth_key, "my_pets")
    # Сверяем полученный ответ с ожидаемым результатом
    if len(my_pets_after['pets']) > len(my_pets_before['pets']):
        # если список моих питомцев увеличился, то выдаем ошибку
        raise Exception("You can't create a pet with wrong name")
    else:
        # если список питомцев не изменился, то все хорошо
        assert status == 200


def test_get_api_key_for_wrong_user(email="wrong@mail.ru", password="invalid_password"):
    """ Проверяем что запрос api ключа возвращает не возвращает статус 200"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status != 200


def test_add_new_pet_with_wrong_animal_type(name='Барбоскин', animal_type='',
                                     age='12', pet_photo='images/cat1.jpg'):
    """Проверяем что нельзя создать питомца с неверным типом животного"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key и узнаем число питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets_before = pf.get_list_of_pets(auth_key, "my_pets")
    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    _, my_pets_after = pf.get_list_of_pets(auth_key, "my_pets")
    # Сверяем полученный ответ с ожидаемым результатом
    if len(my_pets_after['pets'])>len(my_pets_before['pets']):
        # если список моих питомцев увеличился, то выдаем ошибку
        raise Exception("You can't create a pet with wrong animal_type")
    else:
        # если список питомцев не изменился, то все хорошо
        assert status == 200


def test_add_new_pet_without_photo_with_wrong_name(name='', animal_type='чтож',
                                     age='12'):
    """Проверяем что нельзя создать питомца без фото с неверным именем"""


    # Запрашиваем ключ api и сохраняем в переменую auth_key и узнаем число питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets_before = pf.get_list_of_pets(auth_key, "my_pets")
    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    _, my_pets_after = pf.get_list_of_pets(auth_key, "my_pets")
    # Сверяем полученный ответ с ожидаемым результатом
    if len(my_pets_after['pets'])>len(my_pets_before['pets']):
        # если список моих питомцев увеличился, то выдаем ошибку
        raise Exception("You can't create a pet with wrong name")
    else:
        # если список питомцев не изменился, то все хорошо
        assert status == 200

def test_add_new_pet_without_photo_with_wrong_animal_type(name='барбоска', animal_type='',
                                     age='12'):
    """Проверяем что нельзя создать питомца без фото с неверным типом животного"""


    # Запрашиваем ключ api и сохраняем в переменую auth_key и узнаем число питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets_before = pf.get_list_of_pets(auth_key, "my_pets")
    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    _, my_pets_after = pf.get_list_of_pets(auth_key, "my_pets")
    # Сверяем полученный ответ с ожидаемым результатом
    if len(my_pets_after['pets'])>len(my_pets_before['pets']):
        # если список моих питомцев увеличился, то выдаем ошибку
        raise Exception("You can't create a pet with wrong animal_type")
    else:
        # если список питомцев не изменился, то все хорошо
        assert status == 200

def test_add_new_pet_without_photo_with_wrong_age(name='барбоска', animal_type='',
                                     age='gffgf'):
    """Проверяем что нельзя создать питомца без фото с неверным типом животного"""


    # Запрашиваем ключ api и сохраняем в переменую auth_key и узнаем число питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets_before = pf.get_list_of_pets(auth_key, "my_pets")
    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    _, my_pets_after = pf.get_list_of_pets(auth_key, "my_pets")
    # Сверяем полученный ответ с ожидаемым результатом
    if len(my_pets_after['pets'])>len(my_pets_before['pets']):
        # если список моих питомцев увеличился, то выдаем ошибку
        raise Exception("You can't create a pet with wrong age")
    else:
        # если список питомцев не изменился, то все хорошо
        assert status == 200
        assert result['age']==age