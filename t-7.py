# Заданные функции eq, gr, ls, ge, le, ne и filter_rows
from operator import ge, le, ne


def eq(column1, column2):
    return [val1 == val2 for val1, val2 in zip(column1, column2)]

# ... (остальные функции gr, ls, ge, le, ne и filter_rows)

def filter_rows(bool_list, table, copy_table=False):
    if copy_table:
        table = [row.copy() for row in table]

    return [row for row, keep in zip(table, bool_list) if keep]

# Пример данных
column1 = [5, 7, 9, 8]
column2 = [8, 7, 9, 5]

# Применение функций для сравнения столбцов
eq_result = eq(column1, column2)


def gr(column1, column2):
    pass


gr_result = gr(column1, column2)


def ls(column1, column2):
    pass


ls_result = ls(column1, column2)
ge_result = ge(column1, column2)
le_result = le(column1, column2)
ne_result = ne(column1, column2)

# Ваша таблица данных (предположим, что это ваша таблица)
table = [
    [5, 8, 1],
    [7, 7, 2],
    [9, 9, 3],
    [8, 5, 4]
]

# Применение фильтрации строк на основе результата сравнения
bool_list = eq_result  # Можно выбрать любой результат сравнения
filtered_table = filter_rows(bool_list, table)

# Вывод результатов
print("Равный:", eq_result)
print("Больший:", gr_result)
print("Меньший:", ls_result)
print("Больше или равно:", ge_result)
print("Меньше или равно:", le_result)
print("Не равно:", ne_result)

print("Финальная таблица:", filtered_table)