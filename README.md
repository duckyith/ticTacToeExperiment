# ticTacToeExperiment
When against an opponent who always sees forced moves and otherwise plays randomly, what sequence of moves in tic tac toe gives you the best chance of winning? This project seeks to answer that question.

## Basic Game and AI
The game is functional, played in terminal by running the Play executable.

Functionality includes:
- Printed array to show played X's and O's and un-played spaces
- User input 0-8 to play an X (including first move)
- Incorrect and out of range input detection
- Built in quit command
- AI response that plays randomly or recognizes forced moves and blocks/wins

Planned:
- [X] Modified play option to run game fast without user input or prints
- [X] Ability to play itself using the same set moves to try all combinations a set number of times
- [] Recognizing when gameplay doesn't need to continue (ends in tie)
- [X] Tracking statistics for most efficient gameplay
- [X] Analysis of statistics

## AI vs AI
Now the game can play it self, and not just once; When presented with a choice, insstead of choosing randomly it will try every combination from that point, branching out many times recursively and tracking the statistics.

Note: Currently, the game will print every combination and many useful bits of information as it goes, to remove that, just remove the print statements, but I kind of like them :)

## Some statistics from running every game
Remember: The way the AI works is it will see when a player is about to win and block it / win. Other than that it chooses randomly. With this I wantedd to see what the win rates were for each starting move (and over-all)

X in the middle
- wins: 80 (8.62%)
- losses: 32 (3.44%)
- draws: 816 (87.93%)

total games: 928 (x1)

X on the edge
- wins: 380 (14.20%)
- losses: 152 (5.68%)
- draws: 2,144 (80.11%)

total games: 2,676 (x4: 10,704)

X in the corner
- 292 (14.34%)
- 76 (3.73%)
- 1,668 (81.92%)

total games: 2,036 (x4: 8,144)

All Games (took 10 seconds to run where all others were under a second)
- 2,768 (13.99%)
- 944 (4.77%)
- 16,064 (81.22%)

total games: 19,776

## Analysis
Clearly this game is rigged. I mean if I were to design this game, I would want these type of AI's to have a sort of 1/3 chance winning, loosing, and drawing. Balanced, as a game should be. That way the players can use their skill to tip the odds in their favor. Well we already knew that Tic Tac Toe is solved and that if two good playerss play againssst each other they should always tie. The game isn't long enough either to hide a "plan of attack." But that's exactly why we're here. If you were to challange a random, unsuspecting player who is only half-heartedly playing, which opening would give you the best odds of the outcome you want?

Well to start, if you just want to not loose, by this data you should go with the middle which has the lowest losing rate of 3.44%. But overall performace is best found in the corner with a similar loss rate of 3.73% but a promising 14.20% win rate. Maybe avoid starting with an edge but honestly it's not a terrible option either.

But here is where we face the truth: We are only half-heartedly playing as well. In these statistics we wanted to know what gave us the best change of winning if we also played randomly. We also didn't account for symmetry. In the total statistics we count the corners and the edges 4 times even though they are just as likely starts with the exact same results.

So it's time to up our game! What if we played perfectly and knew every combination of the game. How should we play to maximise our odds of beating the average joe who chooses randomly unless forced by anything 2 in a row. We'll have to find out in the next coding adventure!

Planned:
- [] Better Recursion that does not repeat symmetry
- [] Improved AI that will always play the best move (most likely to end in a win)
- [] New statistics that can tell us what the best move from a given position is
- [] Determine the best openning and branches from there
- [] Analyze the utility in using other opennings
