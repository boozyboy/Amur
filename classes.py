import config


class Signal:

    def __init__(
            self,
            name=None,
            descript=None,
            ru_descript=None,
            signal_type=None,
            signal_type_cat2=None,
            classifier=None,
            position=None,
            plc=None,
            location=None,
            ff_out=None,
            device=None,
            address=None,
    ):
        self.name = name
        self.descript = descript
        self.ru_descript = ru_descript
        self.signal_type = signal_type
        self.signal_type_cat2 = signal_type_cat2
        self.classifier = classifier
        self.position = position
        self.plc = plc
        self.location = location
        self.ff_out = ff_out
        self.device = device
        self.address = address

    def format_name(self):
        """
        Метод преобразует название
        сигнала в вид необходимый
        для проекта в SCADA текон
        """
        self.name = self.name.replace('-', '_').replace(' ', '')
        if self.name[0] != 'P':
            self.name = 'P' + self.name

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$ СТРОКИ ДЛЯ ST КОДА $$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # $$$$$$$$$$$$$$$$$$$$$$$$$ COUNTING $$$$$$$$$$$$$$$$$$$$$$$$$

    # ПО ОДНОМУ СИГНАЛУ

    # срабатывание счетчика по одному сигналу
    def one_signal_for_counting(self, counter, cntr_marker):
        return \
            f'{counter}:=Count({self.name}.{cntr_marker}, {counter});\n'

    # TWO OF ANY

    # первый сигнал для счетчика по условиям
    def first_signal_for_toa_counting(self, counter, cntr_marker, n):
        return \
            f'{counter}:=Count(TWO_OF_{n}(\n' \
            f'{self.name}.{cntr_marker},\n'

    # для сигналов между первым и последним
    def signal_between_for_toa_counting(self, cntr_marker):
        return \
            f'{self.name}.{cntr_marker},\n'

    # последний сигнал
    def last_signal_for_toa_counting(self, counter, cntr_marker):
        return \
            f'{self.name}.{cntr_marker}), {counter});\n'

    # TWO OF TWO

    def first_signal_for_tot_counting(self, counter, cntr_marker):
        return \
            f'{counter}:=Count({self.name}.{cntr_marker} '

    def second_signal_for_tot_counting(self, counter, cntr_marker):
        return \
            f'AND {self.name}.{cntr_marker}, {counter});\n'


