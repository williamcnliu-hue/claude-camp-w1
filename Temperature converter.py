# 温度转换器 - 摄氏度 ↔ 华氏度
print("1: 摄氏度 → 华氏度")
print("2: 华氏度 → 摄氏度")

choice = input("请选择转换方向（1 或 2）: ")
temp = float(input("请输入温度数值: "))

if choice == "1":
    result = temp * 9 / 5 + 32
    print(f"{temp}°C = {result}°F")
elif choice == "2":
    result = (temp - 32) * 5 / 9
    print(f"{temp}°F = {result}°C")
else:
    print("输入错误，请输入 1 或 2")