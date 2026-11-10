# Dictionnaire des données et KPI — démonstrateur synthétique

Toutes les valeurs sont **fictives**, créées pour tester la clarté des règles et l'interface. Elles ne proviennent d'aucune entité réelle. Ne pas les présenter comme des statistiques VIDI.

## Grain et clés

**Grain :** une ligne par `centre_id` et `periode` (mois), pour une modalité dominante illustrative. **Clé métier :** `(centre_id, periode)` unique. En situation réelle, les données source ont potentiellement un grain plus fin (examen, facture) et nécessitent dédoublonnage et agrégation avant cet état.

| Champ | Type / unité | Règle de contrôle | Rôle |
|---|---|---|---|
| `periode` | YYYY-MM | Mois valide | Filtre et jointure budget |
| `centre_id` | Texte | Non nul, clé contrôlée | Clé référentielle |
| `centre_fictif` | Texte | Aucun nom réel | Libellé |
| `modalite` | Enum : IRM / Scanner | Liste contrôlée | Contexte de comparaison |
| `ca_realise_eur` | Nombre EUR ≥ 0 / NULL | NULL explicitement incomplet | Numérateur écart |
| `ca_budget_eur` | Nombre EUR ≥ 0 / NULL | Zéro ≠ manquant | Dénominateur écart |
| `honoraires_eur` | Nombre EUR ≥ 0 | Ne pas les ajouter au CA sans définition | KPI descriptif |
| `examens` | Entier ≥ 0 | Ne pas compter les lignes de facturation comme examens | Activité |
| `vacations` | Entier ≥ 0 | Définir unité métier en vrai projet | Activité |
| `equipements` | Entier ≥ 0 | Ici effectif illustratif, pas temps de fonctionnement | Contexte |
| `statut_qualite` | VALIDE / INCOMPLET | INCOMPLET bloque calcul d'alerte | Transparence |

## KPI et logique

| Indicateur | Définition démonstrateur | Cas limite |
|---|---|---|
| CA réalisé | Somme du CA **uniquement sur les lignes valides**, même période/périmètre | NULL ne vaut jamais 0 |
| CA budget | Somme des budgets correspondant au même périmètre **seulement si toutes les lignes attendues sont présentes** | Un budget absent rend la comparaison non fiable |
| Écart absolu | `ca_realise_eur - ca_budget_eur` pour une ligne valide | Si l'une des entrées manque : non calculable |
| Écart relatif | `100*(réalisé-budget)/budget` | Si budget nul ou NULL : « non calculable » |
| Volume examens | Valeur `examens` du scénario sélectionné | Ne pas confondre actes, dossiers, factures |
| Examens / vacation | `examens / vacations` | Vacations = 0 : « non calculable » |
| Alerte d'écart défavorable | Si données valides et budget > 0 et écart% ≤ -10 %, afficher une alerte **selon seuil purement fictif de démonstration** | Données incomplètes => « non évaluable » ; budget zéro => « non calculable » |
| Benchmark | Comparer périodes identiques ; afficher modalité et nombre d'équipements | Classement descriptif, pas causal |

**Important :** le seuil `-10 %` sert à rendre la maquette vérifiable. Il n'est **pas validé par VIDI** et n'est pas le seuil d'acceptation métier `30 %` du MVP.

## Jeux de cas vérifiables

| Cas | Référence | Résultat attendu |
|---|---|---|
| C01 / février | 104 000 / 120 000 | Écart −16 000 €, −13,33 % ; alerte défavorable |
| C02 / mars | 88 000 / 100 000 | Écart −12 000 €, −12 % ; alerte défavorable |
| C03 / février | 180 000 / 200 000 | Écart −20 000 €, −10 % ; alerte défavorable |
| C04 / janvier | 70 000 / 0 | Écart absolu +70 000 € ; relatif non calculable |
| C04 / février | CA manquant | Écarts et alerte non évaluables |
| C01 / mars | 125 000 / 120 000 | Écart +5 000 €, +4,17 % ; pas d'alerte défavorable |

La cible de 100 % de cas de référence corrects ne devient une réussite mesurée **qu'après exécution documentée des tests**. Ce tableau donne les résultats attendus, pas des résultats observés.

## Contrôle de fuite de données

Aucun nom patient, aucune date de naissance, aucun identifiant de santé, aucun dossier d'entreprise ni valeur réelle dans `data/`. Les champs du dictionnaire correspondent à un jeu d'illustration, pas à une extraction d'entreprise.

## Référence de provenance

`data/radiopilot_synthetique.csv` — jeu de démonstration fabriqué pour le devoir, 12 lignes, 4 centres fictifs, janvier à mars 2026. Ces mois sont des **dates de scénarios fictifs**, pas les échéances du planning du projet.
