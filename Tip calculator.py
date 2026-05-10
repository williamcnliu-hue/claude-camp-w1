# 小费计算器 - 多道菜小费 & 账单计算
bill = float(input("请输入餐费金额（美元）: "))
tip_percent = float(input("请输入小费比例（如 18 代表 18%）: "))
people = int(input("请输入用餐人数: "))

tip = bill * tip_percent / 100
total = bill + tip
per_person = total / people

print(f"餐费: ${bill:.2f}")
print(f"小费 ({tip_percent}%): ${tip:.2f}")
print(f"总金额: ${total:.2f}")
print(f"每人应付: ${per_person:.2f}")