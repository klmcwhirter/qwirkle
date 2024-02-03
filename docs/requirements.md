# qwirkle - translated requirements

From [stijn-geerits/Qwirkle](https://github.com/stijn-geerits/Qwirkle?tab=readme-ov-file#requirements) translated from Dutch.


## Requirements

> Note this was translated by the "Translate page ..." feature in Firefox. It is pretty rough.

> A hand translation based on this one is available in [../docs/test-requirements.md](../docs/test-requirements.md).

  -  There will be 108 blocks.
  -  There will be six colors: red, orange, yellow, green, blue and purple.
  -  There will be six forms: circle, x, diamond, square, star and clover.
  -  Each block will have a color and a shape.
  -  There will be 3 blocks for any combination of color and shape.
  -  There will be between the two and eight players.
  -  At the beginning of the game, each player will get six blocks.
  -  The player who can lay the longest consecutive line will start the game by laying this line.
  -  At each turn, the player will choose between two options: moor or exchange.
       - The construction of
            - All the blocks will be connected.
            - All the blocks will form a line.
            - Each continuous line will consist of cubes of the same color or shape.
            - A continuous line will never be longer than six blocks.
            - A continuous line will never contain identical blocks.
            - The player will take as many blocks out of the bag as he/she has laid out.
            - If the bag is empty, the player will not take new blocks.
        - Exchange of exchanges
           -  The player will put as many blocks in the bag as he/she takes out.
           -  The blocks taken will be random.
           -  If the bag is empty and the player cannot moor, the player will skip his/her turn.
  -  If all players skip their turn, the game will end.
  -  If the bag is empty, the game will end when a player runs out of cubes.
  -  If the player has built, these points will receive.
        - The player will receive a point for each boarding block per line to which he/she is docking.
        - The player will receive six bonus points when he/she is laying/filling a contiguous line of six cubes.
        - The player will receive six bonus points if it has used up all its blocks first.
  -  The player with the highest score will win.
