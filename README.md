# *Scrabble Game*

## *Description*

Scrabble is a board game in which two to four players score points by placing tiles that contain a single letter on a game board divided into a 15x15 grid. The tiles must form words that, in online reading, are formed from left to right in rows or downwards in columns, and must be included in a standard dictionary.

Each player starts the game with seven tiles and on each turn, a player can decide to place a word on the board, swap tiles for new tiles, or pass their turn. The game ends when a player has used all their tiles and there are no more tiles to draw from or when a player passes 3 times in a row.

## *Rules*

- The game is played by two to four players.
- Each player starts the game with seven tiles.
- The game board is divided into a 15x15 grid.
- The tiles must form words that, in online reading, are formed from left to right in rows or downwards in columns, and must be included in https://dle.rae.es/.
- The game ends when a player has used all their tiles and there are no more tiles to draw from or when a player passes 3 times in a row.
- The player with the highest score wins.
- For more Information about the rules, visit https://es.wikipedia.org/wiki/Scrabble

## *Installation*

1. Make sure you have git and docker installed. Once you have them, clone the repository.

```bash
git clone https://github.com/um-computacion-tm/scrabble-2023-FernandoWeigandt.git
```

2. Build the Docker image

```bash
docker build -t scrabble .
```

3. Run the Docker image

```bash
docker run -it scrabble
```


## *Contact*

Fernando Weigandt - f.weigandt@alumno.um.edu.ar - Universidad de Mendoza

# Main
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/scrabble-2023-FernandoWeigandt/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/scrabble-2023-FernandoWeigandt/tree/main)

# Develop
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/scrabble-2023-FernandoWeigandt/tree/develop.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/scrabble-2023-FernandoWeigandt/tree/develop)

# Maintainability

[![Maintainability](https://api.codeclimate.com/v1/badges/51b497c3e452c5148aaf/maintainability)](https://codeclimate.com/github/um-computacion-tm/scrabble-2023-FernandoWeigandt/maintainability)

# Coverage

[![Test Coverage](https://api.codeclimate.com/v1/badges/51b497c3e452c5148aaf/test_coverage)](https://codeclimate.com/github/um-computacion-tm/scrabble-2023-FernandoWeigandt/test_coverage)
