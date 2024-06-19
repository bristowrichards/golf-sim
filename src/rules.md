# rules
This file contains plain language rules for reference.

## players
Golf is a card game typically played between 2-4 players with a single deck of playing cards. More decks can be used with more players present, but I'm not sure what the best ratio would be as I typically play with fewer than 5 players. Jokers may optionally be included; see **scoring**.

## setup
Each player receives 4 face-down cards in a 2x2 grid in front of them. Each player may secretly view the 2 cards closest to them, and they may only view these cards once, before play begins. 

Once cards are dealt and players secretly view 2 cards from their grids, one card is flipped to initiate the discard pile. The player to the left of the dealer may then begin their turn.

## objective
The objective of the game is to achieve the lowest score of the table over multiple rounds of play. Rounds are sometimes referred to as "holes" per the golf theme.

## scoring
Each card is worth a number of points based on its rank (suits are irrelevant):

| Card | Points |
|------|-------|
| Ace | 1 |
| 2-10 | face value |
| Jack-Queen | 10 |
| King | 0 |
| Joker (Optional) | -5 |

At the end of the round, each card in a player's 2x2 grid will be face-up. The player's score will be the sum of these 4 cards, with the following caveat: *a pair of cards "cancels out" both cards, resulting in a score of 0 for those two cards.*

Example 1: Alice has one Ace, one Four, and two Jack cards. Alice's score would be `1+4+10+10=25`, but the Jack cards cancel out, so Alice's score is `1 + 4 + 0 + 0 = 5`.

Example 2: Bob has one King and three Eight cards. Bob's score would be `0+8+8+8=24`, but *one pair* of the Eight cards cancels out, so Bob's score is `0 + 0 + 0 + 8 = 8`. Note that, in a three-of-a-kind scenario, only two of the cards "cancel" and the third retains its face value.

Example 3: Charlie plays in a game where Jokers are included. Charlie's hand has two Joker cards, one 8, and one Queen. Unfortunately for Charlie, the pair of Jokers *also* cancels out, so instead of the score being `-5 + -5 + 8 + 10 = 8`, this hand yeilds a score of `0 + 0 + 8 + 10 = 18`. 

## turns
When a player begins their turn, they have four cards in their grid and there is one face-up card in the discard pile. The player will have 4 turns each round. 

The player has 3 options during each turn:

1. Select one of their face-down cards to turn face-up and "lock"
2. Draw the top card from the discard pile, replacing it with one of their face-down cards in their grid. The new card from the discard pile becomes face-up and "locked" in the player's grid. The player discards the former card from the grid, placing it in the discard pile face-up. 
3. Draw a new card from the deck to place on top of the discard pile. The player may do this only once per turn to "refresh" the discard pile option. The player must then choose between options 1 and 2 for their final action. 

At the end of each turn, the player will have gained one more face-up card, either through flipping face-down cards or exchanging from the discard pile. A face-up card is considered "locked". Once a card is "locked" it may not be moved, exchanged, discarded, or flipped back into a face-down position. Locked cards may practically be considered a part of a player's ongoing score within a round because they are set in place and may not be removed. The only way to "remove" a locked card is to acquire another card of the same rank to create a pair, thus cancelling the values of each of those two cards (note again that three-of-a-kinds of a rank are considered to be a single card of that rank and two 0-value cards). 

## concluding the round
Once each player has each of their four cards upright and locked, the round ends. Players tally their scores, a new player deals, and a new round begins. 

## concluding the game
One game of Golf typically consists of multiple rounds ("holes"). Following the thematic guidelines of real-life golf, I typically play either 3, 6, 9, or 18 holes, depending on how much time I anticipate having. Each round typically only lasts 2-3 minutes. Each individual round can be volatile, with players typically scoring between 2-5 points but sometimes scoring as low as -5 and sometimes as high as 30. For this reason, playing multiple rounds allows for an ostensibly fairer assessment of players' strategies and skills. 
