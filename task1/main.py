import pulp

model = pulp.LpProblem(name="production-optimization", sense=pulp.LpMaximize)

lemonade = pulp.LpVariable(name="lemonade", lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable(name="fruit_juice", lowBound=0, cat='Continuous')

model += pulp.lpSum([lemonade, fruit_juice]), "Total_Products"

model += (2 * lemonade + fruit_juice <= 100), "Water_Constraint"
model += (lemonade <= 50), "Sugar_Constraint"
model += (lemonade <= 30), "Lemon_Constraint"
model += (2 * fruit_juice <= 40), "Fruit_Puree_Constraint"

model.solve()

print(f"Оптимальне виробництво Лимонаду: {lemonade.varValue}")
print(f"Оптимальне виробництво Фруктового соку: {fruit_juice.varValue}")
print(f"Загальна кількість вироблених продуктів: {pulp.value(model.objective)}")
