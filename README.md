# Dragons and Destiny: A Virtual AI-Powered RPG

This repository contains **Dragons and Destiny**, a virtual tabletop RPG platform that leverages multi-agent AI systems to create dynamic, player-driven narratives. Unlike traditional games with static scripts, this system uses an **AI Dungeon Master** to interpret intent, weave complex plots, and adapt the world in real-time based on player choices.

---

## 🎮 Project Overview

**Dragons and Destiny** transforms the classic RPG experience into a digital environment where two players collaborate with specialized AI agents to build a unique fantasy world.

### Key Features

* 
**2-Player Support**: Designed for two human players to interact simultaneously within the same story arc.


* 
**AI Dungeon Master**: Acts as the "brains" of the game, handling story progression and logic.


* 
**Dynamic Narrative**: Generates initial settings and character backgrounds based on raw user descriptions.


* 
**Memory Integration**: Maintains a persistent record of game history and player context to ensure narrative consistency.



---

## 🛠 Technical Architecture

The project is built using the **Moya Framework**, a multi-agent orchestration platform that allows specialized AI agents to work together without heavy manual coding.

### 1. Multi-Agent Orchestration

The system utilizes "Divide and Conquer" logic, where different tasks are handled by autonomous agents:

* 
**Narrator Agent**: Responsible for generating initial world settings, creating character sketches, and dynamically updating the plot based on player moves.


* 
**Memory Agent**: Stores the entire game history, plot points, and player context to provide contextually relevant outputs.


* 
**NPC Agent**: Manages interactions with non-player characters that appear in the story when mentioned in player inputs.



### 2. The Moya Framework Advantage

* 
**Automatic Routing**: Moya automatically routes user prompts to the most appropriate agent without needing human-defined algorithms.


* 
**Scalability**: The modular nature of the framework allows for the addition of new specialized agents (e.g., combat or inventory) as needed.


* 
**Maintainability**: Division of labor between agents makes the codebase easier to manage and debug.



### 3. Core Functionalities

* 
**Input Interpretation**: The AI understands player intent behind text-based moves.


* 
**Plot Weaving**: Crafts engaging narratives that follow a logical progression.


* 
**Dynamic Adaptation**: Reacts instantly to player choices, such as a player stealing an item from another.



---

## 📜 Execution Workflow

The game follows a structured initialization and gameplay loop:

### Phase 1: Game Setup

1. 
**Initial Setting**: Players enter a general idea, theme, location, and villain (e.g., "desert in China").


2. 
**Character Sketches**: Each player provides a brief description (e.g., "Archer" or "Godzilla").


3. 
**Initialization**: The AI generates a comprehensive backstory, including character names, backgrounds, and a common goal.



### Phase 2: Gameplay Loop

* 
**Player Move**: Players enter text-based moves (e.g., "the archer sees a coconut tree and shoots at it").


* 
**AI Processing**: The Orchestrator routes the input to the Narrator and Memory agents.


* 
**Narrative Update**: The AI generates a result for the action and updates the scene description.



---

## 🚀 Technical Specifications & Requirements

* 
**Language**: Python.


* 
**Framework**: Moya.


* 
**Pre-requisite**: **Python 3.10** is required (though some documentation may incorrectly state 3.8).


* 
**Deployment Environment**: Best suited for **greenfield, cloud-native projects** where modernization is possible due to computational overhead.



---

## 🚧 Limitations & Future Scope

### Current Limitations

* 
**Performance**: There is extra computational overhead due to the dynamic orchestration process.


* 
**Complexity**: Faced some issues with the multi-agent orchestrator stability during development.


* 
**Classification**: Current implementation uses a very simple classifier; future versions could integrate advanced NLP/ML classifiers.



### Future Scope

* 
**Expanded Agents**: Integration of specialized agents for **Combat Resolution**, **Inventory Management**, and **Quest Tracking**.


* 
**Enhanced Memory**: Implementation of more sophisticated memory management for long-term sessions.


* 
**In-Game Scoring**: Adding a score factor based on how much a player's input changes the system state, which could be used to buy character upgrades.


* 
**Multi-Level Gameplay**: Transitioning from single-scene encounters to multi-level game structures.



---

## 👥 Contributors

* 
**Shravani K** 


* 
**Saloni Goyal** 



---

**Would you like me to help you draft the Python code for the proposed "Combat Resolution" or "Inventory Management" agents?**
