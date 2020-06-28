# Overview

Because the NHL draft lottery is on everyone's mind, I came up with a crazy idea to revamp the draft lottery.  My one goal, make watching the lottery drawing exciting.  And I'm talking about the actual drawing of the balls powerball style, not just declaring which team is in which draft spot.  The idea is to have an all-day event that can be televised, fans of teams can gather to cheer on the balls that get picked, and basically make a huge spectacle of complete random luck.  First a Q&A before we get started:

**Q: This sounds dumb, why is this necessary?**  
A: it is dumb, and it is not necessary.  The whole point is to try and revamp the system to make it fun and exciting

**Q: Do you really think people would get together and cheer balls being picked out of a lottery machine?**  
A: I'm so starved for sports right now, I cheered two raindrops racing down my apartment window.  So yes, I would love some drawn out sports related content.  My model for success is the NFL draft.  They have hundreds of fans sitting around waiting hours to hear that their GM picked a new backup center.  The point is getting hardcore fans of the team together to celebrate and cheer things.

**Q: Does this new method give the worse teams better odds of getting the first pick**  
A: It does not give the worst team better odds, but it gives eveyrone in the bottom 9 a good chance for snagging that first spot.  I'll throw the percentages below.

## The New Draft Lottery

The way that my newly envisioned draft lottery will work is that each team has a number of balls in a bag that get picked by random each round until there is one team left who did not have a ball picked.  This team is "eliminated".  The eliminated team then gets the worst available draft position, all balls from non-eliminated teams are readded, and the next round starts.  So the gimmick is that if your team's ball is picked, you move to the next round.  In order to set odds and give added weight towards picking the teams lower down in the standings, they will get more balls in the bag.

For example, if we had 4 teams (A, B, C, D) and they finished in the standings where D was last, C was 2nd to last, B was 3rd to last, and A was 4th to last, here's how the bag would be set up.  A would have 1 ball, B would have 2 balls, C would have 3 balls, and D would have 4 balls.  In the first round, the balls are drawn in this order:
```
1. a ball was picked for D
2. a ball was picked for C
3. a ball was picked for C
4. a ball was picked for D
5. a ball was picked for B
```
This means that team A is eliminated and gets the 4th overall pick, while teams C, D, and B move onto the next round.  Team A's ball are removed from the bag, team B, C, and D's balls are readded to the bag, and the 2nd round goes as follows:
```
1. a ball was picked for C
2. a ball was picked for C
3. a ball was picked for D
```
This means that team B is eliminated and gets the 3rd overall pick, while teams C and D move onto the next round.  Team B's balls are removed from the bag, team C and D's balls are readded to the bag, and the 3rd round goes as follows:
```
1. a ball was picked for C
```
This means that team D is eliminated and gets the 2nd overall pick, while team C gets the 1st overall pick.  

Running 10,000 simulations, here is a table with the percentage chance of each draft position  
| Team | 1st   | 2nd   | 3rd   | 4th   |
|------|-------|-------|-------|-------|
| A    | 4.1%  | 11.9% | 28.6% | 55.4% |
| B    | 17.1% | 27.0% | 31.9% | 24.1% |
| C    | 31.3% | 32.5% | 23.2% | 13.0% |
| D    | 47.6% | 28.7% | 16.3% | 7.5%  |

## How would this work for the 2020 draft?

