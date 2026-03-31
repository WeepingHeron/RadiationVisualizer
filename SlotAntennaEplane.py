import numpy as np
import matplotlib.pyplot as plt

# 1. 전계(E-field) 측정 데이터 입력 (이미지 표 수치 반영)
# 양수 각도 (0 ~ 19도)
angles_pos = np.arange(20)
gains_pos = [0, -0.6, -1.1, -2.6, -3, -3.5, -4.3, -4, -5.2, -6.2,
             -7.8, -6.8, -8, -8.5, -7.8, -9, -9.5, -10, -10, -10]

# 음수 각도 (-1 ~ -20도)
angles_neg = np.arange(-1, -21, -1)
gains_neg = [-0.8, -1.4, -3.1, -3.8, -3.9, -4.6, -4.4, -5, -5.2, -6,
             -7.2, -8.8, -8.5, -8, -7.8, -8.5, -9.5, -10, -10, -10]

# 2. 전체 범위 (-180 ~ 180) 데이터 생성
full_angles = np.arange(-180, 181)
full_gains = []

for ang in full_angles:
    if 0 <= ang <= 17:
        full_gains.append(gains_pos[ang])
    elif -18 <= ang <= -1:
        full_gains.append(gains_neg[abs(ang)-1])
    else:
        # +- 18도 이후는 모두 -10dB로 통일
        full_gains.append(-15)

full_gains = np.array(full_gains)
theta = np.radians(full_angles)

# 3. 그래프 설정 (통일성을 위해 기존 형태 유지)
min_db = -15  # 원점 기준값 (패턴의 끝이 -10dB이므로 모양 유지를 위해 설정)
display_gains = full_gains - min_db
display_gains[display_gains < 0] = 0

# 4. 그래프 그리기
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))

# 0도 북쪽, 시계 방향 설정
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

# 데이터 플롯
ax.plot(theta, display_gains, linewidth=2, color='#D95319', label='Measured E-field')
ax.fill(theta, display_gains, color='#D95319', alpha=0.1)

# 시각적 요소 설정
ax.set_title("Waveguide Linear Slot Array E-plane Pattern\n(Center=-15dB, Tail=-10dB)", va='bottom', fontsize=14)
ax.set_rlabel_position(0)
ax.grid(True, linestyle=':', alpha=0.6)

# r축 라벨을 실제 dB로 표시
ticks = np.linspace(0, -min_db, 4)
tick_labels = [f"{int(t + min_db)}dB" for t in ticks]
ax.set_rticks(ticks)
ax.set_yticklabels(tick_labels)

plt.tight_layout()
plt.show()
