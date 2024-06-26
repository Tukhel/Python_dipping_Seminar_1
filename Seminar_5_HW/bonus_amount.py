# Напишите однострочный генератор словаря, который принимает на вход
# три списка одинаковой длины: имена str, ставка int, премия str с указанием
# процентов вида “10.25%”. В результате получаем словарь с именем в качестве
# ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка
# умноженная на процент премии

names: list[str] = ["Alice", "Bob", "Charlie"]
salary: list[int] = [5000, 6000, 7000]
bonus: list[str] = ["10%", "5%", "15%"]


result = {names[i]: round(salary[i] * float(bonus[i].strip('%')) / 100, 2)
          for i in range(len(names))}
print(result)