class SignalsList(list):

    # $$$$$$$$$$$$$$ ПРОВЕРКА НАЛИЧИЯ СИГНАЛОВ $$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$            ДЛЯ            $$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$   HS_OS, XL_XLA, ALARMING $$$$$$$$$$$$$$$$$$$

    # Проверка наличия сигналов для hs_os
    def contains_signals_for_hs_os(self):
        """
        Возвращает True если в списке есть объект
        сигнала, удовлетворяющий условиям:

        1)Зачение атрибута .classifier объекта
        позволяет отнести его к сигналам которые
        должны участвовать в тексте программы hs_os.
        """
        flg = False
        for signal in self:
            if (
                    signal.classifier in config.hs_os_for
                    and
                    not flg
            ):
                flg = True
                break
        return flg

    # Проверка наличия сигналов для xl_xla
    def contains_signals_for_xl_xla(self):
        """
        Возвращает True если в списке есть объект
        сигнала, удовлетворяющий условиям:

        1)Зачение атрибута .classifier объекта
        позволяет отнести его к сигналам которые
        должны участвовать в тексте программы xl_xla.
        """
        flg = False
        for signal in self:
            if (
                    signal.classifier in config.xl_xla_for
                    and
                    not flg
            ):
                flg = True
                break
        return flg

    # Проверка наличия сигналов для alarming
    def contains_signals_for_alarming(self):
        """
        Возвращает True если в списке есть объект
        сигнала, удовлетворяющий условиям:

        1)Зачение атрибута .classifier объекта
        позволяет отнести его к сигналам которые
        должны участвовать в тексте программы alarming.
        """
        flg = False
        for signal in self:
            if (
                    signal.classifier in config.alarming_for
                    and
                    not flg
            ):
                flg = True
                break
        return flg

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$ ПРОВЕРКА НАЛИЧИЯ СИГНАЛОВ ДЛЯ COUNTING $$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def contains_signals_ready_for_counting(self):
        """
        Возвращает True при выполнении условий:

        1)В списке есть экземпляр сигнала, атрибут
        .location которого хранит ссылку на экземпляр
        или наследника Location.

        2)В списке нет экземпляров сигнала, атрибут
        .location которого хранит ссылку на экземпляр
        или наследника str.
        """
        str_flg = None
        loc_flg = None
        for signal in self:
            if isinstance(signal.location, str):
                str_flg = True
            if isinstance(signal.location, Location):
                loc_flg = True
        if (
                loc_flg
                and
                str_flg is None
        ):
            return True
        else:
            return False

    # Проверка наличия исполнительного оборудования
    def contains_actuators_signals_for_counting(self):
        """
        Возвращает True если в списке есть объект
        сигнала, удовлетворяющий условиям:

        1)Зачение атрибута .classifier позволяет
        отнести его к исполнительному оборудованию,
        сигналы которого должны участвовать в тексте
        программы counting.
        """
        flg = False
        for signal in self:
            if (
                    signal.classifier in config.actuators_counting_for
                    and
                    not flg
            ):
                flg = True
                break
        return flg

    # Проверка наличия извещателей
    def contains_sensors_or_buttons_signals_for_counting(self):
        """
        Возвращает True если в списке есть объект
        сигнала, удовлетворяющий условиям:

        1)Зачение атрибута .classifier позволяет
        отнести его к ручным извещателям или
        сенсорным датчикам, сигналы которых должны
        участвовать в тексте программы counting.
        """
        flg = False
        for signal in self:
            if (
                    (signal.classifier in config.buttons_counting_for
                     or
                     signal.classifier in config.sensors_counting_for)
                    and
                    not flg
            ):
                flg = True
                break
        return flg

    # Проверка наличия в списке извещателей не инициирующих тушение
    def contains_sensors_or_buttons_signals_for_counting_without_ff(self):
        """
        Возвращает True если в списке есть объект
        сигнала, удовлетворяющий условиям:

        1)Зачение атрибута .classifier позволяет
        отнести его к ручным извещателям или
        сенсорным датчикам, сигналы которых должны
        участвовать в тексте программы counting.

        2)При наличии такого на входе контроллера
        не должны срабатывать счетчики относящиеся к
        системам пожартотушения в логике контроллера.
        """
        flg = False
        for signal in self:
            if signal.location is not None:
                if (
                        signal.location.fire_fightings_cntrs is None
                        and
                        (signal.classifier in config.buttons_counting_for
                         or
                         signal.classifier in config.sensors_counting_for)
                        and
                        not flg
                ):
                    flg = True
                    break
        return flg

    # Проверка наличия извещателей инициирующих тушение
    def contains_sensors_or_buttons_signals_for_counting_with_ff(self):
        """
        Возвращает True если в списке есть объект
        сигнала, удовлетворяющий условиям:

        1)Зачение атрибута .classifier позволяет
        отнести его к ручным извещателям или
        сенсорным датчикам, сигналы которых должны
        участвовать в тексте программы counting.

        2)При наличии такого на входе контроллера
        должны срабатывать счетчики относящиеся к
        системам пожартотушения в логике контроллера.
        """
        flg = False
        for signal in self:
            if signal.location is not None:
                if (
                        signal.location.fire_fightings_cntrs is not None
                        and
                        (signal.classifier in config.sensors_counting_for
                         or
                         signal.classifier in config.buttons_counting_for)
                        and
                        not flg
                ):
                    flg = True
                    break
        return flg

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$ ЗАПИСЬ ST КОДА В ФАЙЛЫ $$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def xl_xla_write(self, txt):
        """
        Метод записывает txt строки кода на ST.
        В коде участвуют все сигналы из SignalsList
        .classifier которых входят в config.xl_xla_for
        """
        for signal in self:
            if signal.classifier in config.xl_xla_for:
                txt.write(
                    f'{signal.name}(.IVXX, .MBIN, .CAON, '
                    '.SCMX, .STYP, SYS_LNG.XLNG, .IDVX);\n'
                )

    def hs_os_write(self, txt):
        """
        Метод записывает в txt строки кода на ST.
        В коде участвуют все сигналы из SignalsList
        .classifier которых входят в config.hs_os_for
        """
        for signal in self:
            if signal.classifier in config.hs_os_for:
                txt.write(
                    f'{signal.name}(.IVXX, .MBIN, '
                    f'{signal.position.name}CORS.XORS, '
                    '.IDVX, SYS_LNG.XLNG);\n'
                )

    def alarming_write(self, txt, warning_part):
        """
        Метод записывает в txt строки кода на ST.
        В коде участвуют все сигналы из SignalsList
        .classifier которых входят в config.alarming_for
        """
        for signal in self:
            if signal.classifier in config.alarming_for:
                txt.write(
                    f'{signal.name}.CAON:='
                    f'{signal.position.name}XFRX_CNT > 0'
                    f'{warning_part};\n'
                )

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$ ВЫВОД НА ЭКРАН $$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def print_signals(self):
        for signal in self:
            signal_location_name = \
                signal.location.name \
                if isinstance(signal.location, Location) \
                else signal.location
            print(
                f'\nИмя сигнала:'
                f' {signal.name}\n'
                f'Описание сигнала EN:'
                f' {signal.descript}\n'
                f'Описание сигнала RU:'
                f' {signal.ru_descript}\n'
                f'Классификатор сигнала:'
                f' {signal.classifier}\n'
                f'Тип сигнала:'
                f' {signal.signal_type}\n'
                f'Тип сигнала для 2ой категории:'
                f' {signal.signal_type_cat2}\n'
                f'Позиция:'
                f' {signal.position.name}\n'
                f'Имя контроллера:'
                f' {signal.plc.name}\n'
                f'Устройство:'
                f' {signal.device}\n'
                f'Адрес:'
                f' {signal.address}\n'
                f'Локация: '
                f'{signal_location_name}\n'
                f'FF_Out: '
                f'{signal.ff_out}'
            )


