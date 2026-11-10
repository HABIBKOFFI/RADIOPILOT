# 04 — Projet data : CRISP-DM

> Référence : question métier dans [01-comprendre.md](01-comprendre.md). Le MVP est un **prototype cliquable avec scénarios fictifs**, et non une connexion opérationnelle aux systèmes VIDI. Objectif de test : **≥ 30 % de réduction** du temps d'identification de trois écarts, **sans détériorer l'exactitude**.

## 1. Business Understanding

**Question métier.** Comment aider les DAF et directeurs des opérations à repérer les écarts de performance, examiner leurs facteurs possibles et prioriser les actions ? 
**Décision à améliorer.** Identifier quels centres et périodes nécessitent une analyse prioritaire.
**KPI métier.** CA réalisé et budgété, écart en euros et en %, évolution temporelle, examens, honoraires, vacations, comparaison contextualisée entre centres.
**Succès métier proposé.** Mesure chronométrée des mêmes trois écarts sur deux méthodes, avec une réduction du temps moyen d'au moins 30 %, sans perte d'exactitude. Ce seuil est un objectif **non encore testé**.
**Lien SMART.** Voir la charte dans [README.md](../README.md).

## 2. Data Understanding — dictionnaire de collecte envisagée

Ces noms de fichiers figurent dans le document de travail et désignent des **sources candidates**, pas des fichiers collectés, audités ou rendus accessibles au groupe. Aucun jeu de données réel n'est intégré à ce dépôt.

| Donnée | Source envisagée | Disponibilité pour ce rendu | Volume estimé | Fraîcheur cible (hypothèse) | Sensibilité a priori | Vigilance |
|---|---|---|---|---|---|---|
| Cotations / montants / examens | `stat_cotation_detail.csv` | Non vérifiée | À mesurer, non communiqué | Mensuelle pour test ; à confirmer | Potentiellement personnelle/sensible si détail patient | Double comptage, identifiants, dates |
| Facturation | `stat_facture_detail.csv` | Non vérifiée | À mesurer | Mensuelle, à confirmer | Potentiellement personnelle | Périmètre facture vs cotation |
| Forfaits techniques | `ft_detail.csv` | Non vérifiée | À mesurer | Mensuelle, à confirmer | Potentiellement personnelle | Rattachement aux examens |
| Sites et cabinets | `site.csv`, `cabinet.csv` | Non vérifiée | À mesurer | Lors de changement du référentiel | Faible à personnelle selon contenu | Identifiants et correspondances |
| Types d'examens | `examen_type.csv` | Non vérifiée | À mesurer | Lors de changement nomenclature | Faible si nomenclature seule | Codes et catégories |
| Vacations | Plannings | Non vérifiée | À mesurer | Mensuelle, à confirmer | Personnelle possible (professionnels) | Annulations, périodes |
| Budgets / objectifs | Budget financier | Non vérifiée | À mesurer | Mensuelle, à confirmer | Confidentielle entreprise | Version budgétaire, périmètre |
| Cas tests fictifs | Scénarios synthétiques créés pour la démonstration | À créer | 2 à 4 centres et 3 périodes, **dimension cible fictive** | Fixe pour test | Aucune donnée réelle | Scénarios cohérents, documentés |

**Règle de confidentialité.** Même si des sources internes sont connues, ne verser sur GitHub ni données de santé, ni fichiers financiers confidentiels, ni enregistrements professionnels. Aucun nom de patient, professionnel ou structure réelle dans les démonstrations. L'autorisation et la base légale d'un éventuel traitement réel restent à établir.

## 3. Data Preparation

Contrôles prévus : dates et devises homogènes, clés centre/période stables, doublons, valeurs manquantes, règles de jointure, rapprochement facturation/cotations, période et périmètre budgétaire, nullité des budgets.

**Garde-fous :** ne pas diviser par zéro ; statut « non calculable » si budget nul/absent ; alerte « données insuffisantes » en cas de doute ; ne jamais afficher « pas d'alerte » quand la donnée manque ; comparer les centres avec contexte (modalités, équipements, taille/activité) avant d'interpréter les rangs.

## 4. Modeling

