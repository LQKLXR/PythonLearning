def compute(weight, height):
    bmi = weight / (height * height)
    print("您的 BMI 指数为：" + str(bmi))
    if bmi < 18.5:
        print("体重过轻")
    elif 18.5 <= bmi < 24.9:
        print("体重良好，继续保持")
    elif 24.9 <= bmi < 29.9:
        print("体重过重")
    elif 29.9 <= bmi:
        print("肥胖")


if __name__ == '__main__':
    height = float(input("请输入您的身高(cm)：")) / 100
    weight = float(input("请输入您的体重(kg)："))
    compute(weight, height)