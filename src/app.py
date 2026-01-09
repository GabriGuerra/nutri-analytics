import streamlit as st
import plotly.express as px

from filters import load_data
from layout import load_layout

# ===================== CONFIGURAÇÃO =====================
st.set_page_config(
    page_title="Bio-Intelligence Command",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_layout()

# ===================== DADOS =====================
df = load_data()

# ===================== SIDEBAR =====================
with st.sidebar:
    st.markdown("""
        <div class="profile-box">
            <div class="profile-name">Plataforma Nutricional Inteligente</div>
            <div class="profile-role">Nutrição & Saúde</div>
            <div class="profile-desc">Data Analytics, BI & Applied Intelligence</div>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("Filtros Globais")

    opts_pilar = ["Todos"] + sorted(df['Sistema_Biologico'].unique().tolist())
    sel_pilar = st.multiselect("Filtrar Sistemas:", options=opts_pilar, default="Todos")

    opts_hor = ["Todos"] + sorted(df['Cronobiologia_Periodo'].unique().tolist())
    sel_hor = st.multiselect("Filtrar Períodos:", options=opts_hor, default="Todos")

    st.markdown("---")
    st.subheader("Configuração da Visualização")

    eixo_sunburst = st.selectbox(
        "Agrupar Gráfico por:",
        options=[
            "Sistema_Biologico",
            "Mecanismo_Acao",
            "Uso_Pratico",
            "Cronobiologia_Periodo",
            "Fonte_Alimentar"
        ],
        format_func=lambda x: x.replace("_", " ").title()
    )

# ===================== ENGINE DE FILTROS =====================
df_view = df.copy()

if "Todos" not in sel_pilar and sel_pilar:
    df_view = df_view[df_view['Sistema_Biologico'].isin(sel_pilar)]

if "Todos" not in sel_hor and sel_hor:
    df_view = df_view[df_view['Cronobiologia_Periodo'].isin(sel_hor)]

df_display = df_view.sort_values('Ordem_Cronos')

# ===================== INTERFACE PRINCIPAL =====================
st.markdown(
    "<h2 style='font-weight:700; margin-bottom:0;'>Sistema de Dados Nutricionais</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='margin-bottom:2.5rem;'>Arquitetura de Dados Bioativos & Gestão de Estratégia</p>",
    unsafe_allow_html=True
)

col_left, col_right = st.columns([5, 7])

with col_left:
    st.markdown(
        f"<div class='section-title'>Mapa de Hierarquia: {eixo_sunburst.replace('_', ' ')}</div>",
        unsafe_allow_html=True
    )

    fig_sun = px.sunburst(
        df_view,
        path=[eixo_sunburst, 'Nome_Item'],
        values='Peso_Visual',
        color=eixo_sunburst,
        color_discrete_sequence=px.colors.qualitative.Safe,
        hover_data=[eixo_sunburst]
    )

    fig_sun.update_layout(
        height=620,
        margin=dict(t=0, l=0, r=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
    )

    st.plotly_chart(fig_sun, width="stretch")

with col_right:
    st.markdown(
        "<div class='section-title'>Dossiê de Ativos (Organização Cronológica)</div>",
        unsafe_allow_html=True
    )

    st.dataframe(
        df_display.drop(columns=['Peso_Visual', 'Ordem_Cronos'], errors='ignore'),
        width="stretch",
        height=620,
        hide_index=True,
        column_config={
            "Nome_Item": st.column_config.TextColumn("Ativo", width="medium"),
            "Sistema_Biologico": st.column_config.TextColumn("Sistema"),
            "Mecanismo_Acao": st.column_config.TextColumn("Mecanismo de Ação", width="large"),
            "Uso_Pratico": st.column_config.TextColumn("Uso Prático", width="medium"),
            "Cronobiologia_Periodo": st.column_config.TextColumn("Período"),
            "Fonte_Alimentar": st.column_config.TextColumn("Fonte"),
            "Momento_Refeicao": st.column_config.TextColumn("Refeição"),
            "Objetivo_Primario": st.column_config.TextColumn("Objetivo")
        }
    )

# ===================== RODAPÉ =====================
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("""
    <div style='display:flex; justify-content:space-between;
                color:#9CA3AF; font-size:0.75rem; padding-bottom:20px;'>
        <span>Protocolo Bio-Intelligence Matrix v17.0</span>
        <span>Analytics Engineer: Gabriel Guerra</span>
    </div>
""", unsafe_allow_html=True)
