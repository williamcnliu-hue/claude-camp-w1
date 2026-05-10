# 简单密码生成器
import random
import string

length = int(input("请输入密码长度（建议 12 以上）: "))

# 字符池：大小写字母 + 数字 + 符号
characters = string.ascii_letters + string.digits + string.punctuation

# 随机抽 length 个字符拼起来
password = "".join(random.choice(characters) for _ in range(length))

print(f"生成的密码: {password}")