class Location:

    def __init__(
            self,
            name=None,
            warning_cntr=None,
            fire_cntr=None,
            fire_fightings_cntrs=None,
            conterminal_systems_cntrs=None,
            voting_logic=None,
    ):
        self.signals_list = SignalsList()  # для ссылок на объекты сигналов
        self.position = None  # см метод position_check_and_set

        self.name = name
        self.warning_cntr = warning_cntr
        self.fire_cntr = fire_cntr
        self.fire_fightings_cntrs = fire_fightings_cntrs
        self.conterminal_systems_cntrs = conterminal_systems_cntrs
        self.voting_logic = voting_logic

    def position_check_and_set(self):
        """
        Метод проверяет, что все сигналы относящиеся
        к "локации" принадлежат к одной позиции,
        бросает ошибку, если это не так.
        Устанавливает значение для атрибута position.
        """
        positions_set = set()
        for signal in self.signals_list:
            positions_set.add(signal.position)
        if len(positions_set) != 1:
            print(
                f'Список позиций сигналов '
                f'"локации" {self.name}:\n'
            )
            for position in positions_set:
                print(position.name)
            print()
            raise ValueError(
                f'В локации {self.name} обнаружены '
                'сигналы с разными позициями,\n'
                'исправьте входные данные.'
            )
        else:
            self.position = list(positions_set)[0]
            self.position.locations_list.append(self)

    def counter_with_condition_write(self, txt):
        pass


