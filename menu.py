import sys


def menu(plc):

    line = '-' * 100 + '\n'

    # В каждом подсписке:
    # [0] - название операции
    # [1] - условие для возможности ее выполнения
    # [2] - операция
    operations = [
        [
            'Вывести все сигналы на экран',
            plc.signals_reformed,
            plc.print_signals,
        ],
        [
            'Вывести все локации на экран',
            plc.locations_reformed,
            plc.print_locations,
        ],
        [
            'Сформировать HS_OS.txt',
            plc.ready_for_hs_os(),
            plc.hs_os,
        ],
        [
            'Сформировать XL_XLA.txt',
            plc.ready_for_xl_xla(),
            plc.xl_xla,
        ],
        [
            'Сформировать Alarming.txt',
            plc.ready_for_alarming(),
            plc.alarming,
        ],
        [
            'Сформировать Counting.txt',
            plc.ready_for_counting(),
            plc.counting
        ],
        [
            'Вывести инструкцию на экран',
            True,
            print,
        ],
        [
            'Изменить директорию для выходных файлов\n\t'
            '(по умолчанию та же, что у input.xlsx)',
            True,
            plc.change_output_path,
        ],
        [
            'Выход',
            True,
            sys.exit
        ],
    ]

    available_operations = {}
    operation_num = 1
    for lst in operations:
        if lst[1]:
            available_operations[operation_num] = []
            available_operations[operation_num] += lst[0:3]
            operation_num += 1

    while True:

        print('\tВведите через пробел номера необходимых операций:\n')

        for key in range(len(available_operations)):
            print(f'{key+1}.\t{available_operations[key+1][0]}')

        choice = input().split()

        if (

            int(choice[0]) in available_operations
            and
            available_operations[int(choice[0])][0] != 'Выход'

        ):
            print('\n'+line)

        elif int(choice[0]) not in available_operations:
            print('\n' + line)

        for key in (int(n) for n in choice):

            # Операции требующие обработки не по шаблону
            if key not in available_operations.keys():
                print(f'{key} - неизветная операция!')

            elif available_operations[key][0] == 'Выход':
                available_operations[key][2]()

            elif available_operations[key][0] == \
                'Изменить директорию для выходных файлов\n\t' \
                    '(по умолчанию та же, что у input.xlsx)':
                available_operations[key][2]()

            elif available_operations[key][0] == \
                    'Вывести инструкцию на экран':
                available_operations[key][2]('Инструкция')
                input('\nДля продолжения нажмите любую клавижу')

            # Шаблон для выполнения операций
            elif available_operations[key][1]:
                print(
                    f'Выполняется операция '
                    f'"{available_operations[key][0]}"'
                )
                try:
                    available_operations[key][2]()
                    print(
                        '\nУСПЕХ!\n'
                        f'\nОперация "{available_operations[key][0]}"'
                        ' выполнена!'
                    )
                except Exception as e:
                    print(
                        '\nОШИБКА!\n\n',
                        e.__class__,
                        e,
                        f'\n\nОперация "{available_operations[key][0]}"'
                        ' НЕ выполнена!'
                    )

            print(f'\n{line}')
