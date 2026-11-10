# Protocole de test MVP — plan, non résultats

## Objectif et hypothèse

Tester **H1** : l'interface RADIOPILOT permet aux deux personas de repérer trois écarts plus rapidement que la présentation de référence, avec un **gain moyen cible ≥ 30 %**, **sans baisse de l'exactitude**.

## Matériel

- Version de référence : feuille de reporting fictive, contenant les mêmes informations que la maquette mais réparties par sections.
- Version MVP : [prototype HTML cliquable RADIOPILOT](prototype.html) sur **scénarios fictifs**, consultable localement après téléchargement. Les éventuelles erreurs de la maquette doivent être corrigées avant les séances de test.
- Deux ensembles de trois écarts de difficulté comparable préparés à l'avance (A et B).
- Feuille de chronométrage, grille de correction avec centre/période/écart exact, questionnaire d'observation.
- Consentement à participer aux tests et minimisation des données personnelles de test.

## Participants et plan

**Cible proposée :** au moins un profil financier et un profil opérationnel, idéalement plusieurs personnes par profil. Si seulement deux personnes participent, le test est **exploratoire**, non une preuve généralisable. Les mêmes participants ne doivent pas voir d'avance les réponses attendues.

Alterner l'ordre pour réduire l'effet d'apprentissage :

| Groupe de passage | Étape 1 | Étape 2 |
|---|---|---|
| A | Référence, scénario A | Prototype, scénario B |
| B | Prototype, scénario A | Référence, scénario B |

Comparer la complexité des scénarios et recueillir les observations qualitatives. Le taux d'erreur est enregistré pour chaque support.

## Formulaire vierge à utiliser pendant le test

| Participant (code) | Profil | Support | Scénario | Début / fin | Durée sec | Réponses exactes / 3 | Erreurs / blocages |
|---|---|---|---|---|---|---|---|
| À renseigner | À renseigner | À renseigner | A/B | À renseigner | À renseigner | À renseigner | À renseigner |

**Aucune ligne de résultat n'est préremplie.**

## Calculs et verdict

- `T_ref` = durée moyenne sur support de référence.
- `T_mvp` = durée moyenne sur prototype.
- `gain_% = 100*(T_ref-T_mvp)/T_ref` si `T_ref > 0`.
- `exactitude = réponses correctes / (3 × nombre d'essais)`.
- **Succès selon H1 :** `gain_% ≥ 30 %` ET `exactitude_mvp ≥ exactitude_ref`.
- **Échec/inconcluant :** seuil manqué, données de mesure insuffisantes, scénario non équivalent ou biais non maîtrisé ; documenter précisément.

Ne pas annoncer « H1 validée » sans tableau de résultats effectifs et traçables. Une amélioration moyenne ne démontre pas une significativité statistique avec un échantillon minuscule.

## Liste de vérification du prototype

- [ ] Changement centre et période avec valeurs cohérentes.
- [ ] Calcul relatif masqué si budget = 0.
- [ ] Donnée manquante clairement affichée comme non évaluable.
- [ ] Trois alertes négatives de référence retrouvables, avec seuil fictif affiché.
- [ ] Comparaisons contextualisées (IRM/Scanner, équipements).
- [ ] Définition, source fictive et date accessibles pour tout KPI.
- [ ] Aucun chiffre ni résultat de test réel inventé.

## Risques du protocole

Effet d'apprentissage, ordre de passage, familiarité outil, différence de complexité, différence de fonctions, recrutement limité, temps atypiques et confusions entre comparaison descriptive et causalité. Conserver ces limites dans le bilan.
