# Написати програму, що вирішує виділені овалами задачі. Старатись кожну задачу описати функцією, яку нижче викликати
# 1163


def watermelon(total, first_day_diff, second_day_diff):
    result = total - (total / first_day_diff) - ((total / first_day_diff) + second_day_diff)
    return result


watermelon_balance = watermelon(600, 6, 27)
print(f"Залишилось {watermelon_balance} кг кавунів.")


# 1166
def seeds(total, seed_ratio):
    result = total / seed_ratio
    return result


the_seeds = seeds(244, 2)
print(f"Одержали {the_seeds} кг насіння.")


# 1168
def usage(normal_usage, days, new_usage):
    total_charcoal = normal_usage * days
    result = round(total_charcoal / new_usage)
    return result


eco_usage = usage(9, 72, 8)
print(f"Якщо щодня витрачати по 8 кг вугілля, то його вистачить на {eco_usage} днів.")


# 1169
def acorn(quantity_per_kg, kg, flaw):
    sowing = quantity_per_kg * kg
    result = round(sowing / 100) * (100 - flaw)
    return result


acorn_success = acorn(300, 2, 10)

print(f"Зійшло {acorn_success} саджанців дуба.")


# 1172
def dry_fruit(fruit, shrinkage):
    result = fruit / shrinkage
    return result


dry = dry_fruit(322, 2)
print(f"Вийшло {dry} кг сухих плодів шипшини.")