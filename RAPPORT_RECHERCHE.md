# Rapport de Recherche - Système Multi-Agents Conversationnel

## 1. Introduction

Ce projet explore la mise en œuvre d'un système conversationnel multi-agents utilisant LangChain et LangGraph pour répondre aux demandes d'aide scolaire. L'objectif est de comparer une approche baseline (LLM simple) avec une architecture multi-agents structurée.

## 2. Problématique

Les LLMs modernes sont puissants mais peuvent manquer de structure et de cohérence dans les réponses complexes. L'approche multi-agents vise à :
- Mieux structurer les réponses
- Identifier les informations manquantes
- Évaluer la qualité des réponses
- Maintenir un contexte conversationnel cohérent

## 3. Méthodologie

### 3.1 Architecture Baseline
- Un seul LLM qui répond directement aux questions
- Pas de structuration des réponses
- Pas d'évaluation de qualité

### 3.2 Architecture Multi-Agents
- **Intent Agent** : Analyse l'intention et détecte les informations manquantes
- **Clarification Agent** : Pose des questions ciblées
- **Response Agent** : Génère des réponses contextuelles
- **Evaluation Agent** : Évalue la pertinence des réponses
- **Supervisor** : Orchestre le flux entre agents

### 3.3 Technologie
- **LangChain** : Framework pour applications LLM
- **LangGraph** : Gestion du flux entre agents
- **Google Gemini 3.6-flash** : Modèle LLM utilisé
- **Pydantic** : Validation et structuration des données

## 4. Implémentation

### 4.1 Structure du Projet
```
mini-projet-agentic-ai/
├── agents/           # Différents agents spécialisés
├── state.py          # État partagé entre agents
├── graph.py          # Graphe d'orchestration
├── baseline.py       # Version baseline
└── run_experiment.py # Script de comparaison
```

### 4.2 Défis Techniques
- **Adaptation du modèle** : Les modèles Gemini 1.5 n'étant plus disponibles, adaptation à Gemini 3.6-flash
- **Gestion des réponses** : Format de réponse variable (liste vs texte) nécessitant un traitement adaptatif
- **Activation de l'environnement** : Nécessité d'activer l'environnement virtuel pour accéder aux dépendances

## 5. Résultats

### 5.1 Fonctionnalité
- ✅ Baseline opérationnel
- ✅ Intent Agent détecte correctement les intentions
- ✅ Clarification Agent formule des questions pertinentes
- ✅ Response Agent génère des réponses contextuelles
- ✅ Graphe LangGraph orchestre correctement les agents

### 5.2 Observations
- L'approche multi-agents fournit des réponses plus structurées
- La détection d'informations manquantes améliore la pertinence
- L'évaluation permet un contrôle qualité des réponses

## 6. Analyse Comparative

### 6.1 Avantages de l'Approche Multi-Agents
- **Structuration** : Réponses plus organisées
- **Flexibilité** : Adaptation selon le contexte
- **Qualité** : Évaluation systématique
- **Traçabilité** : Journal des actions des agents

### 6.2 Limites
- **Complexité** : Architecture plus complexe à maintenir
- **Coût** : Plusieurs appels LLM par requête
- **Latence** : Temps de réponse plus long

## 7. Perspectives

### 7.1 Améliorations Possibles
- Ajout d'agents spécialisés par matière
- Intégration de mémoires à long terme
- Optimisation du routage entre agents
- Interface utilisateur interactive

### 7.2 Applications
- Systèmes de tutorat en ligne
- Assistants pédagogiques
- Support client intelligent
- Aide à la décision

## 8. Conclusion

Ce projet démontre la viabilité de l'approche multi-agents pour les systèmes conversationnels. Bien que plus complexe qu'un simple LLM, elle offre des avantages significatifs en termes de structuration, qualité et cohérence des réponses.

L'implémentation avec LangChain et LangGraph s'est révélée efficace pour orchestrer les différents agents et maintenir un état partagé cohérent.

## 9. Bibliographie

- LangChain Documentation: https://python.langchain.com/
- LangGraph Documentation: https://langchain-ai.github.io/langgraph/
- Google AI Documentation: https://ai.google.dev/
- Pydantic Documentation: https://docs.pydantic.dev/
