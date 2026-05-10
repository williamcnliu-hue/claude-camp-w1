# 个性化问候语
name = input("请输入您的姓名: ")
age  = int(input("请输入您的年龄: "))

greeting = f"您好，{name}！您今年 {age} 岁。"

if age < 18:
    greeting += " 祝您学业进步！"
elif age < 60:
    greeting += " 祝您工作顺利！"
else:
    greeting += " 祝您身体健康！"

print(greeting)