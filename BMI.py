user_weight = float(input("您的体重（单位：kg）为："))
user_height = float(input("您的身高（单位：cm）为："))
user_BMI = user_weight / (user_height/100) ** 2
print(f"您的BMI值为：{user_BMI}")

if user_BMI < 16 or user_BMI > 60:
    print("请检查数据是否有有误。")
elif 16 <= user_BMI < 18.5:
    print("您的BMI标准为偏瘦。")
elif 18.5 <= user_BMI < 24:
    print("您的BMI标准为正常。")
elif 24 <= user_BMI < 27:
    print("您的BMI标准为过重。")
elif 27 <= user_BMI:
    if 27 <= user_BMI < 30:
        type = "I度"
    elif 30 <= user_BMI < 40:
        type = "II度"
    else:
        type = "III度"
    print(f"您的BMI标准为{type}肥胖。")