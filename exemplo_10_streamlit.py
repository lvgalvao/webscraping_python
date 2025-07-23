import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Carrega o CSV ---
df = pd.read_csv("historico_precos_fake.csv", names=["created_at", "produto", "preco", "url", "fonte"])

# --- Converte datas e preços ---
df["created_at"] = pd.to_datetime(df["created_at"])
df["preco"] = df["preco"].astype(str).str.replace(".", "").astype(float)

# --- Estatísticas ---
preco_min = df["preco"].min()
preco_max = df["preco"].max()
preco_medio = df["preco"].mean()

# --- Título ---
st.title("📊 Monitoramento de Preços")

# --- Estatísticas ---
st.markdown("### 📈 Estatísticas")
st.write(f"**Menor preço:** R$ {preco_min:,.2f}")
st.write(f"**Maior preço:** R$ {preco_max:,.2f}")
st.write(f"**Preço médio:** R$ {preco_medio:,.2f}")

# --- Gráfico ---
st.markdown("### 📉 Evolução do Preço ao Longo do Tempo")
fig, ax = plt.subplots()
ax.plot(df["created_at"], df["preco"], marker='o', linestyle='-', color='blue')
ax.set_xlabel("Data e Hora")
ax.set_ylabel("Preço (R$)")
ax.set_title("Histórico de Preços")
plt.xticks(rotation=45)
st.pyplot(fig)

# --- Tabela completa (opcional) ---
st.markdown("### 📋 Histórico Completo")
st.dataframe(df.sort_values(by="created_at", ascending=False))
