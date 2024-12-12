import csv
from typing import Callable, List, Any


def hierarchy_departments(data: List[List[str]]) -> None:
    """
    Display the hierarchy of departments and their corresponding commands.

    Args:
        data: List[List[str]]: List of lists representing the data from csv.

    Returns:
        None
    """
    unique_department_commands = set()
    hierarchy_tree = dict()
    for row in data[1:]:
        unique_department_commands.add((row[1], row[2]))
    for dep, com in unique_department_commands:
        hierarchy_tree[dep] = []
    for dep, com in unique_department_commands:
        if com not in hierarchy_tree[dep]:
            hierarchy_tree[dep].append(com)
    for dep, com in hierarchy_tree.items():
        print('Департамент:', dep)
        print('Команды:')
        print(*com, sep=', ')
        print()
    return


def consolidated_report_department(data: List[List[str]]) -> List[List[Any]]:
    """
    Generate a consolidated report for each department and display it,
    including information about:
    1)Name of department
    2)Count of employees
    3)Minimum of salary
    4)Maximum of salary
    5)Average of salary

    Args:
        data (List[List[Any]]): List of lists representing the data from csv.

    Returns:
        List[List[Any]]: A list of lists containing the consolidated report.
    """
    unique_department = set()
    cons_dict_num = dict()
    cons_dict_temp = dict()
    cons_dict_salary = dict()
    for row in data[1:]:
        unique_department.add(row[1])
    for dep in unique_department:
        cons_dict_num[dep] = 0
        cons_dict_temp[dep] = []
    for dep in unique_department:
        for row in data[1:]:
            if row[1] == dep:
                cons_dict_num[dep] += 1
                cons_dict_temp[dep].append(int(row[5]))
    for dep, sal in cons_dict_temp.items():
        cons_dict_salary[dep] = [cons_dict_num[dep],
                                 min(sal), max(sal),
                                 sum(sal)/cons_dict_num[dep]]

    data_to_upload = []
    for dep, elem in cons_dict_salary.items():
        data_to_upload.append([dep] + elem)
        print('Департамент:', dep)
        print('Количество сотрудников:', elem[0])
        print('Минимальная - Максимальная:', elem[1], '-', elem[2])
        print('Средняя:', round(elem[3], 2))
        print()
    return data_to_upload


def write_report_csv(name_function: Callable, data: List[List[Any]]) -> None:
    """
    Write a consolidated report to a new CSV file.

    Args:
        name_function (Callable): The function used to generate the report.
        data (List[List[Any]]): List of lists representing the data.

    Returns:
        None
    """
    data_temp = name_function(data)
    label_column = [['Департамент', 'Количество сотрудников',
                    'Минимальная', 'Максимальная', 'Средняя']]
    data_upload = label_column + data_temp
    with open('Consolidated_summary.csv', 'w', newline='') as cons_sum:
        writer = csv.writer(cons_sum)
        for row in data_upload:
            writer.writerow(row)
    return


if __name__ == '__main__':
    option = ''
    options = ['1', '2', '3']
    while option not in options:
        print('Выберите: {} или {} или {}'.format(*options))
        option = input()
    with open('Corp_Summary.csv', 'r', newline='') as corp_summary_file:
        reader = csv.reader(corp_summary_file, delimiter=';')
        all_data = list(reader)

        if option == '1':
            hierarchy_departments(all_data)
        elif option == '2':
            consolidated_report_department(all_data)
        else:
            write_report_csv(consolidated_report_department, all_data)
