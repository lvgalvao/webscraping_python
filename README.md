# 🕷️ Projeto de Web Scraping com Python

## 📋 Objetivo do Projeto

Este projeto demonstra como realizar **web scraping** no Mercado Livre para monitorar preços de produtos em tempo real. O objetivo é coletar dados de preços automaticamente e criar um sistema completo de monitoramento com notificações e visualização.

## 🎯 Objetivos da Aula

### Conceitos Fundamentais
- **Web Scraping**: Técnicas para extrair dados de websites
- **HTTP Requests**: Como fazer requisições para páginas web
- **HTML Parsing**: Interpretar e extrair informações do HTML
- **Automação**: Criar scripts que executam tarefas repetitivas

### Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto
- **Requests**: Biblioteca para fazer requisições HTTP
- **BeautifulSoup**: Parser HTML para extrair dados
- **Streamlit**: Interface web para visualização de dados
- **Telegram Bot API**: Notificações em tempo real
- **Pandas**: Manipulação e análise de dados
- **Matplotlib**: Criação de gráficos

## 📁 Estrutura do Projeto

### Exemplos Progressivos

#### **exemplo_01.py** - Primeira Requisição
- Faz uma requisição básica para o Mercado Livre
- Demonstra o uso da biblioteca `requests`

#### **exemplo_02_a.py** - Headers de Navegador
- Adiciona headers para simular um navegador real
- Evita bloqueios do site

#### **exemplo_02_b.py** - Salvando HTML
- Salva o HTML da página em arquivos
- Organiza arquivos por timestamp

#### **exemplo_03.py** - Requisição com Headers
- Combina requisição com headers apropriados

#### **exemplo_04.py** - BeautifulSoup
- Introduz o BeautifulSoup para parsing HTML
- Extrai o preço do produto usando seletores CSS

#### **exemplo_05.py** - Salvando em CSV
- Salva dados coletados em arquivo CSV
- Cria histórico de preços

#### **exemplo_06.py** - Monitoramento Contínuo
- Loop infinito para monitoramento
- Coleta dados a cada minuto
- Simula comportamento humano com delays aleatórios

#### **exemplo_07_telegram.py** - Integração Telegram
- Configuração básica do bot do Telegram
- Envio de mensagens via API

#### **exemplo_08_todo_minuto.py** - Sistema Completo
- Combina scraping + CSV + Telegram
- Sistema completo de monitoramento com notificações

#### **exemplo_10_streamlit.py** - Interface Web Básica
- Primeira versão da interface Streamlit
- Visualização de dados e gráficos

#### **exemplo_11_streamlitfinal.py** - Interface Web Final
- Interface completa e otimizada
- Métricas, gráficos e tabelas interativas

### Arquivos de Dados
- **historico_precos.csv**: Dados reais coletados
- **historico_precos_fake.csv**: Dados simulados para demonstração
- **gerador_dados.py**: Script para gerar dados de exemplo

## 🚀 Funcionalidades Implementadas

### ✅ Coleta de Dados
- Requisições HTTP com headers apropriados
- Parsing HTML com BeautifulSoup
- Extração de preços usando seletores CSS
- Salvamento em arquivos CSV

### ✅ Monitoramento Automático
- Loop de execução contínua
- Delays aleatórios para evitar detecção
- Tratamento de erros robusto
- Logs detalhados de execução

### ✅ Notificações
- Integração com Telegram Bot API
- Alertas em tempo real
- Mensagens formatadas com emojis

### ✅ Visualização
- Interface web com Streamlit
- Gráficos de evolução de preços
- Métricas estatísticas (mín, máximo, médio)
- Tabelas interativas

## 🛠️ Como Usar

### Pré-requisitos
```bash
pip install requests beautifulsoup4 streamlit pandas matplotlib
```

### Executando os Exemplos
```bash
# Exemplo básico de scraping
python exemplo_01.py

# Monitoramento completo
python exemplo_08_todo_minuto.py

# Interface web
streamlit run exemplo_11_streamlitfinal.py
```

### Configuração do Telegram
1. Crie um bot no Telegram via @BotFather
2. Obtenha o token do bot
3. Substitua o token no código
4. Configure o chat_id

## 📊 Resultados Esperados

- **Coleta automática** de preços do Mercado Livre
- **Histórico completo** de variações de preços
- **Notificações instantâneas** via Telegram
- **Dashboard interativo** para análise de dados
- **Gráficos** mostrando tendências de preços

## 🔗 Links Úteis

- **Jornada de Dados**: https://suajornadadedados.com.br/
- **Documentação Requests**: https://requests.readthedocs.io/
- **Documentação BeautifulSoup**: https://beautiful-soup-4.readthedocs.io/
- **Documentação Streamlit**: https://docs.streamlit.io/

## 📝 Aprendizados

Este projeto demonstra conceitos fundamentais de:
- **Automação web**
- **Manipulação de dados**
- **APIs externas**
- **Visualização de dados**
- **Desenvolvimento de aplicações web**

---

*Projeto desenvolvido como parte da Jornada de Dados - Curso completo de Engenharia de dados*