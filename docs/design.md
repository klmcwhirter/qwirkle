# qwirkle - design

* Come up with new name  - Qwirkle => "Shaped Colors"

## Tile

| Shape | Code |  | Color | Code |
|---|---|---|---|---|
| Circle | O |  | Red | R |
| Criss-cross | X |  | Orange | O |
| Diamond | ^ |  | Yellow | Y |
| Square | # |  | Green | G |
| Starburst | * |  | Blue | B |
| Clover | + |  | Purple | P |

Example:
- RO, OO, YO => Red Circle, Orange Circle, Yellow Circle
- R+, R#, R^ => Red Clover, Red Square, Red Diamond

## Game Play
* Capture moves in a log that can be replayed to re-calculate the score from scratch, for example.
* Each move should carry metadata to identify player and provide scoring and display hints.
* Model board as a dynamic grid for display purposes only.
	* because a Qwirkle is defined as a line of 6 tiles, add segments of 6x6 tiles to extend the board (early guess)
	* start with a 12x12 board (4 segments) that is roughly centered on the display (if GUI) - favor top/left for now; i.e., exact center is (5,5)
	
| | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **0** | (0,0) | (1,0) | (2,0) | (3,0) | (4,0) | (5,0) | (6,0) | (7,0) | (8,0) | (9,0) | (10,0) | (11,0) |
| **1** | (0,1) | (1,1) | (2,1) | (3,1) | (4,1) | (5,1) | (6,1) | (7,1) | (8,1) | (9,1) | (10,1) | (11,1) |
| **2** | (0,2) | (1,2) | (2,2) | (3,2) | (4,2) | (5,2) | (6,2) | (7,2) | (8,2) | (9,2) | (10,2) | (11,2) |
| **3** | (0,3) | (1,3) | (2,3) | (3,3) | (4,3) | (5,3) | (6,3) | (7,3) | (8,3) | (9,3) | (10,3) | (11,3) |
| **4** | (0,4) | (1,4) | (2,4) | (3,4) | (4,4) | (5,4) | (6,4) | (7,4) | (8,4) | (9,4) | (10,4) | (11,4) |
| **5** | (0,5) | (1,5) | (2,5) | (3,5) | (4,5) | **(5,5)** | (6,5) | (7,5) | (8,5) | (9,5) | (10,5) | (11,5) |
| **6** | (0,6) | (1,6) | (2,6) | (3,6) | (4,6) | (5,6) | (6,6) | (7,6) | (8,6) | (9,6) | (10,6) | (11,6) |
| **7** | (0,7) | (1,7) | (2,7) | (3,7) | (4,7) | (5,7) | (6,7) | (7,7) | (8,7) | (9,7) | (10,7) | (11,7) |
| **8** | (0,8) | (1,8) | (2,8) | (3,8) | (4,8) | (5,8) | (6,8) | (7,8) | (8,8) | (9,8) | (10,8) | (11,8) |
| **9** | (0,9) | (1,9) | (2,9) | (3,9) | (4,9) | (5,9) | (6,9) | (7,9) | (8,9) | (9,9) | (10,9) | (11,9) |
| **10** | (0,10) | (1,10) | (2,10) | (3,10) | (4,10) | (5,10) | (6,10) | (7,10) | (8,10) | (9,10) | (10,10) | (11,10) |
| **11** | (0,11) | (1,11) | (2,11) | (3,11) | (4,11) | (5,11) | (6,11) | (7,11) | (8,11) | (9,11) | (10,11) | (11,11) |

* add segments consistently so the board remains _rectangular_ to minimize extension operations.
    * e.g., if the board consists of 5 horizontal segments and 3 vertical segments (5x3)
		* then, extending vertically should add 5 horizontal segments so the board becomes 5x4 segments
		* similarly, extending horizontally should add 3 vertical segments so the board becomes 6x3 segments
		* when a tile is placed on any board edge, that is the time to extend (before placing) in that direction only
		* if a tile is placed in one of the 4 corners, extend in both directions (before placing)
	* index lines
		* horizontal first - top to bottom
		* vertical next - left to right
	* when board is resized - update move log and index

# References
- [marianosegura/Qwirkle](https://github.com/marianosegura/Qwirkle) - pits 2 hand coded bots against each other (pygame)
- [MarcLindenbach/qwirkle](https://github.com/MarcLindenbach/qwirkle) (TUI - python 2.x)
- [stijn-geerits/Qwirkle](https://github.com/stijn-geerits/Qwirkle) - junior level impl (pygame)
