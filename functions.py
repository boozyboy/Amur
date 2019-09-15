def del_last_space(x):
    if x[-1] != ' ':
        return x
    else:
        return x[0:-1]


def format_position(position):
    """
    Функция преобразует название
    позиции в вид необходимый
    для формирования кода ST программ
    """
    frmt_position = position.replace('-', '_').replace(' ', '')
    if frmt_position[0] != 'P':
        frmt_position = 'P' + frmt_position + '_'
    return frmt_position


def format_plc_name(plc_name):
    """
    Функция преобразует имя ПЛК в вид
    необходимый для проекта в SCADA текон
    """
    frmt_plc_name = plc_name.replace('-', '_').replace(' ', '')
    if frmt_plc_name[0:4] != 'PLC_':
        frmt_plc_name = 'PLC_' + frmt_plc_name
    return frmt_plc_name
