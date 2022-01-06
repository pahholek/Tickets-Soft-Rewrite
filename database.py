from typing import List, TextIO


def add_ticket(id, print_date, price, price_unit, used_date_computable):
    # import os and check if directories are there
    import os
    if os.path.exists('data'):
        pass
    else:
        os.mkdir('data')

    if os.path.exists('data/base'):
        pass
    else:
        os.mkdir('data/base')

    # open files in append mode and add information to them
    files = [
        open('data/base/id.txt', 'a'),  # 0
        open('data/base/print_date.txt', 'a'),  # 1
        open('data/base/price.txt', 'a'),  # 2
        open('data/base/price_unit.txt', 'a'),  # 3
        open('data/base/used_date_computable.txt', 'a'),  # 4
    ]
    files[0].write(str(id))
    files[1].write(str(print_date))
    files[2].write(str(price))
    files[3].write(str(price_unit))
    files[4].write(str(used_date_computable))
    for i in range(len(files)):
        files[i].write('\n')
        files[i].close()


def get_records():
    # import os and check if directories are there
    import os
    if os.path.exists('data'):
        pass
    else:
        os.mkdir('data')
    if os.path.exists('data/base'):
        pass
    else:
        os.mkdir('data/base')

    # open files in append mode and add information to them
    try:
        files = [
            open('data/base/id.txt', 'r'),  # 0
            open('data/base/print_date.txt', 'r'),  # 1
            open('data/base/price.txt', 'r'),  # 2
            open('data/base/price_unit.txt', 'r'),  # 3
            open('data/base/used_date_computable.txt', 'r'),  # 4
        ]
        lines = [
            files[0].read().splitlines(),
            files[1].read().splitlines(),
            files[2].read().splitlines(),
            files[3].read().splitlines(),
            files[4].read().splitlines()
        ]
    except:
        return
    exit_value = []
    for i in range(len(lines[0])):
        exit_value.append([lines[0][i], lines[1][i], lines[2][i], lines[3][i], lines[4][i]])
    print(exit_value)
    for i in range(len(files)):
        files[i].close()
    return exit_value
