import random

def lucky_rand(n):
    return max(random.randint(0,n), random.randint(0,n))

class Frame:
    def __init__(self, balls):
        self.balls = balls
        #example: [3,7] is a spare
        #example: [10] is a strike

    def is_strike(self):
        return self.balls[0] == 10

    def is_spare(self):    
        return len(self.balls) > 1 and self.balls[0] + self.balls [1] == 10

    #first_frame = frame([3,6]) # example frame

class Player:
    def __init__(self, name):
        self.name = name
        self.frames = []

    def calc_score(self):
        score = 0
        for i, frame in enumerate(self.frames):
            if i == 9:
                if frame.is_strike():
                    score += 10 + frame.balls[1] + frame.balls[2]
                elif frame.is_spare():
                    score += 10 + frame.balls[2]
                else:
                    score += frame.balls[0] + frame.balls[1]

            elif frame.is_strike():
                score += 10 + self.frames[i+1].balls[0]
                if len(self.frames[i+1].balls) > 1:
                    score += self.frames[i+1].balls[1]
                else:
                    score += self.frames[i+2].balls[0]

            elif frame.is_spare():
                score += 10 + self.frames[i+1].balls[0]
            
            else:
                score += frame.balls[0] + frame.balls[1]

        return score

class Game:
    def __init__(self, players):
        self.players = players
        self.current_frame = 0

    def play(self):
        for i in range(10):
            self.bowl_frame()
        for player in self.players:
            print(f'The final score for {player.name} is {player.calc_score()}')
    
    def bowl_frame(self):
        # if self.current_frame <= 9:
        self.current_frame += 1
        for player in self.players:
            balls = []

            # first throw
            balls.append(lucky_rand(10))
            if balls[0] < 10:
                # if they didnt knock down all the pins, they get a second chance
                balls.append(lucky_rand(10 - balls[0]))

                # on the final frame of the game, you get a third ball if you throw a spare
                if balls[0] + balls[1] == 10 and self.current_frame == 10:
                    balls.append(lucky_rand(10))

            # if they get a strike on the last frame they get two extra balls
            if balls[0] == 10 and self.current_frame == 10:
                balls.append(lucky_rand(10))
                if balls[1] == 10:
                    balls.append(lucky_rand(10))
                else:
                    balls.append(lucky_rand(10 - balls[1]))
            
            player.frames.append(Frame(balls))

players = []
for player in ['Alice', 'Bob', 'Carol', 'Dan']:
    players.append(Player(player))

the_game = Game(players)
the_game.play()
