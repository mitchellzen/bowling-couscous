

class Player:
    def __init__(self, index):
        self.id = index
        self.score = 0
        self.frames = []
        self.open_strike = False
        self.open_spare = False

    def play(self, game):
        current_frame = []
        shots_available = 2
        score = 0
        print("Frame: {} Score: {}".format(game.current_frame_id + 1, self.score))
        while shots_available > 0:
            spare = False
            try:
                bowl = int(input("Bowl a number from 0-10: ").strip())
                assert -1 < bowl < 11
            except ValueError:
                print("Please select one of the available options.")
                continue
            except AssertionError:
                print("There are only ten pins in bowling.")
                continue
            current_frame.append(bowl)
            shots_available = 2 - len(current_frame)
            if shots_available == 0:
                spare = current_frame[0] + current_frame[1] == 10
            if spare:
                self.open_spare = True
                shots_available = 0
            if bowl == 10:
                if self.open_strike:
                    score += 20
                self.open_strike = True
                shots_available = 0
            elif self.open_strike and not spare and len(current_frame) > 1:
                score += 10 + current_frame[0] + bowl
                self.open_strike = False
            elif self.open_spare and not spare :
                score += 10 + bowl - self.frames[game.current_frame_id - 1][0]
                self.open_spare = False
            if not spare and bowl != 10:
                score += bowl
            if game.current_frame_id == 9:
                if bowl == 10 or spare:
                    shots_available = 3 - len(current_frame)
        self.frames.append(current_frame)
        self.score += score


class Bowling:
    def __init__(self, number_of_users):
        self.number_of_users = number_of_users
        self.current_user_id = 0
        self.current_frame_id = 0
        self.users = [Player(i) for i in range(number_of_users)]

    def play(self):
        while self.current_frame_id < 10:
            for user in self.users:
                print("Player {}".format(user.id + 1))
                user.play(game)
            self.current_frame_id += 1
        winning_score = 0
        winner = None
        for player in self.users:
            if player.score > winning_score:
                winning_score = player.score
                winner = player.id
        print("Winner is Player {} with score {}".format(winner + 1, winning_score))


if __name__ == "__main__":
    print('Welcome to Bowling')
    number_of_users = None
    while number_of_users is None:
        try:
            number_of_users = int(input('How many players? '))
        except ValueError:
            print("Please select a number.")
    game = Bowling(number_of_users)
    game.play()
    print('Game Over.')
