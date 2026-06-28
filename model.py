
import streamlit as st
from core.database import init_db, seed_demo

st.set_page_config(
    page_title="Projeto Apostas 2.0 PRO",
    page_icon="⚽",
    layout="wide"
)

init_db()

st.title("⚽ Projeto Apostas 2.0 PRO — V6")
st.caption("Scanner de valor com Poisson, odds justas, EV, Kelly, histórico e dashboard.")

st.success("Sistema carregado com sucesso.")

c1, c2 = st.columns(2)

with c1:
    if st.button("Carregar base de exemplo"):
        seed_demo()
        st.success("Base carregada. Abra a página Scanner.")

with c2:
    st.info("Use o menu lateral para navegar.")

st.markdown("""
## Fluxo de uso

1. **Banco de Jogos**: cadastre resultados ou carregue a base de exemplo.
2. **Scanner**: escolha mandante e visitante, digite as odds e veja se tem valor.
3. **Histórico**: salve apostas e atualize os resultados.
4. **Dashboard**: acompanhe ROI, lucro, acerto e desempenho por mercado.
5. **Backtest**: teste mercados com base nos jogos cadastrados.

## Próximas fases

- Integração com API de resultados.
- Integração com API de odds.
- Scanner automático por campeonato.
- Ranking das melhores entradas do dia.
""")
