# 01 — Comprendre le problème

> RADIOPILOT | MSc Data Management 2 — PSB | État : cadrage et hypothèses, pas validation empirique.
> Les personas sont des profils de conception, non des personnes interrogées. Leurs citations sont illustratives.

## Persona 1 — Habib, 38 ans, directeur administratif et financier (DAF)

**Contexte.** Supervise la performance économique de plusieurs centres d'imagerie médicale ; rapproche périodiquement les résultats financiers des budgets avant de les communiquer à la direction.
**Objectif.** Obtenir rapidement une vision fiable, consolidée et actualisée des résultats pour orienter les décisions budgétaires.
**Frustration principale — supposition.** Les données de plusieurs sources nécessitent rapprochements et contrôles, ce qui peut retarder l'analyse des écarts.
**Citation illustrative, non recueillie en entretien.** « Je veux comprendre rapidement pourquoi un centre n'atteint pas son budget, sans attendre plusieurs fichiers et retraitements. »

## Persona 2 — Hariph, 35 ans, directeur des opérations

**Contexte.** Supervise les volumes d'examens, les vacations, la disponibilité des ressources et l'utilisation des équipements.
**Objectif.** Détecter les évolutions défavorables d'activité et décider des actions opérationnelles adaptées.
**Frustration principale — supposition.** La séparation entre indicateurs financiers et opérationnels peut compliquer l'explication d'une baisse d'activité.
**Citation illustrative, non recueillie en entretien.** « Quand l'activité d'un centre baisse, je veux savoir si cela vient des vacations, des examens ou d'un autre facteur pour pouvoir agir. »

## Trois affirmations : faits et suppositions

| Affirmation | Classement | Justification / vérification |
|---|---|---|
| Le pilotage envisagé repose sur plusieurs familles d'indicateurs : CA, honoraires, examens et vacations. | Fait de cadrage du **concept** ; son usage réel chez l'organisation cible reste à vérifier | Vérifier les définitions et documents métiers autorisés, sans publier de données internes. |
| Le DAF perd du temps à rapprocher plusieurs sources financières. | Supposition | Entretien réel et chronométrage d'une préparation de reporting ; conserver la preuve avec accord. |
| Une vue financière et opérationnelle commune facilite les décisions du directeur des opérations. | Supposition | Test comparatif d'une maquette, temps et exactitude de détection des écarts. |

## Question HMW — Design Thinking

**Comment pourrions-nous aider les directeurs financiers et opérationnels des centres d'imagerie médicale à identifier et comprendre plus rapidement les écarts de performance afin de prendre des décisions adaptées ?**

Cette question ne présuppose ni plateforme, ni tableau de bord, ni IA.

## Question métier — CRISP-DM, phase 1

**Comment exploiter les données financières et opérationnelles des centres d'imagerie médicale pour aider le DAF et le directeur des opérations à repérer les écarts significatifs entre l'activité réalisée et les objectifs, à examiner leurs causes possibles et à prioriser les actions correctives ?**

**Décisions concernées :** sélectionner les centres ou périodes à analyser en priorité et identifier les actions pertinentes à instruire. La solution n'affirme pas établir des causalités automatiquement.

**Preuves à obtenir :** validation des deux profils par des utilisateurs réels, entretien ou observation de la pratique actuelle, vérification de l'affirmation métier, source autorisée pour les KPI.
