import streamlit as st
from main_new_Kr_Drozdova import one_func
from main_Nikita_ivanchenko import two_func
from elena_duragina import func_3
from main_tim import func_4
from main_vladimir import func_5

st.title("Программная инженерия. Практическая работа 10")

func = st.selectbox(
    label="Выберите работу:",
    options=["Первый", "Второй", "Третий", "четвёртый", "пятый"]
)


