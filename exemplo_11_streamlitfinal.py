import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Carrega o CSV ---
df = pd.read_csv("historico_precos_fake.csv", names=["created_at", "produto", "preco", "url", "fonte"])

# --- Conversões ---
df["created_at"] = pd.to_datetime(df["created_at"])
df["preco"] = df["preco"].astype(str).str.replace(".", "").astype(float)

# --- Agrupa por hora para suavizar ---
df_hora = df.set_index("created_at").resample("1H").mean().reset_index()

# --- Estatísticas ---
preco_min = df["preco"].min()
preco_max = df["preco"].max()
preco_medio = df["preco"].mean()

# --- Layout ---
st.set_page_config(page_title="Monitor de Preços", layout="wide")
st.title("📊 Evolução de Preços no Mercado Livre")

# --- Colunas com Métricas ---
col1, col2, col3 = st.columns(3)
col1.metric("💰 Menor Preço", f"R$ {preco_min:,.2f}")
col2.metric("📈 Maior Preço", f"R$ {preco_max:,.2f}")
col3.metric("📊 Preço Médio", f"R$ {preco_medio:,.2f}")

# --- Gráfico de Evolução ---
st.markdown("### 📉 Evolução do Preço ao Longo do Tempo")
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(df_hora["created_at"], df_hora["preco"], marker='o', linestyle='-', color='blue')
ax.set_xlabel("Data e Hora")
ax.set_ylabel("Preço (R$)")
ax.set_title("Histórico de Preços (1h)")
ax.grid(True)
plt.xticks(rotation=30)
st.pyplot(fig)

# --- Histórico Completo ---
st.markdown("### 📋 Tabela de Preços")
st.dataframe(df.sort_values(by="created_at", ascending=False), use_container_width=True)
