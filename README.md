# automata
Playground for cellular automata stuff

## Installation & Running

Needs numpy and pygame installed

``pip install pygame``

``pip install numpy``

Run with
``python main.py``

## Configuration

In main, there is the line

```configs.create_Thunderbird(world, 70,50)```

which controls which of several configurations to start with.
Use as many of these as you like to start with different setup configurations.
Any mobile automata can interact with other automata to produce new behaviours.

Currently configured automata include
* Oscillators
  * Blinkers
  * Toad
* Spaceships
  * Glider
* Methuselahs (long lived automata)
  * R-Pentamino
  * Thunderbird

# Gallery
__The Thunderbird Methuselah__

This is the last 30 seconds of one of the standard set pieces running
![alt text](imgs/thunderbird-methuselah.gif)




