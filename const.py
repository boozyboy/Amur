# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@ ============================================================== @@@
# @@@ ============= СЛОВАРЬ ДЛЯ ЧТЕНИЯ ВХОДНЫХ ДАННЫХ ============== @@@
# @@@ ============================================================== @@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

descriptions_types_classes_label = \
    ' @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' \
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n' \
    ' @@@ ===============================' \
    '=============================== @@@\n' \
    ' @@@ ============= СЛОВАРЬ ДЛЯ ЧТЕНИЯ ' \
    'ВХОДНЫХ ДАННЫХ ============== @@@\n' \
    ' @@@ ===============================' \
    '=============================== @@@\n' \
    ' @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' \
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n' \

descriptions_types_classes_marker = '%descriptions_types_classes%'
descriptions_types_classes_text = \
    'Словарь описаний, типов и классификаторов объекта для\n' \
    'сигналов шкафов автоматики СТБ. Ключ - подстрока из\n' \
    'стандартных описаний на английском, нужен для\n' \
    'сопоставления со входными данными.\n' \
    'Первый элемент в списке - описание на русском.\n' \
    'Второй - тип объекта.\n' \
    'Третий - тип объекта для шкафов второй категории.\n' \
    'Четвертый - классификатор объекта.\n' \
    f'{descriptions_types_classes_marker}\n' \
    'Manual Call Point: ' \
    'Ручной извещатель, BTM, BTM_R, HS\n' \
    'Stop Button: ' \
    'Кнопка останова, SB, SB_R, SB\n' \
    'Abort Switch: ' \
    'Кнопка отмены тушения, SB, SB_R, SB\n' \
    'Auto/Manual Selector Switch: ' \
    'Переключатель режимов автоматики, SB, SB_R, SB\n' \
    'Remote Start Push Button: ' \
    'Дист. пуск тушения, SB, SB_R, SB\n' \
    'Smoke Detector: ' \
    'Дымовой извещатель, BTH, BTH_R, OS\n' \
    'Heat Detector: ' \
    'Тепловой извещатель, BTK, BTK_R, TS\n' \
    'Gas Exting. Leave Now Light: ' \
    'Световое табло "Газ уходи", HL, HL_R, XL\n' \
    'Gas Exting. Do Not Enter Light: ' \
    'Световое табло "Газ не входи", HL, HL_R, XL\n' \
    'Automation Off Light: ' \
    'Световое табло "Автоматика отключена", HL, HL_R, XL\n' \
    'Beacon (Fire): ' \
    'Оповещатель (Пожар), HL, HL_R, XL\n' \
    'Exit Light: ' \
    'Световое табло "Выход", HL, HL_R, XL\n' \
    'Exit Light And Fire Audible Alarm: ' \
    'Светозвуковое табло "Выход", HL, HL_R, XLA\n' \
    'Fire Light And Audible Alarm: ' \
    'Светозвуковое табло "Пожар", HL, HL_R, XLA\n' \
    'Sounder (Fire): ' \
    'Звуковой оповещатель, HA, HA_R, XA\n' \
    'Solenoid Valve: ' \
    'Соленоидный клапан, UPT, HL_R, PT\n' \
    'Pressure Switch: ' \
    'Датчик давления, SB, SB_R, PT\n' \
    'Magnetic Door Contact: ' \
    'Концевик двери, SQ, SQ_R, PT\n' \
    'Flame Detector: ' \
    'Извещатель пламени, BTF, BTF_R, BT\n' \
    f'{descriptions_types_classes_marker}\n\n'

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@ ============================================================== @@@
# @@@ ================= HS_OS, ALARMING, XL_XLA ==================== @@@
# @@@ ============================================================== @@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

hs_os_alarming_xl_xla_label = \
    ' @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' \
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n' \
    ' @@@ ===============================' \
    '=============================== @@@\n' \
    ' @@@ ================= HS_OS, ALARMI' \
    'NG, XL_XLA ==================== @@@\n' \
    ' @@@ ===============================' \
    '=============================== @@@\n' \
    ' @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' \
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n' \

hs_os_for_marker = '%hs_os_for%'
hs_os_for_text = \
    'Список классификаторов сигналов, которые должны\n' \
    'участвовать в программе hs_os.\n' \
    f'{hs_os_for_marker}\n' \
    'HS, OS, TS, BT, PT, SQ, SB\n' \
    f'{hs_os_for_marker}\n\n'

alarming_for_marker = '%alarming_for%'
alarming_for_text = \
    'Список классификаторов сигналов, которые должны\n' \
    'участвовать в программе alarming.\n' \
    f'{alarming_for_marker}\n' \
    'XL, XLA\n' \
    f'{alarming_for_marker}\n\n'

xl_xla_for_marker = '%xl_xla_for%'
xl_xla_for_text = \
    'Список классификаторов сигналов, которые должны\n' \
    'участвовать в программе xl_xla.\n' \
    f'{xl_xla_for_marker}\n' \
    'XL, XLA\n' \
    f'{xl_xla_for_marker}\n\n'

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@ ============================================================== @@@
# @@@ ========================== COUNTING ========================== @@@
# @@@ ============================================================== @@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

counting_label = \
    ' @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' \
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n' \
    ' @@@ ===============================' \
    '=============================== @@@\n' \
    ' @@@ ========================== COUNT'\
    'ING ========================== @@@\n' \
    ' @@@ ================================'\
    '============================== @@@\n' \
    ' @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'\
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n'

cntrs_dict_marker = '%cntrs_dict%'
cntrs_dict_cnfg_text = \
    'Словарь для классификации счетчиков. Ключи - назначения\n' \
    'счетчиков на русском, значения - принятые в проекте\n' \
    'отличительные части названий для счетчиков.\n' \
    f'{cntrs_dict_marker}\n' \
    'Смежные системы: XSY\n' \
    'Пожары: XFRX\n' \
    'Имитации: XCIM\n' \
    'Ремонты: XRPX\n' \
    'Неисправности: FXXX\n' \
    'Недостоверности: DVXX\n' \
    'Внимания: XWRX\n' \
    f'{cntrs_dict_marker}\n\n' \

buttons_counting_for_marker = '%buttons_counting_for%'
buttons_counting_for_cnfg_text = \
    'Список классификаторов сигналов ручных извещателей,\n' \
    'которые должны участвовать в программе counting.\n' \
    f'{buttons_counting_for_marker}\n' \
    'HS, SB\n' \
    f'{buttons_counting_for_marker}\n\n'

sensors_counting_for_marker = '%sensors_counting_for%'
sensors_counting_for_cnfg_text = \
    'Список классификаторов сигналов сенсорных датчиков,\n' \
    'которые должны участвовать в программе counting.\n' \
    f'{sensors_counting_for_marker}\n' \
    'OS, TS, BT\n' \
    f'{sensors_counting_for_marker}\n\n'

actuators_counting_for_marker = '%actuators_counting_for%'
actuators_counting_for_cnfg_text = \
    'Список классификаторов сигналов исполнительного оборудования,\n' \
    'которое должно участвовать в программе counting.\n' \
    f'{actuators_counting_for_marker}\n' \
    'XL, XLA, PT\n' \
    f'{actuators_counting_for_marker}\n\n'

config_file_text = [
    descriptions_types_classes_label,
    descriptions_types_classes_text,
    hs_os_alarming_xl_xla_label,
    hs_os_for_text,
    alarming_for_text,
    xl_xla_for_text,
    counting_label,
    cntrs_dict_cnfg_text,
    buttons_counting_for_cnfg_text,
    sensors_counting_for_cnfg_text,
    actuators_counting_for_cnfg_text,
]
