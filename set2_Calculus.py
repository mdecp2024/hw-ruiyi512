import math

def calculate_population_time(initial_population, final_population, doubling_time):
    # 使用變換公式計算時間
    time_required = doubling_time * (math.log10(final_population / initial_population) / math.log10(2))
    return time_required

# 設定初始條件
initial_population = 100
final_population = 50000
doubling_time = 3  # 小時

# 計算並顯示結果
time_to_reach_population = calculate_population_time(initial_population, final_population, doubling_time)
print(f"Time required to reach 50,000 bacteria: {time_to_reach_population:.2f} hours")