class Position:
    """
    Класс необходим для хранения ссылок на объекты
    "локаций" и сигналов, принадлежащих одной позиции.
    Для хранения строковых значений, используемых при
    формировании текста программ на ST для каждой из
    позиций. Для определения в коде каких программ
    необходимо использовать "локации"/сигналы,
    относящиеся к позиции.

    ~~~~~ Описание конструктора: ~~~~~~

    1)name - передаваемое при создании экземпляра
    строковое значение названия позиции в формате
    для формирования строк кода на ST

    ~~~~~~~ Описание атрибутов: ~~~~~~~

    # строки

    1)name - для хранения строкового значения названия
    позиции в формате пригодном для формирования строк
    кода на ST

    # списки

    2)signals_list

    """

    def __init__(
            self,
            name=None,
    ):

        self.name = name

        self.name_for_comment = f"//{self.name[1:-1].replace('_', '-')}"

        self.signals_list = SignalsList()
        self.locations_list = []
        self.upg_counters = []
        self.upg_markers = []
        self.xsy_counters = []
        self.counters = []

    def has_any_warnings(self):
        """
        Возвращет True если в списке locations_list
        есть экземпляр Location атрибут .warning_cntr
        которого == True.
        Если такого экземпляра нет - возвращает False.
        """
        flg = False
        for location in self.locations_list:
            if location.warning_cntr:
                flg = True
                break
        return flg

    def has_any_warnings_with_ff(self):
        """
        Возвращет True если в списке locations_list
        есть экземпляр Location атрибут .warning_cntr
        которого is True, а атрибут .fire_fightings_cntrs
        is not None.
        Если такого экземпляра нет - возвращает False.
        """
        flg = False
        for location in self.locations_list:
            if (
                location.warning_cntr
                and
                location.fire_fightings_cntrs is not None
            ):
                flg = True
                break
        return flg

    def has_any_warnings_without_ff(self):
        """
        Возвращет True если в списке locations_list
        есть экземпляр Location атрибут .warning_cntr
        которого is True, а атрибут .fire_fightings_cntrs
        is None.
        Если такого экземпляра нет - возвращает False.
        """
        flg = False
        for location in self.locations_list:
            if (
                location.warning_cntr
                and
                location.fire_fightings_cntrs is None
            ):
                flg = True
                break
        return flg

    def has_any_fires(self):
        """
        Возвращет True если в списке locations_list
        есть экземпляр Location атрибут .fire_cntr
        которого == True.
        Если такого экземпляра нет - возвращает False.
        """
        flg = False
        for location in self.locations_list:
            if location.fire_cntr:
                flg = True
                break
        return flg

    @staticmethod
    def counters_with_locations_formation(txt, location, counter, cntr_marker):
        if location.fire_cntr:

            # ПО ОДНОМУ СИГНАЛУ
            if (
                    location.voting_logic is not None
                    and
                    int(location.voting_logic[0]) == 1
            ):
                if len(location.signals_list) < 1:
                    raise ValueError(
                        f'В локации {location.name} обнаружен '
                        'конфликт Voting_Logic с количеством\n'
                        'сигналов относящихся к локации! '
                        'Проверьте input.xlsx'
                    )
                else:
                    for signal in location.signals_list:
                        txt.write(
                            signal.one_signal_for_counting(
                                counter,
                                cntr_marker,
                            )
                        )

            # TWO OF ANY
            if (
                    location.voting_logic is not None
                    and
                    int(location.voting_logic[0]) == 2
                    and
                    int(location.voting_logic[1]) > 2
            ):
                if len(location.signals_list) < 3:
                    raise ValueError(
                        f'В локации {location.name} обнаружен '
                        'конфликт Voting_Logic с количеством\n'
                        'сигналов относящихся к локации! '
                        'Проверьте input.xlsx'
                    )
                else:
                    txt.write(
                        location.signals_list[0].first_signal_for_toa_counting(
                            counter,
                            cntr_marker,
                            location.voting_logic[1]
                        )
                    )
                    for signal in location.signals_list[1:-1]:
                        txt.write(
                            signal.signal_between_for_toa_counting(
                                cntr_marker,
                            )
                        )
                    txt.write(
                        location.signals_list[-1].last_signal_for_toa_counting(
                            counter,
                            cntr_marker,
                        )
                    )

            # TWO OF TWO
            if (
                    location.voting_logic is not None
                    and
                    int(location.voting_logic[0]) == 2
                    and
                    int(location.voting_logic[1]) == 2
            ):
                if len(location.signals_list) != 2:
                    raise ValueError(
                        f'В локации {location.name} обнаружен '
                        'конфликт Voting_Logic с количеством\n'
                        'сигналов относящихся к локации! '
                        'Проверьте input.xlsx'
                    )
                else:
                    txt.write(
                        location.signals_list[0].first_signal_for_tot_counting(
                            counter,
                            cntr_marker,
                        )
                    )
                    txt.write(
                        location.signals_list[1].second_signal_for_tot_counting(
                            counter,
                            cntr_marker,
                        )
                    )

    def counting_write(self, txt):

        buttons_sensors = config.buttons_counting_for + \
            config.sensors_counting_for

        actuators = config.actuators_counting_for

        cntrs_markers = config.cntrs_dict

        position_name = self.name

        # СЛОВАРИ НАЛИЧИЯ СЧЕТЧИКОВ НА ПОЗИЦИИ

        # счетчики не инициирующих тушение сигналов
        cntrs_without_ff = {
            'Имитации':
                self.signals_list
                    .contains_sensors_or_buttons_signals_for_counting(),
            'Ремонты':
                self.signals_list
                    .contains_sensors_or_buttons_signals_for_counting()
                or
                self.signals_list
                    .contains_actuators_signals_for_counting(),
            'Неисправности':
                self.signals_list
                .contains_sensors_or_buttons_signals_for_counting_without_ff(),
            'Недостоверности':
                self.signals_list
                .contains_sensors_or_buttons_signals_for_counting_without_ff(),
            'Пожары':
                self.has_any_fires(),
            'Внимания':
                self.has_any_warnings_without_ff()
        }

        # счетчики инициирующих тушение сигналов
        cntrs_with_ff = {
            'Неисправности':
                self.signals_list
                .contains_sensors_or_buttons_signals_for_counting_with_ff(),
            'Недостоверности':
                self.signals_list
                .contains_sensors_or_buttons_signals_for_counting_with_ff(),
            'Внимания':
                self.has_any_warnings_with_ff()
        }

        # ОБНУЛЕНИЕ СЧЕТЧИКОВ
        txt.write('//Обнуление счетчиков\n')

        # без тушения
        for cntr in cntrs_without_ff:
            if cntrs_without_ff[cntr]:
                counter = f'{position_name}{cntrs_markers[cntr]}_CNT'
                txt.write(f'{counter}:=0;\n')

        # c тушением
        for upg_marker in self.upg_markers:
            for cntr in cntrs_with_ff:
                if cntrs_without_ff[cntr]:
                    counter = \
                        f'{position_name}' \
                        f'{cntrs_markers[cntr]}_' \
                        f'{upg_marker}_CNT'
                    txt.write(f'{counter}:=0;\n')

        for counter in self.upg_counters:
            txt.write(f'{counter}:=0;\n')

        # смежные системы
        for counter in self.xsy_counters:
            txt.write(f'{counter}:=0;\n')

        # ИМИТАЦИИ
        if self.signals_list \
               .contains_sensors_or_buttons_signals_for_counting():

            txt.write('\n//Имитации\n')

            cntr_marker = cntrs_markers['Имитации']

            counter = f'{position_name}{cntr_marker}_CNT'

            for classifier in buttons_sensors:

                for signal in self.signals_list:
                    if signal.classifier == classifier:
                        txt.write(
                            signal.one_signal_for_counting(
                                counter,
                                cntr_marker,
                            )
                        )

        # РЕМОНТЫ, ОТКЛЮЧЕНИЯ
        if (
                self.signals_list
                .contains_sensors_or_buttons_signals_for_counting()
                or
                self.signals_list.contains_actuators_signals_for_counting()
        ):

            txt.write('\n//Ремонты, отключения\n')

            cntr_marker = cntrs_markers['Ремонты']

            counter = f'{position_name}{cntr_marker}_CNT'

            for lst in [buttons_sensors, actuators]:
                for classifier in lst:

                    for signal in self.signals_list:
                        if signal.classifier == classifier:
                            txt.write(
                                signal.one_signal_for_counting(
                                    counter,
                                    cntr_marker,
                                )
                            )
                if lst == buttons_sensors:
                    txt.write('\n')

        # СЧЕТЧИКИ ИП БЕЗ ТУШЕНИЯ
        # НЕИСПРАВНОСТИ (сигналы без тушения)
        if (
                self.signals_list
                .contains_sensors_or_buttons_signals_for_counting_without_ff()
        ):

            txt.write('\n//Неисправности (сигналы без тушения)\n')

            cntr_marker = cntrs_markers['Неисправности']

            counter = f'{position_name}{cntr_marker}_CNT'

            for classifier in buttons_sensors:

                for signal in self.signals_list:
                    if signal.location is not None:
                        location = signal.location
                        if (
                                signal.classifier == classifier
                                and
                                location.fire_fightings_cntrs is None
                        ):
                            txt.write(
                                signal.one_signal_for_counting(
                                    counter,
                                    cntr_marker,
                                )
                            )

        # НЕДОСТОВЕРНОСТИ (сигналы без тушения)
        if (
                self.signals_list
                .contains_sensors_or_buttons_signals_for_counting_without_ff()
        ):

            txt.write('\n//Недостоверности (сигнаы без тушения)\n')

            cntr_marker = cntrs_markers['Недостоверности']

            counter = f'{position_name}{cntr_marker}_CNT'

            for classifier in buttons_sensors:

                for signal in self.signals_list:
                    if signal.location is not None:
                        location = signal.location
                        if (
                                signal.classifier == classifier
                                and
                                location.fire_fightings_cntrs is None
                        ):
                            txt.write(
                                signal.one_signal_for_counting(
                                    counter,
                                    cntr_marker,
                                )
                            )

        # ПОЖАРЫ (сигналы без тушения)
        if self.has_any_fires():

            txt.write('\n//Пожары (сигналы без тушения)\n')

            cntr_marker = cntrs_markers["Пожары"]

            counter = f'{position_name}{cntr_marker}_CNT'

            for location in self.locations_list:

                if location.fire_cntr:

                    self.counters_with_locations_formation(
                        txt,
                        location,
                        counter,
                        cntr_marker,
                    )

        # ВНИМАНИЯ (сигналы без тушения)
        if self.has_any_warnings_without_ff():

            txt.write('\n//Внимания (сигналы без тушения)\n')

            cntr_marker = cntrs_markers["Внимания"]

            counter = f'{position_name}{cntr_marker}_CNT'

            for signal in self.signals_list:
                if (
                        signal.location is not None
                        and
                        signal.location.warning_cntr
                ):
                    txt.write(
                        signal.one_signal_for_counting(
                            counter,
                            cntr_marker,
                        )
                    )

        # СЧЕТЧИКИ ИП С ТУШЕНИЕМ
        # НЕИСПРАВНОСТИ (сигналы с тушением)
        if (
                self.signals_list
                .contains_sensors_or_buttons_signals_for_counting_with_ff()
        ):

            txt.write('\n//Неисправности (сигналы с тушением)\n')

            cntr_marker = cntrs_markers['Неисправности']

            for upg_marker in self.upg_markers:

                counter = f'{position_name}{cntr_marker}_{upg_marker}_CNT'

                for classifier in buttons_sensors:

                    for signal in self.signals_list:
                        if signal.location is not None:
                            location = signal.location
                            if (
                                    signal.classifier == classifier
                                    and
                                    location.fire_fightings_cntrs is None
                            ):
                                txt.write(
                                    signal.one_signal_for_counting(
                                        counter,
                                        cntr_marker,
                                    )
                                )

        # НЕДОСТОВЕРНОСТИ
        if (
                self.signals_list
                .contains_sensors_or_buttons_signals_for_counting_with_ff()
        ):

            txt.write('\n//Недостоверности (сигналы с тушением)\n')

            cntr_marker = cntrs_markers['Недостоверности']

            for upg_marker in self.upg_markers:

                counter = f'{position_name}{cntr_marker}_{upg_marker}_CNT'

                for classifier in buttons_sensors:

                    for signal in self.signals_list:
                        if signal.location is not None:
                            location = signal.location
                            if (
                                    signal.classifier == classifier
                                    and
                                    location.fire_fightings_cntrs is None
                            ):
                                txt.write(
                                    signal.one_signal_for_counting(
                                        counter,
                                        cntr_marker,
                                    )
                                )

        # ПОЖАРОТУШЕНИЯ
        if self.has_any_fires():

            txt.write('\n//Пожаротушения (сигналы с тушением)\n')

            cntr_marker = cntrs_markers["Пожары"]

            for upg_marker in self.upg_markers:

                counter = f'{position_name}{cntr_marker}_{upg_marker}_CNT'

                for location in self.locations_list:

                    if location.fire_cntr:

                        self.counters_with_locations_formation(
                            txt,
                            location,
                            counter,
                            cntr_marker,
                        )


