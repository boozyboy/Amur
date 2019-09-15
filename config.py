import os
import re
import const

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@ ============================================================== @@@
# @@@ ======== СОЗДАНИЕ И/ИЛИ ЧТЕНИЕ КОНФИГУРАЦИОННОГО ФАЙЛА ======= @@@
# @@@ ============================================================== @@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

"""
Проверка наличия директории для хранения конфигурационного файла.
При отсутствии - создаем.
"""
config_cat_path = r'.\config'
if not os.path.exists(config_cat_path):
    os.makedirs(config_cat_path)

"""
Проверка наличия конфигурационного файла. При отстутствии -
создаем и заполняем из модуля const.py.
"""
config_file_path = r'.\config\config.txt'
if not os.path.exists(config_file_path):
    with open(config_file_path, 'w') as config_file:
        for config_file_part in const.config_file_text:
            config_file.write(config_file_part)


# Сохраняем содержимое конфигурациооного файла в одну строку
config_file = open(config_file_path, 'r')
config_file_read = config_file.read()
config_file.close()


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@ ============================================================== @@@
# @@@ ================= КОНФИГУРАЦИОННЫЕ ПЕРЕМЕННЫЕ ================ @@@
# @@@ ============================================================== @@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

"""
Вспомогательная функция для поиска содержимого, которым будут
заполнены конфигурационные переменные.
"""


def between_two_markers_search(marker, strng):
    """
    В строке strng находит подстроку между двух "маркеров".
    Возвращает список из строк, разделенных символом начала
    новой строки в этой подстроке.
    Если число "маркеров" в строке отличается от двух,
    бросит ошибку.
    """
    result = re.split(marker, strng)
    if len(result) != 3:
        raise ValueError(
            f'Число маркеров {marker} в передаваемой для поиска между '
            f'маркерами строке не равно двум.'
        )
    else:
        return result[1][1:-1].split('\n')
    # [1] - т.к. нулевым вхождением будет все, что до первого "маркера".
    # [1:-1] - т.к. нулевым и последним эл-том строки будут '\n' после
    # первого и перед вторым "маркером".


"""
Создаем и заполняем конфигурационные переменные сожержимым,
прочитанным из конфигурационного файла.
"""

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$ СЛОВАРЬ ДЛЯ ЧТЕНИЯ ВХОДНЫХ ДАННЫХ $$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

"""
Словарь описаний, типов и классификаторов объекта для
сигналов шкафов автоматики СТБ. Ключ - подстрока из
стандартных описаний на английском, нужен для
сопоставления со входными данными.
Первый элемент в списке - описание на русском.
Второй - тип объекта.
Третий - тип объекта для шкафов второй категории.
Четвертый - классификатор объекта.
"""

descriptions_types_classes = {}
for key_values in between_two_markers_search(
    const.descriptions_types_classes_marker,
    config_file_read
):
    kv = key_values.split(': ')
    descriptions_types_classes[kv[0]] = kv[1].split(', ')


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$ HS_OS, ALARMING, XL_XLA $$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

"""
Список классификаторов сигналов, которые должны
участвовать в программе hs_os
"""
hs_os_for = []
for string in between_two_markers_search(
    const.hs_os_for_marker,
    config_file_read
):
    hs_os_for += string.split(', ')

"""
Список классификаторов сигналов, которые должны
участвовать в программе alarming
"""
alarming_for = []
for string in between_two_markers_search(
    const.alarming_for_marker,
    config_file_read
):
    alarming_for += string.split(', ')

"""
Список классификаторов сигналов, которые должны
участвовать в программе xl_xla
"""
xl_xla_for = []
for string in between_two_markers_search(
    const.xl_xla_for_marker,
    config_file_read
):
    xl_xla_for += string.split(', ')

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$ COUNTING $$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

"""
Список классификаторов сигналов ручных извещателей, 
которые должны участвовать в программе counting.
"""
buttons_counting_for = []
for string in between_two_markers_search(
    const.buttons_counting_for_marker,
    config_file_read
):
    buttons_counting_for += string.split(', ')

"""
Список классификаторов сигналов сенсорных датчиков, 
которые должны участвовать в программе counting.
"""
sensors_counting_for = []
for string in between_two_markers_search(
    const.sensors_counting_for_marker,
    config_file_read
):
    sensors_counting_for += string.split(', ')

"""
Список классификаторов сигналов исполнительного оборудования,
которое должно участвовать в программе counting.
"""
actuators_counting_for = []
for string in between_two_markers_search(
    const.actuators_counting_for_marker,
    config_file_read
):
    actuators_counting_for += string.split(', ')

"""
Словарь для классификации счетчиков в котором каждый
ключ - назначение счетчика на русском, каждое значение -
принятые в проекте отличительные части названий для счетчиков.
"""
cntrs_dict = {}
for key_value_couple in between_two_markers_search(
    const.cntrs_dict_marker, config_file_read
):
    kv = key_value_couple.split(': ')
    cntrs_dict[kv[0]] = kv[1]

# print(cntrs_dict)
# print(hs_os_for)
# print(alarming_for)
# print(xl_xla_for)
# print(buttons_counting_for)
# print(sensors_counting_for)
# print(actuators_counting_for)
# print(descriptions_types_classes)
