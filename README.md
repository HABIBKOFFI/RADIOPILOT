# RADIOPILOT — Charte de projet

**Innovation & Design Thinking × Project Management — Séance 4**  
**MSc Data Management 2 — Paris School of Business**  
**Groupe :** Habib KOFFI ; Hariph ASSOUMA ALASSANE.

RADIOPILOT est un concept de pilotage de la performance financière et opérationnelle des centres d'imagerie médicale. Il vise à consolider les indicateurs, comparer le réalisé aux objectifs et repérer rapidement les écarts pour éclairer les décisions.

> **Statut** : dossier de cadrage académique ; usages métier et résultat de test non validés empiriquement. Données de démonstration fictives. Aucun fichier d'entreprise ni donnée personnelle de santé dans le dépôt.

## 1. Contexte et problème

Les responsables financiers et opérationnels doivent analyser ensemble chiffre d'affaires, honoraires, examens, vacations et objectifs de plusieurs centres. La multiplicité des sources peut compliquer le rapprochement et retarder l'identification des écarts.

**HMW.** Comment pourrions-nous aider les directeurs financiers et opérationnels des centres d'imagerie médicale à identifier et comprendre plus rapidement les écarts de performance afin de prendre des décisions adaptées ?

**Insight de conception (à vérifier).** Le DAF et le directeur des opérations cherchent à comprendre une même performance sous deux angles complémentaires : économique et activité. Une vue consolidée pourrait accélérer le repérage des écarts ; cette hypothèse doit être testée.

## 2. Objectif SMART

**En six semaines**, concevoir et tester un **prototype cliquable** de RADIOPILOT sur des **scénarios fictifs**, permettant aux deux personas de consulter des KPI consolidés, de comparer réalisé et budget, de comparer des centres et de repérer les alertes, afin de **réduire d'au moins 30 %** le temps moyen nécessaire pour identifier **trois écarts prédéfinis**, **sans perte d'exactitude**, par rapport à une présentation de référence.

| Lettre | Justification |
|---|---|
| S — Spécifique | Repérage des écarts financiers et opérationnels par le DAF et le directeur des opérations |
| M — Mesurable | Temps moyen sur trois écarts et nombre de réponses exactes, méthode de référence vs prototype |
| A — Atteignable à vérifier | Prototype léger et données fictives ; faisabilité et accès aux testeurs à confirmer |
| R — Pertinent | Répond au besoin hypothétique de pilotage plus rapide |
| T — Temporel | Test visé en fin de semaine 6 |

**Mesure :** (temps référence − temps prototype) / temps référence × 100. Le **30 % est une cible proposée, non un résultat**.

## 3. Périmètre et exclusions

| Inclus dans le MVP (prototype cliquable) | Exclu du MVP |
|---|---|
| Sélection d'un centre et d'une période | Connexion au SI et exploitation réelle des fichiers VIDI |
| Vue consolidée : CA, honoraires, examens, vacations | Analyse approfondie des facteurs possibles (V2) |
| Comparaison réalisé / budget | Suivi détaillé des équipements (V2) |
| Benchmark contextualisé | Temps réel et simulation d'actions (V3) |
| Alertes sur écarts selon scénarios fictifs | **Assistant IA conversationnel (V3, idée retenue)** |
| Information sur définition, source fictive et fraîcheur des KPI | Décision automatisée et mise en production |

Le [prototype HTML interactif](docs/prototype.html) utilise des **scénarios synthétiques fixes**, avec **calculs déterministes exécutés localement** dans le navigateur. Il ne se connecte à aucun SI et ne constitue pas un moteur de calcul industriel.

## 4. Parties prenantes — matrice pouvoir / intérêt

*Positionnements proposés, à confirmer avec l'organisation cible ; aucune validation officielle de VIDI n'est revendiquée.*

| Pouvoir / intérêt | Parties prenantes envisagées | Stratégie |
|---|---|---|
| Élevé / élevé | DAF, directeur des opérations, sponsor potentiel, DSI | Gérer de près ; valider besoins, indicateurs, contraintes |
| Élevé / ciblé | DPO et juridique | Satisfaire et consulter en amont des traitements |
| Moyen / élevé | Équipe data, responsables de centres | Impliquer, recueillir retours et tester |
| Faible / faible | Acteurs indirects à préciser | Surveiller et informer si impact |

La direction, les financeurs, la DSI et les fonctions pouvant bloquer ou conditionner l'usage des données sont explicitement pris en compte.

## 5. Approche projet et justification

**Approche hybride Scrum + CRISP-DM**, proposée pour répondre à des besoins encore incertains et à une disponibilité de données non vérifiée. Trois cycles de deux semaines servent d'unités de préparation et de revue ; ils ne démontrent pas que des sprints Scrum formels ont déjà eu lieu.