class Device:
    """

    """

    def __init__(self):
        pass


class PLC:
    def __init__(
            self,
            name=None,
            cabinet_category=None,
            reset_position=None,
    ):
        self.name = name
        self.cabinet_category = cabinet_category
        self.reset_position = reset_position

        self.__signals_list = SignalsList()
        self.__locations_list = []
        self.__positions_list = []
        self.__devices_list = []

        self.upg_counters = set()
        self.xsy_counters = set()

        self.signals_list_filled = False
        self.ce_locations_filled = False

        self.signals_reformed = False
        self.locations_reformed = False

        self.output_path = None

    def change_output_path(self):
        self.output_path = str(input(
            'Введите путь для выходных файлов\n'
        ))

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$ ЗАПОЛНЕНИЕ СПИСКОВ $$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def append_signal(self, obj):
        if isinstance(obj, Signal):
            self.__signals_list.append(obj)
        else:
            raise TypeError(
                'Попытка добавить в список сигналов контроллера'
                ' объект не являющийся экземпляром/наследником '
                'класса Signal.'
            )

    def append_location(self, obj):
        if isinstance(obj, Location):
            self.__locations_list.append(obj)
        else:
            raise TypeError(
                'Попытка добавить в список локаций контроллера'
                ' объект не являющийся экземпляром/наследником'
                ' класса Location.'
            )

    def append_position(self, obj):
        if isinstance(obj, Position):
            self.__positions_list.append(obj)
        else:
            raise TypeError(
                'Попытка добавить в список позиций контроллера'
                ' объект не являющийся экземпляром/наследником'
                ' класса Position.'
            )

    def append_device(self, obj):
        if isinstance(obj, Device):
            self.__devices_list.append(obj)
        else:
            raise TypeError(
                'Попытка добавить в список устройств контроллера'
                ' объект не являющийся экземпляром/наследником'
                ' класса Device.'
            )

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$ ОПЕРАЦИИ НАД ОБЪЕКТАМИ В СПИСКАХ $$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def __fill_signals_attribs_with_dict(self):
        """
        Заполнение атрибутов экземпляров сигналов
        по словарю descriptions_types_classes из
        модуля config.
        """
        for signal in self.__signals_list:
            signal.format_name()
            no_translation = True  # станет False при наличии соответствия
            for key in config.descriptions_types_classes:
                if key.lower() in signal.descript.lower():
                    signal.ru_descript = \
                        config.descriptions_types_classes[key][0]
                    signal.signal_type = \
                        config.descriptions_types_classes[key][1]
                    signal.classifier = \
                        config.descriptions_types_classes[key][3]
                    no_translation = False
                    if self.cabinet_category == '2':
                        signal.signal_type_cat2 = \
                            config.descriptions_types_classes[key][2]
                if no_translation:
                    signal.ru_descript = \
                        signal.signal_type = \
                        signal.classifier = \
                        'Неизвестное описание в столбце Description'

    def __fill_positions_signals_lists(self):
        """
        Заполнение signals_list экземпляров
        Position находящихся в self.__positions_list
        ссылками на экземпляры Signal.
        Запись ссылок на экземпляры Position в
        сооветствующие атрибуты экземпляров Signal.
        """
        for position in self.__positions_list:
            for signal in self.__signals_list:
                if signal.position == position.name:
                    position.signals_list.append(signal)
                    signal.position = position

    def __fill_locations_signals_lists_and_position(self):
        """
        Заполнение signals_list экземпляров
        Location находящихся в self.__positions_list
        ссылками на экземпляры Signal.
        Запись ссылок на экземпляры Location в
        сооветствующие атрибуты экземпляров Signal.
        """
        for location in self.__locations_list:
            for signal in self.__signals_list:
                if location.name == signal.location:
                    location.signals_list.append(signal)
                    """
                    Заменим строковое значение атрибута
                    location объекта сигнала полученное из 
                    input_frame ссылкой на соответствующий
                    объект "локации".
                    """
                    signal.location = location
            """
            Проверка допустимости значений в signals_list
            экземпляра Location.
            Установка устанвока необходимых ссылок
            в атрибутах экзмпляра Location и соответствующего
            экземпляра Position на основе заполненного
            signals_list.
            """
            location.position_check_and_set()

    def __fill_counters(self):
        """
        Для каждой позиции:
        Определение количесва счетчиков сигналов
        в смежные системы.
        Опредедение количества счетчиков для
        систем пожаротушений.
        Формирование имен для счетчиков.
        Запись в соответсвующие атрибуты у
        экземпляров Location.
        """
        for position in self.__positions_list:
            conterminal_systems = set()  # все смежные системы на позиции
            fire_fightings = set()  # все пожаротушения на позиции
            for location in position.locations_list:
                # Смежные системы
                if location.conterminal_systems_cntrs is not None:
                    cntrmnl_sstms_lst = location.conterminal_systems_cntrs
                    for conterminal_system in cntrmnl_sstms_lst:
                        conterminal_systems.add(conterminal_system)
                # Пожаротушения
                if location.fire_fightings_cntrs is not None:
                    fr_fghtngs_lst = location.fire_fightings_cntrs
                    for fire_fighting in fr_fghtngs_lst:
                        fire_fightings.add(fire_fighting)

            # словарь для смежных систем
            xsy_uniq_locations = {}
            # ключи - названия смежных систем, значения - "локации"
            for conterminal_system in conterminal_systems:
                xsy_uniq_locations[conterminal_system] = []
                for location in position.locations_list:
                    if location.conterminal_systems_cntrs is not None:
                        if (
                                conterminal_system
                                in
                                location.conterminal_systems_cntrs
                        ):
                            xsy_uniq_locations[conterminal_system].append(
                                location.name
                            )

            # удаляем неуникальные по "локациям" смежные системы
            lst = []
            xsy_uniq_locations_for_iter = xsy_uniq_locations.copy()
            for conterminal_system in xsy_uniq_locations_for_iter:
                lst_of_loc_lsts = xsy_uniq_locations[conterminal_system]
                if xsy_uniq_locations[conterminal_system] in lst:
                    del xsy_uniq_locations[conterminal_system]
                    lst.append(lst_of_loc_lsts)
            xsy_uniq_locations_for_iter.clear()
            lst.clear()

            """
            Замена названий смежных систем из входных
            данных во временном словаре на названия
            счетчиков сигналов в эти смежные системы
            принятые в проекте для дальнейшего использования
            в коде на ST.
            """

            xsy_uniq_locations_for_iter = xsy_uniq_locations.copy()

            # Если счетчиков смежных систем больше одного
            num = 1  # в конце имени каджого добавляется порядковый номер
            if xsy_uniq_locations_for_iter == 1:
                num = ''

            xsy_uniq_locations.clear()
            for conterminal_system in xsy_uniq_locations_for_iter:
                xsy_uniq_locations[
                    f'{position.name}'
                    f'{config.cntrs_dict["Смежные системы"]}_CNT'
                    f'{num}'
                ] = xsy_uniq_locations_for_iter[conterminal_system]
                # добавление в атрибут позиции
                position.xsy_counters.append(
                    f'{position.name}'
                    f'{config.cntrs_dict["Смежные системы"]}_CNT'
                    f'{num}'
                )
                num += 1
            xsy_uniq_locations_for_iter.clear()

            """
            Заполнение атрибутов conterminal_systems_cntrs
            экземпляров Location необходимыми для формирования
            текста программ именами счетчиков сигналов в смежные
            системы.
            """

            for location in position.locations_list:
                # очистка от неактульных значений
                location.conterminal_systems_cntrs = None
                for conterminal_system in xsy_uniq_locations:
                    if (
                            location.name
                            in
                            xsy_uniq_locations[conterminal_system]
                    ):
                        if location.conterminal_systems_cntrs is None:
                            location.conterminal_systems_cntrs = []
                            location.conterminal_systems_cntrs.append(
                                conterminal_system
                            )
                        else:
                            location.conterminal_systems_cntrs.append(
                                conterminal_system
                            )

            # словарь для пожаротушений
            fire_fightings_locations = {}
            # ключи - названия пожаротушений, значения - "локации"
            for fire_fighting in fire_fightings:
                fire_fightings_locations[fire_fighting] = []
                for location in position.locations_list:
                    if location.fire_fightings_cntrs is not None:
                        if (
                                fire_fighting
                                in
                                location.fire_fightings_cntrs
                        ):
                            fire_fightings_locations[fire_fighting].append(
                                location.name
                            )

            """
            Замена названий пожаротушений из входных
            данных во временном словаре на названия
            счетчиков сигналов в эти пожаротушения
            принятые в проекте для дальнейшего
            использования в коде на ST.
            """

            fire_fightings_locations_for_iter = fire_fightings_locations.copy()
            fire_fightings_locations.clear()
            for fire_fighting in fire_fightings_locations_for_iter:
                fire_fightings_locations[
                    f'{position.name}'
                    f'{config.cntrs_dict["Пожары"]}_UPG'
                    f'_{fire_fighting}_CNT'
                ] = fire_fightings_locations_for_iter[fire_fighting]
                # в атрибутах сигналов тоже
                for signal in position.signals_list:
                    if signal.ff_out is not None:
                        for j in range(len(signal.ff_out)):
                            if signal.ff_out[j] == fire_fighting:
                                signal.ff_out[j] = \
                                    f'{position.name}' \
                                    f'{config.cntrs_dict["Пожары"]}_UPG' \
                                    f'_{fire_fighting}_CNT'
                # добавление в атрибуты экземпляра позиции
                position.upg_counters.append(
                    f'{position.name}'
                    f'{config.cntrs_dict["Пожары"]}_UPG'
                    f'_{fire_fighting}_CNT'
                )
                # для использования в именах других счетчиков
                # в срабатывании которых будут участвовать
                # сигналы с тушением
                position.upg_markers.append(fire_fighting)
            fire_fightings_locations_for_iter.clear()

            """
            Заполнение атрибутов fire_fightings_cntrs
            экземпляров Location необходимыми для формирования
            текста программ именами счетчиков сигналов в
            пожаротушения.
            """

            for location in position.locations_list:
                # очистка от неактульных значений
                location.fire_fightings_cntrs = None
                for fire_fighting in fire_fightings_locations:
                    if (
                            location.name
                            in
                            fire_fightings_locations[fire_fighting]
                    ):
                        if location.fire_fightings_cntrs is None:
                            location.fire_fightings_cntrs = []
                            location.fire_fightings_cntrs.append(
                                fire_fighting
                            )
                        else:
                            location.fire_fightings_cntrs.append(
                                fire_fighting
                            )

    def input_data_reformation(self):
        """
        Обработка данных полученных при выполнении
        функции read() из модуля read_input.
        "Взведение" флагов, указывающих на то,
        какие именно операции по обработке данных
        были выполнены.
        """
        if self.signals_list_filled:
            self.__fill_signals_attribs_with_dict()
            self.__fill_positions_signals_lists()
            self.signals_reformed = True
            if self.ce_locations_filled:
                self.__fill_locations_signals_lists_and_position()
                self.__fill_counters()
                self.locations_reformed = True

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$ ПРОВЕРКА ГОТОВНОСТИ К ФОРМИРОВАНИЮ ПРОГРАММ $$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def ready_for_counting(self):
        if self.__signals_list.contains_signals_ready_for_counting():
            return True

    def ready_for_alarming(self):
        if (
                self.ready_for_counting()
                and
                self.__signals_list.contains_signals_for_alarming()
        ):
            return True
        else:
            return False

    def ready_for_xl_xla(self):
        if (
                self.__signals_list.contains_signals_for_xl_xla()
                and
                self.signals_reformed
        ):
            return True
        else:
            return False

    def ready_for_hs_os(self):
        if (
                self.__signals_list.contains_signals_for_hs_os()
                and
                self.signals_reformed
        ):
            return True
        else:
            return False

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$ ФОРМИРОВАНИЕ ТЕКСТОВ ПРОГРАММ $$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def xl_xla(self):
        if self.ready_for_xl_xla():
            txt = open(fr'{self.output_path}\XL_XLA.txt', 'w')
            # txt.close()
            for position in self.__positions_list:
                if position.signals_list.contains_signals_for_xl_xla:
                    # txt = open(fr'{self.output_path}\XL_XLA.txt', 'a')
                    txt.write(f'{position.name_for_comment}\n')
                    position.signals_list.xl_xla_write(txt)
                    txt.write('\n')
                    txt.close()

    def hs_os(self):
        if self.ready_for_hs_os():
            txt = open(fr'{self.output_path}\HS_OS.txt', 'w')
            for position in self.__positions_list:
                if position.signals_list.contains_signals_for_hs_os:
                    txt.write(f'{position.name_for_comment}\n')
                    position.signals_list.hs_os_write(txt)
                    txt.write('\n')
                    txt.close()

    def alarming(self):
        if self.ready_for_alarming():
            txt = open(fr'{self.output_path}\Alarming.txt', 'w')
            for position in self.__positions_list:
                if position.has_any_warnings():
                    warning_part = f' OR {position.name}XWRX_CNT > 0'
                else:
                    warning_part = ''
                txt.write(f'{position.name_for_comment}\n')
                position.signals_list.alarming_write(
                    txt,
                    warning_part,
                )
                txt.write('\n')
                txt.close()

    def counting(self):
        if self.ready_for_counting():
            txt = open(fr'{self.output_path}\Counting.txt', 'w')
            for position in self.__positions_list:
                if position.signals_list.contains_signals_ready_for_counting():
                    txt.write(f'{position.name_for_comment}\n')
                    position.counting_write(txt)
                txt.write('\n')
                txt.close()

    def weintek(self):
        pass

    def mops_mups(self):
        pass

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$ ВЫВОД НА ЭКРАН $$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def print_signals(self):
        print(f'Сигналы контроллера {self.name}:')
        self.__signals_list.print_signals()

    def print_locations(self):
        print(f'Локации контроллера {self.name}:')
        for location in self.__locations_list:
            voting_logic = \
                f'{location.voting_logic[0]} ' \
                f'из {location.voting_logic[1]}' \
                if location.voting_logic is not None \
                else None
            print(
                f'\nИмя локации:'
                f' {location.name}\n'
                f'Позиция "локации":'
                f' {location.position.name}\n'
                f'Счетчик вниманий:'
                f' {location.warning_cntr}\n'
                f'Счетчик пожаров:'
                f' {location.fire_cntr}\n'
                f'Счетчики пожаротушений:'
                f' {location.fire_fightings_cntrs}\n'
                f'Счетчики смежных систем:'
                f' {location.conterminal_systems_cntrs}\n'
                f'Логика срабатывания:'
                f' {voting_logic}'
            )
