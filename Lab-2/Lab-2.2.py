salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
capital = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
capital -= spend - salary
for i in range(1,10):
        spend *= (1 + increase)
        capital -= spend
        capital += salary
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(capital * (-1)) )