| Cycle | Travail envisagé |
|---|---|
| Semaines 1–2 | Comprendre les utilisateurs, inventaire des données candidates, scénario et maquette |
| Semaines 3–4 | Préparer les cas fictifs, formaliser KPI, prototyper les parcours |
| Semaines 5–6 | Tester, chronométrer, corriger et documenter le résultat |

CRISP-DM guide les six phases métier/data et leurs allers-retours ; consulter [docs/04-crisp-dm.md](docs/04-crisp-dm.md). Les dates sont **prévisionnelles**.

## 6. Jalons clés

| Jalon | Échéance relative prévue | Preuve attendue |
|---|---|---|
| J1 — Besoin cadré | Fin S1 | Personas, HMW, hypothèses |
| J2 — Données qualifiées | Fin S2 | Dictionnaire, sources et règles, statut des données |
| J3 — Prototype cliquable | Fin S4 | Parcours et scénarios fictifs |
| J4 — Tests utilisateurs | Fin S5 | Chronométrages et erreurs consignées |
| J5 — Bilan MVP | Fin S6 | Résultat du test, limites et décision |

Ces jalons ne sont **pas** présentés comme déjà atteints.

**Triangle d'or.** Si une contrainte doit céder, **réduire le périmètre fonctionnel** plutôt que sacrifier la fiabilité des KPI ou la protection des informations. Les six semaines et les coûts restent des hypothèses de cadrage.

---

## Livrables

- [Partie 1 — Comprendre](docs/01-comprendre.md)
- [Partie 2 — Idéer et converger](docs/02-ideer.md)
- [Partie 3 — Proposition de valeur](docs/03-valeur.md)
- [Partie 4 — CRISP-DM](docs/04-crisp-dm.md)
- [Partie 5 — MVP](docs/05-mvp.md)
- [Deck PDF](docs/deck.pdf)
- [Journal des usages IA](PROMPTS.md)
- [Visuels et état de la photographie d'atelier](docs/img/README.md)

## Traçabilité et limites de l'exercice

Le Crazy 8 est documenté par une photographie originale fournie par les membres du groupe ; sa transcription et la matrice reconstruite sont présentées dans [la partie 2](docs/02-ideer.md). La sélection des idées a été effectuée **oralement**, sans décompte écrit de points : cette modalité diffère du vote silencieux demandé par l'énoncé et n'est pas présentée comme un vote silencieux à trois points. La photographie doit encore être versée au dossier `docs/img/` pour être accessible à l'enseignante.

Les objectifs, jalons, données et scénarios sont des éléments **proposés** pour le cadrage. Les besoins des personas ne sont pas présentés comme des résultats d'entretiens ; la phase de test du MVP reste planifiée, et non réalisée. Les prompts historiques non disponibles sont explicitement indiqués dans `PROMPTS.md`.

La conformité détaillée et les preuves à produire figurent dans [l'audit](docs/audit-conformite.md). La charte privilégie la maîtrise du périmètre et la fiabilité plutôt qu'un développement prématuré.

## Renforts méthodologiques et démonstrateur vérifiable

- [Prototype interactif autonome (HTML)](docs/prototype.html)
- [Dictionnaire des données et calculs de référence](docs/data-dictionary.md)
- [Jeu de données entièrement fictif](data/radiopilot_synthetique.csv)
- [Protocole de test utilisateur (vierge)](docs/protocole-test.md)
- [Architecture du flux de démonstration](docs/img/architecture-data.svg)
- [Matrice Impact/Effort reconstruite](docs/img/matrice-impact-effort.svg)
- [Visualisation de la story map](docs/img/story-map.svg)
- [Représentation de travail du Value Proposition Canvas](docs/img/vpc-travail.svg) — **ne remplace pas** le modèle PSB Learn.
- [Audit de conformité et preuves manquantes](docs/audit-conformite.md)

Le jeu fictif comporte **4 centres × 3 mois = 12 observations**. Les alertes illustratives utilisent un seuil **−10 %** ; ce seuil est distinct du **30 %** attendu pour l'efficacité du test utilisateur. Aucune métrique n'est présentée comme résultat observé.


### Vérifier les règles de démonstration

Le prototype HTML peut être téléchargé et ouvert localement, sans serveur ni compte. Pour exécuter le contrôle indépendant des 12 observations et des cas limites :

```bash
python scripts/validate_demo.py
```

Le script vérifie des résultats attendus **sur des données fictives** ; il ne prouve pas le gain de temps de 30 %. La photographie originale a été fournie dans la conversation ; elle doit encore être copiée dans le dépôt, et la modalité orale du vote est documentée dans la partie 2.

### Personas visuels

- [Persona Canvas — Habib (DAF)](docs/img/persona-habib.svg)
- [Persona Canvas — Hariph (directeur des opérations)](docs/img/persona-hariph.svg)

Ces canevas reprennent les rubriques du modèle fourni. Ils présentent des **hypothèses** à valider, et non les résultats d'entretiens utilisateurs.
