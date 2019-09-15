from classes import *
from functions import format_position, format_plc_name, del_last_space


def read():

    import pandas as pd
    plc = PLC()

    # input_path = str(input('Введите путь до input.xlsx\n'))
    input_path = r'D:\Python Projects\14092019 HOME\Amur 1.0\path'

    plc.output_path = input_path

    input_frame = pd.read_excel(
        fr'{input_path}\input.xlsx', dtype=str
    ).fillna('')

    # Проверка минимальной наполненности input_frame
    if len(input_frame) == 0:
        raise ValueError('Отсутствуют входные данные! Проверьте input.xlsx.')
    if set(input_frame['Signal']) == {''}:
        raise ValueError('Столбец Signal пуст! Проверьте input.xlsx.')

    # Заполнение атрибутов объекта контроллера
    plc.name = format_plc_name(input_frame['PLC_Name'][0])
    if plc.name == '':
        raise ValueError('Введите имя контроллера в input.xlsx')

    plc.cabinet_category = input_frame['Cabinet_Category'][0]
    if plc.cabinet_category == '':
        raise ValueError('Введите категорию шкафа в input.xlsx')

    plc.reset_position = format_position(input_frame['Reset_Position'][0])
    if plc.reset_position == '':
        raise ValueError('Введите позицию для сброса в input.xlsx')

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$ ПОЗИЦИИ $$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # сохрание множества имен всех позиций на этом контроллере
    positions = set()
    for i in range(len(input_frame)):
        string_number = str(i+2)
        if (
            input_frame['Position'][i].replace(' ', '') == ''
            and
            input_frame['Signal'][i].replace(' ', '') != ''
        ):
            # ошибка при отсутствии заполнения позиции для сигнала
            raise ValueError(
                f'Строка {string_number} столбца Position не заполнена '
                f'при заполненной строке {string_number}\n столбца Signal.'
                'Проверьте входные данные.\n'
            )
        elif input_frame['Position'][i].replace(' ', '') != '':
            positions.add(
                format_position(input_frame['Position'][i])
            )

    # создадим объекты позиций, сохраним ссылки на них
    for position in positions:
        plc.append_position(
            Position(
                name=format_position(position)
            )
        )

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$ СИГНАЛЫ $$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    """
    Создание экземпляров Signal,
    сохранение ссылок на них в список
    сигналов экземпляра PLC.
    """

    for i in range(len(input_frame)):
        if input_frame['Signal'][i].replace(' ', '') != '':
            signal = Signal(

                name=input_frame['Signal'][i],

                descript=input_frame['Description'][i],

                position=format_position(input_frame['Position'][i]),

                plc=plc,

                ff_out=input_frame['FF_Out'][i].split(', ')
                if input_frame['FF_Out'][i] != ''
                else None,

                location=del_last_space(input_frame['Location'][i])
                if input_frame['Location'][i] != ''
                else None,
                # на данном этапе в location записывается
                # имя из input_frame, это значение нужно чтобы
                # в дальнейшем (в этой же функции) перезаписать
                # в этот атрибут ссылку на объект "локации",
                # к которой относится сигнал

                address=input_frame['Address'][i]
                if input_frame['Location'][i] != ''
                else None,

                device=input_frame['Device'][i],

            )
            signal.format_name()
            plc.append_signal(signal)

            # список сигналов заполнен
            if not plc.signals_list_filled:
                plc.signals_list_filled = True

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$ ЛОКАЦИИ (С&E) $$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    """
    Проверка заполнения информации о C&E в input_frame
    по заполнению столбцов Location и Locations.
    Проверка корректности заполнения по равенству множеств
    от значений в столбцах Location и Locations.
    """

    if (
        set(list(input_frame['Location']))
        == set(list(input_frame['Location_CE']))
        and
        set(list(input_frame['Location_CE'])) != {''}
    ):
        seen = []
        for location in input_frame['Location_CE']:
            if location != '' and location in seen:
                raise ValueError(
                    'В столбце Location_CE обнаружены дублирующиеся\n'
                    'названия локаций! Проверьте input.xlsx'
                )
            if location != '':
                seen.append(location)

        """
        Создание экземпляров Location,
        сохранение ссылок на них в список
        локаций экземпляра PLC.
        """
        # заполняем атрибуты на основе input_frame
        import re
        for i in range(len(input_frame)):
            if input_frame['Location_CE'][i] != '':
                string_number = str(i + 2)
                location = Location(

                    name=del_last_space(
                        input_frame['Location_CE'][i]
                    ),

                    warning_cntr=True
                    if 'X' in input_frame['Warning'][i]
                    else False,

                    fire_cntr=True
                    if 'X' in input_frame['Fire'][i]
                    else False,

                    voting_logic=re.findall(
                        r'\d+', input_frame['Voting_Logic'][i]
                    )
                    if input_frame['Voting_Logic'][i] != ''
                    else None,

                    conterminal_systems_cntrs=del_last_space(
                        input_frame['Conterminal_Systems'][i]
                    ).split(', ')
                    if input_frame['Conterminal_Systems'][i] != ''
                    else None,

                    fire_fightings_cntrs=del_last_space(
                        input_frame['Fire_Fightings'][i]
                    ).split(', ')
                    if input_frame['Fire_Fightings'][i] != ''
                    else None,

                )

                # $$$$$$$$$$$$$$$$$$$$$ ПРОВЕРКИ $$$$$$$$$$$$$$$$$$$$$$

                # Voting_Logic
                if (
                    location.voting_logic is not None
                    and
                    len(location.voting_logic) != 2
                ):
                    raise ValueError(
                        f'В строке {string_number} столбца Voting_Logic '
                        'количество чисел отличается от двух! Проверьте '
                        'input.xlsx'
                    )

                if (
                    location.voting_logic is None
                    and
                    not location.warning_cntr
                ):
                    raise ValueError(
                        f'В строке {string_number} отсутствует заполнение'
                        ' столбца Voting_Logic при отсутствующем маркере '
                        'маркере в столбце Warning! Проверьте input.xlsx'
                    )

                if (
                    location.voting_logic is None
                    and
                    (location.fire_cntr
                     or
                     location.fire_fightings_cntrs is not None
                     or
                     location.conterminal_systems_cntrs is not None)
                ):
                    raise ValueError(
                        f'В строке {string_number} отсутствует'
                        ' заполнение Voting_Logic при наличии\n'
                        'заполнения минимум в одном '
                        'из столбцов (Fire, Fire_Fightings,\n'
                        'Conterminal_Systems), заполнение '
                        'которых указывает на необходимость\n'
                        'заполнения Voting_Logic в этой строке. '
                        'Проверьте input.xlsx'
                    )

                # Conterminal_Systems
                if (
                    location.conterminal_systems_cntrs is not None
                    and
                    (len(set(location.conterminal_systems_cntrs))
                     !=
                     len(location.conterminal_systems_cntrs))
                ):
                    raise ValueError(
                        f'В строке {string_number} cтолбца '
                        'Conterminal_Systems обнаружены дублирующиеся\n'
                        'названия смежных систем! Проверьте input.xlsx'
                    )

                # Fire_Fightings
                if (
                    location.fire_fightings_cntrs is not None
                    and
                    (len(set(location.fire_fightings_cntrs))
                     !=
                     len(location.fire_fightings_cntrs))
                ):
                    raise ValueError(
                        f'В строке {string_number} cтолбца '
                        'Fire_Fightings обнаружены дублирующиеся\n'
                        'названия пожаротушений! Проверьте input.xlsx'
                    )

                if (
                    location.fire_fightings_cntrs is not None
                    and
                    location.fire_cntr
                ):
                    raise ValueError(
                        f'В строке {string_number} обнаружено недопустимое '
                        'одновременное\nзаполнение столбцов '
                        'Fires и Fire_Fightings! Проверьте input.xlsx'
                    )

                plc.append_location(location)

        plc.ce_locations_filled = True

    return plc
