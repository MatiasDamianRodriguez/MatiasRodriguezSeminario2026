import streamlit as st

st.set_page_config(
    page_title="Mi app de Streamlit",
    layout="centered",
)

st.title("Calculadora de Potencia")

def multiplicar_por_si_mismo(numero, veces):
    resultado = numero ** veces
    return resultado

# Usamos value=0 y step=1 para trabajar exclusivamente con enteros
numero_input = st.number_input("Ingresá un número", value=0, step=1)
veces_input = st.selectbox("¿Cuántas veces multiplicar?", options=list(range(1, 11)), index=0)

if st.button("Calcular"):
    resultado_output = multiplicar_por_si_mismo(numero_input, veces_input)
    st.success(f"El resultado es: {resultado_output}")