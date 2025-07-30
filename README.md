# Arena Game

A simple Python console game where two warriors fight in an arena. One is a classic warrior, the other is a mage with magical powers. Each uses their own tactics, and the winner is decided by a combination of their stats and a bit of luck (the dice roll).

## Features

* **Turn-based combat** between two characters: a warrior and a mage.
* **Randomized attacks** using a dice (configurable number of sides).
* **Graphical indicators** for health and (for mage) mana.
* **Simple console output** – see every round and what’s happening.

## How to Play

1. **Clone/download** the repo.
2. **Run `main.py`**:

   ```bash
   python main.py
   ```
3. The fight starts in the console. Just follow along and watch the combat!

## Characters

* **Warrior** (`Bojovnik`): High health, strong defense, basic attacks.
* **Mage** (`Mag`): Lower health, has mana. Charges up mana over turns, and when it’s full, can unleash a magical attack for big damage.

## Code Structure

* `main.py` – Entry point, sets up characters and starts the arena fight.
* `arena.py` – Handles the game logic and turns.
* `bojovnik.py` – Warrior class (shared base for all fighters).
* `mag.py` – Mage class (inherits from Warrior, adds mana/magic logic).
* `kostka.py` – Dice logic (random number generator for attacks).

## Example Output

```
Welcome to the Arena!
Today’s fight: Zalgoren vs Gandalf!
The fight begins...

-------------- Arena --------------
Fighters:

Zalgoren
Health: [######            ]
Gandalf
Health: [#####             ]
Mana:   [####              ]
...
```
