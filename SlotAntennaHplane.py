import numpy as np
import matplotlib.pyplot as plt

# 1. 이미지 데이터 입력 (표의 수치 반영)
# 양수 각도 (0 ~ 17도)
angles_pos = np.arange(18)
gains_pos = [0, -1.8, -2.9, -3.6, -4.2, -4.5, -4.4, -5, -5.5, -5, -6.5, -7, -7.5, -8, -7.8, -9, -9.5, -10]

# 음수 각도 (-1 ~ -18도)
angles_neg = np.arange(-1, -19, -1)
gains_neg = [-1.2, -1.8, -2.9, -3.6, -3.8, -4, -4.1, -4.5, -5, -4.8, -5.5, -5.8, -6, -6.5, -6, -6.8, -7.8, -9]

# 2. 전체 범위 (-180 ~ 180) 데이터 생성 및 18도 이후 -10dB 적용
full_angles = np.arange(-180, 181)
full_gains = []

for ang in full_angles:
    if 0 <= ang <= 17:
        full_gains.append(gains_pos[ang])
    elif -18 <= ang <= -1:
        # angles_neg는 -1, -2... 순서이므로 인덱스 처리
        full_gains.append(gains_neg[abs(ang)-1])
    else:
        # +- 18도 이후는 모두 -10dB 처리
        full_gains.append(-10)

full_gains = np.array(full_gains)
theta = np.radians(full_angles)

# 3. 그래프 표시 변환 (기존 Offset 방식 유지)
min_db = -15  # 원점 기준값
display_gains = full_gains - min_db
display_gains[display_gains < 0] = 0

# 4. 그래프 그리기 (형태 변형 없음)
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))

# 기존 설정 유지: 0도 위쪽, 시계 방향
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

# 데이터 플롯
ax.plot(theta, display_gains, linewidth=2, color='#0072BD')

# 시각적 요소 설정 (기존 스타일 유지)
ax.set_title("Waveguide Linear Slot Array H-plane Pattern\n(Center=-15dB, Tail=-10dB)", va='bottom', fontsize=14)
ax.set_rlabel_position(0)
ax.grid(True)

# r축 라벨을 실제 dB로 표시
ticks = np.linspace(0, -min_db, 4)
tick_labels = [f"{int(t + min_db)}dB" for t in ticks]
ax.set_rticks(ticks)
ax.set_yticklabels(tick_labels)

plt.tight_layout()
plt.show()
