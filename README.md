# 🐉 Dragons and Destiny: A Virtual AI-Powered RPG (Prototype for Dungeons & Dragons)

This repository contains **Dragons and Destiny**, a virtual tabletop RPG platform that leverages multi-agent AI systems to create dynamic, player-driven narratives. Unlike traditional games with static scripts, this system uses an **AI Dungeon Master** to interpret intent, weave complex plots, and adapt the world in real time based on player choices.

---

## 🎮 Project Overview

**Dragons and Destiny** transforms the classic RPG experience into a digital environment where two players collaborate with specialized AI agents to build a unique fantasy world.

### ✨ Key Features

- **2-Player Support**  
  Designed for two human players to interact simultaneously within the same story arc.

- **AI Dungeon Master**  
  Acts as the “brains” of the game, handling story progression, logic, and rule interpretation.

- **Dynamic Narrative**  
  Generates initial settings and character backgrounds based on raw user descriptions rather than predefined scripts.

- **Memory Integration**  
  Maintains a persistent record of game history and player context to ensure narrative consistency across turns.

---

## 🛠 Technical Architecture

The project is built using the **Moya Framework**, a multi-agent orchestration platform that enables specialized AI agents to collaborate without heavy manual control logic.

### 1. Multi-Agent Orchestration

The system follows a *Divide-and-Conquer* philosophy, where different responsibilities are handled by autonomous agents:

- **Narrator Agent**  
  Generates the initial world setting, creates character sketches, and dynamically updates the plot based on player actions.

- **Memory Agent**  
  Stores the complete game history, key plot points, and player context to ensure continuity and coherence.

- **NPC Agent**  
  Manages interactions with non-player characters that emerge organically from player inputs.

---

### 2. The Moya Framework Advantage

- **Automatic Routing**  
  Moya intelligently routes user prompts to the most appropriate agent without requiring hand-written routing logic.

- **Scalability**  
  The modular agent-based design allows easy integration of new agents (e.g., combat, inventory, quest systems).

- **Maintainability**  
  Clear separation of responsibilities between agents simplifies debugging, testing, and long-term evolution of the codebase.

---

### 3. Core Functionalities

- **Input Interpretation**  
  The system understands player intent behind natural language, not just surface-level commands.

- **Plot Weaving**  
  Crafts coherent and engaging narratives that maintain logical progression across turns.

- **Dynamic Adaptation**  
  Reacts instantly to unexpected player choices (e.g., betrayal, theft, or creative problem-solving).

---

## 📜 Execution Workflow

The game follows a structured initialization and gameplay loop.

### Phase 1: Game Setup

1. **Initial Setting**  
   Players provide a general idea, theme, location, and villain  
   *(e.g., “a desert kingdom in ancient China”)*.

2. **Character Sketches**  
   Each player enters a brief description of their character  
   *(e.g., “Archer”, “Godzilla”)*.

3. **Initialization**  
   The AI generates a complete backstory, including character names, motivations, and a shared overarching goal.

---

### Phase 2: Gameplay Loop

- **Player Move**  
  Players submit text-based actions  
  *(e.g., “The archer spots a coconut tree and shoots at it”)*.

- **AI Processing**  
  The Orchestrator routes the input to the Narrator and Memory agents.

- **Narrative Update**  
  The AI resolves the action, updates the world state, and advances the story.

---

## 🚀 Technical Specifications & Requirements

- **Language**: Python  
- **Framework**: Moya  
- **Pre-requisite**: Python **3.10** (some documentation may incorrectly mention 3.8)  
- **Deployment Environment**: Best suited for **greenfield, cloud-native projects**, as multi-agent orchestration introduces computational overhead.

---

## 🚧 Limitations & Future Scope

### Current Limitations

- **Performance**  
  Additional computational cost due to dynamic agent orchestration.

- **Complexity**  
  Stability challenges encountered while coordinating multiple autonomous agents.

- **Classification**  
  Current implementation relies on a basic classifier; future versions can integrate advanced NLP/ML-based intent classification.

---

### Future Scope

- **Expanded Agents**  
  Dedicated agents for:
  - Combat Resolution  
  - Inventory Management  
  - Quest Tracking  

- **Enhanced Memory**  
  More sophisticated long-term memory handling for extended campaigns.

- **In-Game Scoring System**  
  A scoring metric based on how significantly a player’s actions alter the world state—usable for character upgrades.

- **Multi-Level Gameplay**  
  Evolution from single-scene encounters to multi-level, multi-arc campaign structures.

---

## 👥 Contributors

- **Shravani K**  
- **Saloni Goyal**

---

**Would you like help drafting the Python code for the proposed _Combat Resolution_ or _Inventory Management_ agents?**