For the 2020 draft, Detroit would get 15 balls, Ottawa 14 balls, San Jose 13 balls, Los Angeles 12 balls, Anaheim 11 balls, New Jersey 10 balls, Buffalo 9 balls, and then the qualifier teams from A to H would get 8 decreasing to 1, respectively.  After 10,000 simulations, here percentage table:
| Team | 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th | 10th | 11th | 12th | 13th | 14th | 15th |
|------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| DET | 23.00% | 17.96% | 14.63% | 11.26% | 8.49% | 6.99% | 5.18% | 3.88% | 2.99% | 2.21% | 1.57% | 1.02% | 0.54% | 0.19% | 0.09% |
| OTT | 20.14% | 16.46% | 13.16% | 11.67% | 9.71% | 8.02% | 6.19% | 4.58% | 3.51% | 2.49% | 2.07% | 1.10% | 0.49% | 0.34% | 0.07% |
| SJS | 16.34% | 15.62% | 13.56% | 11.72% | 10.12% | 8.06% | 6.63% | 5.69% | 4.33% | 3.07% | 2.03% | 1.23% | 0.84% | 0.56% | 0.20% |
| LAK | 12.55% | 13.25% | 12.68% | 11.44% | 10.62% | 9.24% | 8.12% | 6.26% | 5.13% | 4.09% | 2.78% | 1.84% | 1.06% | 0.65% | 0.29% |
| ANA | 9.59% | 10.50% | 11.47% | 11.71% | 11.33% | 10.51% | 8.32% | 7.37% | 6.26% | 4.55% | 3.60% | 2.15% | 1.46% | 0.93% | 0.25% |
| NJD | 7.38% | 9.20% | 10.06% | 10.60% | 10.85% | 9.81% | 9.94% | 8.45% | 6.79% | 6.25% | 4.24% | 2.94% | 1.94% | 0.96% | 0.59% |
| BUF | 5.14% | 6.67% | 8.60% | 10.00% | 9.82% | 10.94% | 9.93% | 9.16% | 8.70% | 7.15% | 5.69% | 3.67% | 2.58% | 1.32% | 0.63% |
| NHLA | 3.12% | 5.02% | 6.35% | 7.44% | 8.95% | 10.25% | 11.00% | 10.45% | 9.56% | 8.89% | 6.74% | 5.40% | 3.65% | 2.17% | 1.01% |
| NHLB | 1.61% | 2.84% | 4.62% | 6.13% | 7.32% | 9.26% | 10.15% | 11.03% | 10.66% | 10.41% | 9.18% | 7.48% | 4.93% | 3.10% | 1.28% |
| NHLC | 0.85% | 1.62% | 2.63% | 4.55% | 5.93% | 7.64% | 9.68% | 10.98% | 11.56% | 10.86% | 11.09% | 9.50% | 6.85% | 4.03% | 2.23% |
| NHLD | 0.22% | 0.68% | 1.53% | 2.29% | 4.13% | 5.01% | 7.49% | 9.69% | 11.56% | 12.69% | 12.85% | 11.89% | 9.68% | 7.06% | 3.23% |
| NHLE | 0.06% | 0.17% | 0.63% | 0.89% | 2.08% | 2.96% | 4.71% | 7.23% | 10.03% | 12.06% | 14.40% | 15.12% | 13.61% | 10.29% | 5.76% |
| NHLF | 0.00% | 0.01% | 0.08% | 0.29% | 0.57% | 1.13% | 2.17% | 3.93% | 6.25% | 10.12% | 13.47% | 17.46% | 18.48% | 15.77% | 10.27% |
| NHLG | 0.00% | 0.00% | 0.00% | 0.01% | 0.08% | 0.18% | 0.46% | 1.26% | 2.53% | 4.48% | 8.52% | 14.45% | 20.86% | 25.38% | 21.79% |
| NHLH | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | 0.03% | 0.04% | 0.14% | 0.68% | 1.77% | 4.75% | 13.03% | 27.25% | 52.31% |

The worst teams in the league have the possiblity of getting a very unfavorable draft, and can drop more than current draft process by dropping more than 3 spaces.  However, bubble playoff teams have a worse shot of getting that top pick.  In my new and improved draft system, the Qualifier teams have a combined 5.8% chance of snagging the top spot, whereas in the current system the Qualifier teams had a 24.5% chance of getting the first overall draft pick.

## Final Q&A

**Q: This draft process gives the worst teams lesser odds of getting good picks, why didn't you solve that?**  
A: I was just trying to make the draft process fun and exciting.  You can change the amount of balls each team has to vary the percentages of each slot, but this system is based on chance and giving every team a shot at at a good draft position.

**Q: There are like 100+ balls, are there lottery ping pong ball machines big enough for 100 balls?**  
A: I've got no clue

**Q: Aren't there lawyers to make sure all the balls are identical and that no tampering is possible?  Especially considering marking the balls adds extra weight, and oils from people's hands if they touch the ball could effect the outcome of the entire process, not to mention that adding and removing balls adds extra conditionalities that the teams lawyers would object to?**  
A: stop ruining my dreams.

# How to run

To run, just download this project into PyCharm and run the main() function in `Draft.py`.  Use a Python 3+ interpreter, and you may need to pull in the 
`copy` package into the interpreter.

# Additional notes

Please do not expect tests or regular updates, this is a pet project moreso as a proof of concept than anything well maintained. If there is interest in it, I will expand it out to make it customizable and easier to use for all major league teams.
