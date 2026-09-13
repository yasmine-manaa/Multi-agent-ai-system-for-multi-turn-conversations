# Mini-Projet Agent IA - Système Multi-Agents

Système conversationnel multi-agents utilisant LangChain et LangGraph pour répondre aux demandes d'aide scolaire.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Utilisateur                                 │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                 Intent Agent                                  │
│  - Analyse l'intention de l'utilisateur                       │
│  - Identifie les informations manquantes                     │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
              ┌────────────────┐
              │  Supervisor     │
              │  (Routage)      │
              └────────┬────────┘
                       │
           ┌───────────┴───────────┐
           │                       │
           ▼                       ▼
┌─────────────────────┐  ┌─────────────────────┐
│ Clarification Agent │  │  Response Agent    │
│ (Questions)         │  │  (Réponse finale)  │
└─────────────────────┘  └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Evaluation Agent    │
                         │ (Score de qualité)  │
                         └─────────────────────┘
```

## 📦 Installation

1. **Créer l'environnement virtuel** :
```bash
python -m venv venv
```

2. **Activer l'environnement** :
```bash
# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Linux/Mac
source venv/bin/activate
```

3. **Installer les dépendances** :
```bash
pip install langchain langgraph langchain-google-genai python-dotenv pydantic
```

4. **Configurer les variables d'environnement** :
Créer un fichier `.env` avec votre clé API Google :
```
GOOGLE_API_KEY=votre_clé_api_ici
```

## 🚀 Utilisation

### Baseline (Simple LLM)
```bash
python baseline.py
```

### Agents Individuels
```bash
# Intent Agent
python agents/intent_agent.py

# Clarification Agent
python agents/clarification_agent.py

# Response Agent
python agents/response_agent.py

# Evaluation Agent
python agents/evaluation_agent.py
```

### Système Multi-Agents Complet
```bash
python graph.py
```

### Expérimentation Comparative
```bash
python run_experiment.py
```

## 📁 Structure du Projet

```
mini-projet-agentic-ai/
├── agents/
│   ├── intent_agent.py          # Analyse d'intention
│   ├── clarification_agent.py   # Questions de clarification
│   ├── response_agent.py        # Génération de réponses
│   ├── evaluation_agent.py      # Évaluation de qualité
│   └── supervisor.py            # Logique de routage
├── baseline.py                  # Baseline simple
├── graph.py                     # Graphe LangGraph
├── state.py                     # État partagé
├── scenarios.py                 # Scénarios de test
├── run_experiment.py            # Script d'expérimentation
├── test_llm.py                  # Test de connexion LLM
└── .env                         # Variables d'environnement
```

## 🔧 Agents

### Intent Agent
Analyse le message utilisateur et détecte :
- L'intention principale
- Le type de tâche
- Les informations manquantes

### Clarification Agent
Transforme les informations manquantes en questions naturelles.

### Response Agent
Génère des réponses adaptées au contexte et à l'intention.

### Evaluation Agent
Évalue la pertinence des réponses générées (score 0-1).

### Supervisor
Décide du routage entre les agents selon l'état du système.

## 📊 Métriques

Le système évalue :
- Taux de succès des réponses
- Score de pertinence (0-1)
- Détection d'informations manquantes
- Complexité des réponses

## 🎯 Scénarios de Test

20 scénarios variés couvrant :
- Questions claires
- Demandes vagues
- Différents niveaux scolaires
- Différentes matières
- Complexités variables

## 📝 Remarques

- Le modèle utilisé est `gemini-3.6-flash` (modèles plus anciens non disponibles)
- L'environnement virtuel doit être activé pour exécuter les scripts
- Les résultats d'expériences sont sauvegardés en CSV


