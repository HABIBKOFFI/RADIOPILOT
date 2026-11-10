#!/usr/bin/env python3
"""Validation hors ligne du jeu de démonstration RADIOPILOT, sans dépendance externe."""
from __future__ import annotations
import csv
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "data" / "radiopilot_synthetique.csv"

with CSV.open(encoding="utf-8", newline="") as f:
    records = list(csv.DictReader(f))

assert len(records) == 12, "Le jeu doit contenir 4 centres x 3 périodes"
keys = [(r["centre_id"], r["periode"]) for r in records]
assert len(keys) == len(set(keys)), "Doublon de grain centre/période"
assert len({r["centre_id"] for r in records}) == 4
assert len({r["periode"] for r in records}) == 3

def row(centre, mois):
    return next(r for r in records if r["centre_id"] == centre and r["periode"] == mois)

def kpi(centre, mois):
    r = row(centre, mois)
    if r["statut_qualite"] != "VALIDE" or not r["ca_realise_eur"] or not r["ca_budget_eur"]:
        return None
    ca = Decimal(r["ca_realise_eur"])
    budget = Decimal(r["ca_budget_eur"])
    if budget == 0:
        return None
    return (ca - budget) / budget * 100

assert kpi("C01", "2026-02").quantize(Decimal("0.01")) == Decimal("-13.33")
assert kpi("C02", "2026-03").quantize(Decimal("0.01")) == Decimal("-12.00")
assert kpi("C03", "2026-02").quantize(Decimal("0.01")) == Decimal("-10.00")
assert kpi("C04", "2026-01") is None, "Budget nul : relatif non calculable"
assert kpi("C04", "2026-02") is None, "CA absent : écart non évaluable"
assert kpi("C01", "2026-03").quantize(Decimal("0.01")) == Decimal("4.17")

alerts = [(r["centre_id"], r["periode"]) for r in records
          if (x := kpi(r["centre_id"], r["periode"])) is not None and x <= -10]
assert alerts == [("C01", "2026-02"), ("C02", "2026-01"),
                  ("C02", "2026-03"), ("C03", "2026-02")], alerts

print("PASS : 12 lignes uniques, calculs, cas limites, 4 alertes de demonstration.")
print("NB : ceci teste les REGLES du dataset fictif, pas la valeur metier sur utilisateurs.")
