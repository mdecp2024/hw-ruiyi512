def calculate_deceleration(v0_kmh, distance):
    # 將初速度從 km/h 轉換成 m/s
    v0_ms = v0_kmh * 1000 / 3600
    # 計算加速度
    acceleration = -(v0_ms ** 2) / (2 * distance)
    return acceleration

# 設定初始條件
initial_velocity_kmh = 310  # km/h
runway_distance = 1000      # m

# 計算並顯示結果
deceleration = calculate_deceleration(initial_velocity_kmh, runway_distance)
print(f"Required deceleration: {deceleration:.2f} m/s^2")
