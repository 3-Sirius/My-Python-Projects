sumnum = 0 #总和
quantity = 0 #数字总数
num = input("请输入需要计算平均数的数字（输入结束时请输入p）：")
while num != "p":
    sumnum += float(num)
    quantity += 1
    num = input("请输入需要计算平均数的数字（输入结束时请输入p）：")
else:
    if quantity == 0:
        print("这些数字的平均数为0")

    else:
        answer = sumnum / quantity
        print(f"这些数字的平均数为{answer}")