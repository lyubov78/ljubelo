money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

budget_balance = money_capital + salary - spend

months = 1

while budget_balance >= spend:
    if money_capital == 20000:
        budget_balance = money_capital + salary - spend
        money_capital = budget_balance
    else:
        spend = spend + spend * increase
        budget_balance = money_capital + salary - spend
        money_capital = budget_balance
    months = months + 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
