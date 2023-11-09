import math

# 获取仪器量程
range_input = input("请输入仪器的精确度：")
range_value = float(range_input)

# 计算仪器不确定度
instrument_uncertainty = range_value / math.sqrt(3)

# 输入测量次数
n = int(input("请输入测量次数："))

# 输入各组数据
data = []
for i in range(n):
    data_input = float(input("请输入第{}组数据：".format(i + 1)))
    data.append(data_input)

# 计算平均值和标准差
mean = sum(data) / n
variance = sum((x - mean) ** 2 for x in data) / (n - 1)
standard_deviation = math.sqrt(variance)

# 输入修正因子
tp_input = float(input("请输入修正因子tp："))
tp = tp_input

# 计算A类不确定度
a_class_uncertainty = tp * standard_deviation

# 计算总不确定度
total_uncertainty = math.sqrt(a_class_uncertainty ** 2 + instrument_uncertainty ** 2)

print("仪器不确定度：", instrument_uncertainty)
print("A类不确定度：", a_class_uncertainty)
print("总不确定度：", total_uncertainty)
