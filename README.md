# Battleship Agent

Self-initiated Project for CSCI 3202 Introduction to Artificial Intelligence (Fall 2026)

## Introduction

This projects aims to create two agents to sink all ships in the Battleship game in as little moves as possible and compare them with each other as well as an agent that makes purely random moves.

## Battleship Game

We implemented a single-player, terminal version of the game.

The game board can be initialised with either random generation or manual placement.

For each turn, players can choose a tile that has not been played before, and the board returns whether it is a hit or miss and if a ship was sunk.

The game ends when all ships are sunk.

## DFS Agent

Starting from the center of the board, the agent searches diagonally adjacent tiles until it gets a hit, then searches adjacent tiles to find the rest of the ship.

## Probability Density Agent

*To be implemented in second half*

This agent calculates the next best move by determining which area of the board is more likely to have ships given the hits and misses so far.

## Random Agent

Uses `random` to choose tiles.