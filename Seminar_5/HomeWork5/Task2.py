# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

def dict_maker(str_names: list[str], int_list: list[int], percents: list[str]) -> dict:
    res_dict = {name: val * (float(percent.replace('%', ''))/100) for name, val, percent in
                zip(str_names, int_list, percents)}
    return res_dict


res = dict_maker(['Andy', 'Garry', 'Bob'], [20000, 50000, 30000], ['10.25%', '5%', '9%'])
print(res)