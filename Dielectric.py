import numpy as np
import matplotlib.pyplot as plt

# 1. Dielectric 안테나 전계(E-field) 측정 데이터 입력
# 양수 각도 (0 ~ 33도까지 변화, 34도부터 -12dB 고정)
pos_gains = {
    0: 0, 1: 0, 2: 0, 3: 0, 4: -0.2, 5: -0.3, 6: -0.3, 7: -0.2, 8: -0.6, 9: -0.8,
    10: -1.0, 11: -0.9, 12: -0.9, 13: -1.0, 14: -1.2, 15: -1.7, 16: -1.6, 17: -1.8, 18: -2.0, 19: -2.6,
    20: -3.0, 21: -3.4, 22: -4.0, 23: -4.1, 24: -4.5, 25: -4.5, 26: -5.0, 27: -5.5, 28: -6.0, 29: -5.5,
    30: -6.8, 31: -7.0, 32: -8.5, 33: -10.0
}

# 음수 각도 (-1 ~ -29도까지 변화, -30도부터 -12dB 고정)
neg_gains = {
    -1: 0, -2: 0, -3: 0, -4: -0.1, -5: -0.3, -6: -0.8, -7: -1.2, -8: 0.9, -9: -1.0,
    -10: -0.8, -11: -0.7, -12: -1.0, -13: -1.2, -14: -1.6, -15: -2.7, -16: -3.1, -17: -3.4, -18: -3.8, -19: -4.0,
    -20: -4.1, -21: -4.5, -22: -4.7, -23: -4.5, -24: -5.0, -25: -5.7, -26: -6.0, -27: -6.5, -28: -8.0, -29: -10.5
}

# 2. 전체 범위 (-180 ~ 180) 데이터 생성
full_angles = np.arange(-180, 181)
full_gains = []

for ang in full_angles:
    if ang in pos_gains:
        full_gains.append(pos_gains[ang])
    elif ang in neg_gains:
        full_gains.append(neg_gains[ang])
    else:
        # 데이터 시트 기반: 양수 34도~, 음수 -30도~ 이후는 -12dB 고정
        full_gains.append(-12.0)

full_gains = np.array(full_gains)
theta = np.radians(full_angles)

# 3. 그래프 설정
min_db = -15  # 최저 이득(-12dB)을 고려한 원점 기준 설정
display_gains = full_gains - min_db
display_gains[display_gains < 0] = 0

# 4. 그래프 그리기
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))

# 0도 북쪽, 시계 방향 설정
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

# 데이터 플롯 (전계 그래프이므로 주황색 계열 사용)
ax.plot(theta, display_gains, linewidth=2, color='#D95319', label='Measured E-field')
ax.fill(theta, display_gains, color='#D95319', alpha=0.1)

# 시각적 요소 설정
ax.set_title("Dielectric Antenna E-plane Pattern\n(Center=-15dB, Tail=-12dB)", va='bottom', fontsize=14)
ax.set_rlabel_position(0)
ax.grid(True, linestyle=':', alpha=0.6)

# r축 라벨을 실제 dB로 표시
ticks = np.linspace(0, -min_db, 4)
tick_labels = [f"{int(t + min_db)}dB" for t in ticks]
ax.set_rticks(ticks)
ax.set_yticklabels(tick_labels)

ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

plt.tight_layout()
plt.show()