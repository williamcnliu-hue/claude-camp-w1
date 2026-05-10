# BMI 计算器 - 计算身体质量指数
weight = float(input("请输入您的体重（公斤）: "))
height = float(input("请输入您的身高（米，例如 1.75）: "))

bmi = weight / (height ** 2)

print(f"您的 BMI 是: {bmi:.2f}")

if bmi < 18.5:
    print("健康建议: 偏瘦，注意营养均衡。")
elif bmi < 24:
    print("健康建议: 正常，继续保持！")
elif bmi < 28:
    print("健康建议: 偏胖，建议适度运动。")
else:
    print("健康建议: 肥胖，建议咨询医生。")