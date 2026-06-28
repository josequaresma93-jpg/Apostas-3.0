# Apostas 3.0 PRO — Site GitHub Pages

Site estático em HTML, CSS e JavaScript para análise de apostas esportivas.

## Publicar no GitHub Pages

1. Suba `index.html`, `style.css`, `app.js` e `README.md` no repositório `Apostas-3.0`.
2. Vá em **Settings**.
3. Clique em **Pages**.
4. Em **Build and deployment**, selecione:
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/root`
5. Clique em **Save**.

O site ficará em:

```text
https://josequaresma93-jpg.github.io/Apostas-3.0/
```

## Recursos

- Cadastro de jogos
- Importação CSV
- Exportar/importar backup JSON
- Base de exemplo
- Poisson
- BTTS
- Over/Under
- Handicap Asiático
- Odd justa
- Edge
- EV
- Kelly
- Stake sugerida
- Histórico
- ROI/Yield
- Dashboard por mercado e liga
- Backtest simples
- Dados salvos no navegador com localStorage

## CSV

Colunas aceitas:

```text
data,liga,mandante,visitante,gols_mandante,gols_visitante
```

ou:

```text
match_date,league,home_team,away_team,home_goals,away_goals
```
