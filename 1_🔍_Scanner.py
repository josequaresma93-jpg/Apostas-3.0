
import tempfile
import os
import pandas as pd

def test_flow():
    with tempfile.TemporaryDirectory() as tmp:
        os.chdir(tmp)

        from core.database import init_db, seed_demo, get_teams, save_bet, get_bets, update_bet_result, performance_metrics
        from core.model import estimate_lambdas, market_probabilities, compare_with_odds

        init_db()
        seed_demo()

        teams = get_teams("Série B")
        assert "Vila Nova" in teams
        assert "Novorizontino" in teams

        lh, la, warning = estimate_lambdas("Vila Nova", "Novorizontino", "Série B")
        assert lh > 0
        assert la > 0

        probs = market_probabilities(lh, la)
        assert "BTTS Sim" in set(probs["market"])

        odds = pd.DataFrame([{"market": "BTTS Sim", "odd": 2.0}])
        radar = compare_with_odds(probs, odds, 1000, 0.01)
        assert not radar.empty

        row = radar.iloc[0]

        save_bet(
            "Série B",
            "Vila Nova x Novorizontino",
            row["market"],
            row["odd"],
            row["fair_odd"],
            row["prob"],
            row["edge"],
            row["ev"],
            row["kelly"],
            10,
        )

        bets = get_bets()
        assert len(bets) == 1

        update_bet_result(1, "win")
        m = performance_metrics()
        assert m["profit"] > 0

if __name__ == "__main__":
    test_flow()
    print("TODOS OS TESTES PASSARAM")
