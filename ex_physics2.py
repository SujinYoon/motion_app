import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def free_fall_simulation():
    st.header('자유낙하 시뮬레이터')
    g = 9.81  # 중력가속도 (m/s^2)

    # 입력
    fall_time = st.slider('낙하 시간 (s)', 0.0, 10.0, 1.0)

    # 속도 및 이동 거리 계산
    velocity = g * fall_time
    distance = 0.5 * g * fall_time ** 2

    # 결과 출력
    st.info(f'낙하 후 속도: {velocity:.3f} m/s')
    st.info(f'낙하 거리: {distance:.3f} m')

    # session_state에 결과 저장
    if 'free_fall_results' not in st.session_state:
        st.session_state.free_fall_results = []

    st.session_state.free_fall_results.append({
        '낙하 시간 (s)': fall_time,
        '속도 (m/s)': velocity,
        '거리 (m)': distance
    })

    # 시뮬레이션 결과를 누적한 테이블 출력
    st.divider()
    st.write("누적 결과:")
    st.table(st.session_state.free_fall_results)

def linear_motion_simulation():
    st.header('등속 직선 운동 시뮬레이터')

    # 입력(양식-form 활용)
    with st.form("linear_param"):
        initial_position = st.number_input('초기 위치 (m)', value=0.0)
        velocity = st.number_input('속도 (m/s)', value=0.0)
        time = st.number_input('시간 (s)', value=0.0)
        submit = st.form_submit_button('계산')

    if submit:
        # 위치 계산 및 결과 출력
        final_position = initial_position + velocity * time
        st.info(f'최종 위치: {final_position:.3f} m')

def projectile_motion_simulation():
    st.header('포물선 운동 시뮬레이터')

    # 입력
    initial_velocity = st.number_input('초기 속도 (m/s)', value=20.0)
    angle = st.slider('발사 각도 (도)', 0, 90, 45)

    # 최대 높이와 도달 거리 계산
    angle_rad = np.radians(angle)
    g = 9.81  # 중력가속도 (m/s^2)
    max_height = (initial_velocity ** 2) * (np.sin(angle_rad) ** 2) / (2 * g)
    range = (initial_velocity ** 2) * np.sin(2 * angle_rad) / g

    # 결과 출력
    st.info(f'최대 높이: {max_height:.3f} m')
    st.info(f'도달 거리: {range:.3f} m')

    # 포물선 그래프
    t = np.linspace(0, 2 * initial_velocity * np.sin(angle_rad) / g, num=100)
    x = initial_velocity * np.cos(angle_rad) * t
    y = initial_velocity * np.sin(angle_rad) * t - 0.5 * g * t ** 2

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Height (m)')
    ax.set_title('Projectile Motion')
    st.pyplot(fig)

def show_about_app():
    st.header("운동 시뮬레이터 앱에 오신 것을 환영합니다!")
    st.write("""
           ## [앱 소개]

           이 앱은 물리학에서 다양한 운동의 시뮬레이션을 제공합니다. 
           사이드바를 사용하여 다양한 운동 유형을 선택하고 시뮬레이터를 사용해보세요.

           - **자유낙하**: 공기 저항이 없는 상황에서 중력의 영향을 받아 물체가 자유롭게 떨어지는 운동을 시뮬레이션합니다.
           - **등속직선운동**: 직선 경로를 따라 등속으로 움직이는 운동을 시뮬레이션합니다.
           - **포물선운동**: 중력의 영향을 받아 공중에 던져진 물체의 궤적을 시각화합니다.

           각 시뮬레이션은 매개변수를 입력하고, 이를 통해 운동이 어떻게 변화하는지 관찰할 수 있습니다. 

           ### [사용 방법]

           1. **시뮬레이션 선택**: 사이드바의 라디오 버튼을 사용하여 탐구하고자 하는 운동 유형을 선택하세요.
           2. **매개변수 입력**: 선택한 운동 유형에 따라 관련 매개변수를 입력하세요 (예: 초기 속도, 각도, 높이).
           3. **시뮬레이션 실행**: 시뮬레이션 결과와 그래프를 통해 운동의 역학을 이해해 보세요.
           """)

def welcome():
    st.snow()

# 사이드바 구성
st.sidebar.title("Simulator")
st.sidebar.radio(
    "**Select:**",
    ["**:rainbow[Home]**", "**free fall**", "**uniform linear motion**", "**projectile motion**"],
    captions = ["about app", "자유 낙하", "등속 직선 운동", "포물선 운동"],
    key="kind_of_motion", on_change=welcome)

# 선택한 동작(도움말 또는 시뮬레이션) 실행
if st.session_state["kind_of_motion"] == "**:rainbow[Home]**":
    show_about_app()
elif st.session_state["kind_of_motion"] == "**free fall**":
    free_fall_simulation()
elif st.session_state["kind_of_motion"] == "**uniform linear motion**":
    linear_motion_simulation()
elif st.session_state["kind_of_motion"] == "**projectile motion**":
    projectile_motion_simulation()