import math

# 获取直接测量量的个数
num_direct_measurements = int(input("请输入直接测量量的个数："))

# 初始化直接测量量和对应的不确定度
direct_measurements = []
direct_measurement_uncertainties = []

# 获取直接测量量的名称和数据
for i in range(num_direct_measurements):
    measurement_name = input("请输入第{}个直接测量量的名称：".format(i+1))
    measurements = []
    num_measurements = int(input("请输入{}的测量次数：".format(measurement_name)))
    for j in range(num_measurements):
        measurement = float(input("请输入{}的第{}次测量数据：".format(measurement_name, j+1)))
        measurements.append(measurement)
    direct_measurements.append(measurements)

    # 计算直接测量量的不确定度
    measurement_range = float(input("请输入{}的量程：".format(measurement_name)))
    b_uncertainty = measurement_range / math.sqrt(3)
    direct_measurement_uncertainties.append(b_uncertainty)

    # 计算A类不确定度
    mean = sum(measurements) / num_measurements
    ua = math.sqrt(sum([(x - mean) ** 2 for x in measurements]) / (num_measurements * (num_measurements - 1)))
    tp = float(input("请输入{}的修正因子tp：".format(measurement_name)))
    a_uncertainty = tp * ua

    # 计算间接测量量对直接测量量的不确定度
    for k in range(num_measurements):
        partial_derivative = float(input("请输入间接测量量公式对{}的偏导数：".format(measurement_name)))
        indirect_measurement_uncertainty = partial_derivative * a_uncertainty
        direct_measurement_uncertainties[i] = math.sqrt(direct_measurement_uncertainties[i] ** 2 + indirect_measurement_uncertainty ** 2)

# 计算总不确定度
total_uncertainty = math.sqrt(sum([uncertainty ** 2 for uncertainty in direct_measurement_uncertainties]))

# 输出结果
print("直接测量量的不确定度：", direct_measurement_uncertainties)
print("总不确定度：", total_uncertainty)
