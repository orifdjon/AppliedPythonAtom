from .data_verifier import is_valid_data
from .creator_of_data import to_comfort_format


class PrinterData:

    def __init__(self, lencols):
        self.lencols = lencols
        # у каждой колонки 5 доп.символов: | и 4 ' '
        # плюс в конце еще |
        self.lenline = sum(self.lencols) + 5 * len(self.lencols) + 1

    def print_hat(self, elems):
        for ind in range(len(elems)):
            start_after = (self.lencols[ind] - len(str(elems[ind]))) // 2

            left_board = '|  ' + ' ' * start_after
            rigth_board = ' ' * (self.lencols[ind] -
                                 start_after - len(str(elems[ind])))

            print(left_board + str(elems[ind]) + rigth_board, end='  ')
        print('|')

    def print_lines(self, data):
        for elems in data:
            # заполняем все до предпоследнего
            for ind in range(len(elems) - 1):
                start_after = (self.lencols[ind] - len(str(elems[ind]))) // 2

                left_board = '|  ' +\
                             ' ' * start_after
                rigth_board = ' ' * (self.lencols[ind] -
                                     start_after - len(str(elems[ind])))

                print(left_board + str(elems[ind]) + rigth_board, end='  ')

            # а теперь последняя колонка
            start_after = (self.lencols[ind] - len(str(elems[-1])))
            print('|  ' + ' ' * start_after + str(elems[-1]), end='  ')
            print('|')

    def __enter__(self):
        print('-' * self.lenline)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('-' * self.lenline)
        # if exc_val:
        #     raise UnboundLocalError


def count_cols_len(hat, data):
    res = [len(str(h)) for h in hat]
    for dd in data:
        lens = [len(str(d)) for d in dd]
        res = [max(x, y) for x, y in zip(res, lens)]
    return res


def create_table(data):
    is_valid_data(data)
    hat, data = to_comfort_format(data)

    pd = PrinterData(count_cols_len(hat, data))
    with pd:
        pd.print_hat(hat)
        pd.print_lines(data)
