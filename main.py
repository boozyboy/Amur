import tiger
import read_input as inp
from menu import menu

line = '\n\n'+'-' * 100
while True:

    try:

        plc = inp.read()
        plc.input_data_reformation()
        menu(plc)

    except FileNotFoundError as e:
        print(
            'ОШИБКА!\n\n',
            e,
            '\n\nНажмите любую клавишу, повторите '
            f'ввод пути до input.xlsx{line}'
        )

    except Exception as e:
        print(
            'ОШИБКА!\n\n',
            e.__class__,
            e,
            f'{line}'
        )

    input()
