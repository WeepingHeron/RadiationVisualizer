import numpy as np
import matplotlib.pyplot as plt

# 1. 자계(H-field) 측정 데이터 입력 (이미지 표 수치 반영)
# 양수 각도 (0 ~ 13도까지 변화, 14도부터 -12dB)
pos_gains = {
    0: 0, 1: -0.2, 2: -0.4, 3: -0.8, 4: -1.4, 5: -2.6,
    6: -3.0, 7: -4.3, 8: -6.0, 9: -7.8, 10: -10.0, 11: -11.0,
    12: -11.4, 13: -11.0
}

# 음수 각도 (-1 ~ -9도까지 변화, -10도부터 -12dB)
neg_gains = {
    -1: -0.4, -2: -1.0, -3: -1.6, -4: -2.9, -5: -4.5,
    -6: -6.0, -7: -8.5, -8: -10.8, -9: -11.6
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
        # 나머지 각도(14~180, -10~-180)는 표기된 최소값인 -12dB로 통일
        full_gains.append(-12.0)

full_gains = np.array(full_gains)
theta = np.radians(full_angles)

# 3. 그래프 설정
min_db = -15  # 원점 기준값 (최저 이득이 -12dB이므로 모양 유지를 위해 -15dB로 설정)
display_gains = full_gains - min_db
display_gains[display_gains < 0] = 0

# 4. 그래프 그리기
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))

# 0도 북쪽, 시계 방향 설정
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

# 데이터 플롯 (자계 그래프이므로 파란색 톤으로 변경)
ax.plot(theta, display_gains, linewidth=2, color='#0072BD', label='Measured H-field')
ax.fill(theta, display_gains, color='#0072BD', alpha=0.1)

# 시각적 요소 설정
ax.set_title("Horn Fed Paraboloid H-plane Pattern\n(Center=-15dB, Tail=-12dB)", va='bottom', fontsize=14)
ax.set_rlabel_position(0)
ax.grid(True, linestyle=':', alpha=0.6)

# r축 라벨을 실제 dB로 표시
ticks = np.linspace(0, -min_db, 4)
tick_labels = [f"{int(t + min_db)}dB" for t in ticks]
ax.set_rticks(ticks)
ax.set_yticklabels(tick_labels)

# 범례 추가
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

plt.tight_layout()
plt.show()