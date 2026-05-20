import streamlit as st
st.title('강아지')
st.write('고기 사줘')
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="자동 계획 생성기",
    page_icon="📅"
)

# 제목
st.title("📅 자동 계획 생성기")

st.write("목표를 입력하면 간단한 계획을 자동으로 만들어줍니다.")

# 사용자 입력
goal = st.text_input("목표를 입력하세요")

days = st.slider("며칠 동안 진행할까요?", 1, 30, 7)

# 버튼
if st.button("계획 만들기"):

    if goal == "":
        st.warning("목표를 입력해주세요.")
    else:
        st.subheader("✅ 추천 계획")

        for day in range(1, days + 1):

            if day == 1:
                task = "목표 정리하기"

            elif day < days:
                task = f"{goal} 연습 및 진행하기"

            else:
                task = "최종 점검 및 마무리"

            st.write(f"Day {day} - {task}")
