# golf-sim
 A Monte Carlo simulation of the card game Golf

# Background

## Inspiration
Golf is a card game I learned from a childhood friend at a young age. It is a simple, iterative game where players attempt to minimize their score over multiple rounds ("holes"), hence the name. It features a rummy-like draw-and-discard mechanic and creates a unique dynamic through the use of irreversible, public choices. The game is quite simple, and it is my suspicion that the game can be "solved", either in the sense of some closed-form solution or an assessment of simulated strategies. In this project, I will try to create a game framework in Python, model agent-based behavior to explore different strategies, and assess the outcomes of each.

While I have wanted to explore agent-based game simulation for some time, this project was specifically inspired by Bernard Pfann's [UNO simulation project](https://towardsdatascience.com/tackling-uno-card-game-with-reinforcement-learning-fad2fc19355c), which is an fabulous writeup of Monte Carlo and Reinforcement Learning methods. 

## Goals
- Coherently model a game in Python (as much from scratch as possible)
- Create a framework to simulate agents capable of exercising distinct strategies to play a round independently
- Learn what frameworks one can use to assess agent performance
- Assess the performance of different strategies

## Caveat
The way I learned to play this game as a child is unlike most instructions I can find online. The [Wikipedia page for golf](https://en.wikipedia.org/wiki/Golf_(card_game)) lists several variants, none of which specifically match my rules. I will try my best to specify those rules here, because they are what I know best and how I plan to continue to play. 

# Project setup
todo (planning to have run.py file and some kind of config file at root directory, then most of the actual app files within a src directory, then any output data and resulting analysis in an analysis folder, but this is highly tbd)
