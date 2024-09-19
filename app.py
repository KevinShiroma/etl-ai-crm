import streamlit as st
from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError 

def main():
    st.title("Sistema de CRM e Vendas")
    email = st.text_input("Campo de texto para inserção do email do vendedor")
    data = st.date_input("Campo para selecionar a data em qeu a venda foi realizada", datetime.now())
    hora = st.time_input("Campo para selecionar a hora que foi realizada", value=time(9,0))
    valor = st.number_input("Campo numérico para inserir o valor monetário da venda realziada", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Campo de texto para inserção de quantidade de produtos vendidos", min_value=1, step=1)
    produto = st.selectbox("Campo de seleção para escoher o produto vendido", ["Zapflow com Gemini", "Zapflow com ChatGPT", "Zapflow com Lhama"])

    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data,hora)

            venda = Vendas(
            email = email,
            data = data_hora,
            valor = valor,
            quantidade = quantidade,
            produto = produto
        )
            st.write(venda)
        except ValidationError as e:
            st.error(f"Deu erro {e}")

        
            # st.write("**Dados da Vemda:**")
            # st.write(f"Email do vendedor: {email}")
            # st.write(f"Data e Hora da compra: {data_hora}")
            # st.write(f"Valor da venda: R$ {valor:.2f}")
            # st.write(f"Quantidade de produtos: {quantidade}")
            # st.write(f"produto: {produto}")

if __name__ == "__main__":
    main()