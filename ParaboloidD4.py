import numpy as np
import matplotlib.pyplot as plt

# 1. 자계(H-field) 측정 데이터 입력 (이미지 수치 반영)
# 양수 각도 (0 ~ 11도까지 변화, 12도부터 -17dB 고정)
pos_gains = {
    0: 0, 1: -0.1, 2: -0.4, 3: -1.2, 4: -2.2, 5: -3.0,
    6: -4.5, 7: -6.5, 8: -9.0, 9: -12.2, 10: -14.0, 11: -16.5
}

# 음수 각도 (-1 ~ -13도까지 변화, -14도부터 -17dB 고정)
neg_gains = {
    -1: -0.4, -2: -0.8, -3: -1.6, -4: -3.0, -5: -4.5, -6: -6.5,
    -7: -8.5, -8: -12.2, -9: -15.5, -10: -16.5, -11: -17.0, -12: -16.5, -13: -16.0
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
        # 요청하신 대로 12도 이상, -14도 이하는 모두 -17dB로 설정
        full_gains.append(-17.0)

full_gains = np.array(full_gains)
theta = np.radians(full_angles)

# 3. 그래프 설정
# 최저값이 -17dB이므로 원점 기준을 -20dB로 설정하여 패턴 모양 확보
min_db = -20
display_gains = full_gains - min_db
display_gains[display_gains < 0] = 0

# 4. 그래프 그리기
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))

# 0도 북쪽, 시계 방향 설정
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

# 데이터 플롯
ax.plot(theta, display_gains, linewidth=2, color='#0072BD', label='Measured H-field')
ax.fill(theta, display_gains, color='#0072BD', alpha=0.1)

# 시각적 요소 설정
ax.set_title("Horn Fed Paraboloid H-plane Pattern\n(Center=-20dB, Tail=-17dB)", va='bottom', fontsize=14)
ax.set_rlabel_position(0)
ax.grid(True, linestyle=':', alpha=0.6)

# r축 라벨을 실제 dB로 표시 (0, -5, -10, -15, -20 표시)
ticks = np.linspace(0, -min_db, 5)
tick_labels = [f"{int(t + min_db)}dB" for t in ticks]
ax.set_rticks(ticks)
ax.set_yticklabels(tick_labels)

# 범례 추가
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

plt.tight_layout()
plt.show()