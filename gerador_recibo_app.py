import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime, date
import os 

st.set_page_config(page_title="Emissor de Recibos", page_icon="🧾")
st.title("Emissor de Recibos"

st.subheader("Preencha os dados do recibo")

nome = st.text_input("Nome do Cliente")
cpf = st.text_input("CPF/CNPJ")
valor = st.number_input("Valor (R$)", min_value=0.0, format="%.2f")
descricao = st.text_area("Descrição do Serviço")
cidade = st.text_input("Cidade")
data = st.date_input("Data", datetime.today())

def gerar_pdf(nome, cpf, valor, descricao, cidade, data):
  file_name = "recibo.pdf"
  c = canvas.Canvas(file_name, pagesize=letter)
  width, height = letter 
  c.setFont("Helvetica-Bold", 16)
  c.drawString(250, height - 50, "RECIBO")
  texto = [
    f"Recebi de: {nome}",
    f"CPF/CNPJ: {cpf}",
    "",
    f"A importância de: R$ {valor:.2f}",
    "",
    f"Referente a: {descrição}",
    "",
    f"{cidade}, {data.strftime('%d/%m/%Y')}",
    "",
    "",
    "______________________________",
    "Assinatura"
  ]
  y = height - 50
  for linha in texto:
    c.drawString(50, y, linha)
    y -= 20
  c.save()
  return file_name

if st.button("Gerar Recibo"):
  if nome and valor and descricao:
    pdf = gerar_pdf(nome, cpf, valor, descricao, cidade, data)
    with open(pdf, "rb") as f:
      st.download_button(
        "Baixar Recibo",
        f,
        file_name = f"recibo_{nome}.pdf",
        mime="application/pdf"
      )
  else:
    st.warning("Preencha pelo menos nome, valor e descrição."