**Méthode MVP :** règles déterministes transparentes illustrées par des scénarios simulés, sans entraîner de modèle :
- Écart CA (€) = CA réalisé − CA budgété.
- Écart CA (%) = (CA réalisé − CA budgété) / CA budgété × 100, seulement si CA budgété ≠ 0 et renseigné.
- Une alerte est visible si un seuil métier *proposé et à valider* est dépassé ; pas de seuil prétendument acté.
- Benchmark : comparaison à période et périmètre communs, avec mentions explicites des différences de centres.

**Pourquoi pas l'IA générative dans le MVP ?** Le calcul exact des écarts relève de règles testables et non d'une prédiction. L'**assistant IA conversationnel**, idée retenue du groupe, demeure envisagé en **V3**, avec interrogation des indicateurs et explication des sources, garde-fous et contrôle de confidentialité. Il n'est pas supprimé.

## 5. Evaluation

| Dimension | Métrique | Seuil d'acceptation proposé | Preuve attendue |
|---|---|---|---|
| Technique | Exactitude sur jeu de référence fictif | 100 % des cas de calcul et cas limites prévus | Tableau de cas et résultats attendus |
| Technique | Concordance des totaux consolidés | 0 écart inexpliqué | Rapprochements documentés |
| Métier | Temps moyen pour repérer trois écarts | Réduction ≥ 30 % vs méthode de référence | Chronométrage et protocole |
| Métier | Exactitude de détection | Pas de baisse vs méthode de référence | Grille des trois bonnes réponses |
| Responsable | Compréhension de la définition et de la fraîcheur | Chaque indicateur du test expose définition, source fictive et date | Vérification de US05 |

**Aucun résultat de test n'est actuellement revendiqué.** Exemple illustratif fictif : 12 min → 7 min donne 41,67 % ; ce chiffre n'est pas un résultat utilisateur.

## 6. Deployment

**MVP :** [prototype HTML cliquable](prototype.html), cas d'utilisation fictifs, calculs locaux déterministes et aucune connexion aux données réelles. Un prototype fonctionnel en production n'est pas annoncé. **Utilisation future envisagée :** outil de pilotage et alertes, selon les droits métiers. Maintenance d'une future solution : équipe data pour qualité/calculs, responsables métier pour validation des KPI, DSI pour exploitation, DPO et juridique selon traitement ; rôles non confirmés.

## Itérations, risque prioritaire, RGPD

**Allers-retours :** Business Understanding ↔ Data Understanding en semaines 1–2 ; Data Preparation ↔ Modeling en semaines 3–4 ; Evaluation ↔ préparation/maquette en semaines 5–6. Cette répartition est **prévisionnelle**.

**Donnée la plus risquée :** lien fiable entre montants financiers, examens et centres/périodes. Un rapprochement défectueux peut rendre des écarts trompeurs. Alternative MVP : cas synthétiques vérifiés, et tester explicitement l'utilité de la présentation, non l'intégration réelle.

**RGPD :** le prototype doit privilégier des données fictives et sans personnes identifiables. Pour un projet réel, documenter avant traitement : finalités déterminées, catégories, qualification des données de santé ou personnelles, base légale pertinente (sans supposer le consentement), minimisation, accès, sécurité, durées de conservation et suppression, information des personnes et, si applicable, AIPD et contrat avec prestataires. **La durée de conservation et la base légale sont à définir avec le responsable de traitement et le DPO ; aucune durée n'est inventée.**

## Traçabilité des user stories

| Story | Données et métadonnées liées |
|---|---|
| US01 | CA, honoraires, examens, vacations, centre, période |
| US02 | CA réalisé, budget, centre, période, état du budget |
| US03 | Centres, périodes, types d'activités et indicateurs comparables |
| US04 | Écarts, seuils à valider, statuts de qualité |
| US05 | Dictionnaire KPI, source (fictive pour prototype), fraîcheur, préférences facultatives si activées |


## Annexes techniques et traçabilité des règles

- [Architecture conceptuelle des flux fictifs](img/architecture-data.svg)
- [Dictionnaire, granularité, contrôles et cas de référence](data-dictionary.md)
- [Jeu de scénarios totalement synthétiques](../data/radiopilot_synthetique.csv)
- [Protocole de test et seuil de réussite](protocole-test.md)

**Deux pourcentages différents :** `-10 %` est un **seuil d'alerte fictif de démonstration** ; `30 %` est un **objectif de gain de temps** à mesurer auprès d'utilisateurs. Aucun de ces seuils ne constitue une performance prouvée.
