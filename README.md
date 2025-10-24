# AI-Catan-Agent

**Overview**

This project is an AI agent designed to play Settlers of Catan, with a long-term goal of mastering the Cities and Knights expansion — the most complex version of the game. Because Catan involves a wide range of strategic decisions, the project is divided into incremental stages that progressively build toward a fully autonomous and competitive AI player.

**Project Structure and Goals**

The agent will be developed step-by-step, focusing on one core component of gameplay at a time. Each stage builds upon the previous one, allowing the system to grow in complexity and intelligence in a controlled way.

**Stage 1: Game State Representation
**
The foundation of the AI is an accurate representation of the game state. This includes:
	•	Board layout (tiles, numbers, ports)
	•	Resource distribution
	•	Player turns and actions
	•	Settlement and city placements

Initially, the AI is given its first two settlements manually. Later, it will evaluate the board and determine optimal starting placements autonomously using heuristics or reinforcement signals.

**Stage 2: Reinforcement Learning Setup
**
The learning backbone of the agent is Q-learning (or another RL variant if the complexity requires adaptation).
Key components include:
	•	State encoding: Translating board conditions into structured numerical representations.
	•	Action space: Possible moves such as building, trading, or buying development cards.
	•	Q-values: Representing the expected reward of taking specific actions in each state.

**Stage 3: Reward System
**
The AI learns through rewards tied to in-game objectives:
	•	Building settlements or cities
	•	Achieving “Longest Road” or “Largest Army”
	•	Gaining resources efficiently
	•	Increasing victory points

Rewards are contextual and depend on the AI’s current resources, position, and strategy. This system encourages the AI to balance short-term gains (e.g., resource optimization) and long-term goals (e.g., victory conditions).

**Stage 4: Trading Logic
**
Trading is one of the most human aspects of Catan. It involves both strategy and negotiation.
Our approach introduces it gradually:
	1.	Step 1: AI only accepts trades that directly support its active goals.
	2.	Step 2: AI evaluates trades in the context of potential goal switching — determining if accepting a trade might lead to a more advantageous strategy.
	3.	Step 3: AI initiates trades, considering board state, player relationships, and dynamic conditions.

This structured approach helps the AI develop rational, adaptive trading behavior over time.

**Stage 5: Simulation and Training
**
The agent will train across thousands of simulated Catan games to develop competitive play strategies.
Throughout training:
	•	We collect performance metrics and gameplay logs.
	•	We analyze patterns in decision-making and outcomes.
	•	We refine the state, reward, and trade systems to improve adaptability and consistency.

**Future Work
**	•	Expand from basic Catan to Cities and Knights ruleset.
	•	Incorporate multi-agent training for more dynamic environments.
	•	Add heuristic and neural policy comparisons for decision refinement.
	•	Develop a visualization dashboard to track learning progress and in-game decision flow.

**Summary**

By breaking down Catan’s complexity into structured, learnable modules, this project aims to create an AI capable of understanding and excelling at a deeply strategic board game. From resource management to trading psychology, each step brings the agent closer to playing Catan not just logically — but competitively.
