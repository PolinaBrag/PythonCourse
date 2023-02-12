# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список

balance = 0

def add_to_balance(user_balance):
    pass

def charge_off_balance(user_balance):
    pass

exit_choice = False
while not exit_choice:
    menu_choice = int(input(
        "Выберите пункт меню в формате цифры:" + "\n"
        + "1. Пополнить счет" + "\n"
        + "2. Снять деньги" + "\n"
        + "3. Выход" + "\n"))
    if menu_choice == 1:
        add_to_balance(balance)
    elif menu_choice == 2:
        charge_off_balance(balance)
    elif menu_choice == 3:
        pass
        #exit_choice == True

