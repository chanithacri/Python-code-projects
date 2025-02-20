import random


class RockPaperScisors:
    def __init__(self, u_c):
        self.potions = ['rock', 'paper', 'scissors']
        self.game_options = ['human-human', 'human-easy', 'human-meadium', 'human-hard']
        self.wining_op = {'rock' : 'scissors', 'paper' : 'rock', 'scissors' : 'paper'}
        self.comp_wins = 0
        self.human_wis = 0
        self.user_choice = u_c
        self.com_choice = ''

    def win_finder(self):
        wining = self.wining_op
        com = self.com_choice
        use = self.user_choice
        while True:
            if self.comp_wins == 5 or self.human_wis == 5:
                if self.comp_wins == 5:
                    print('Comuter wins!')
                else:
                    print('You won!')
                break
            if use == wining[com]:
                self.comp_wins  += 1
                print(f'Comuper gets this. {com}')
            elif com == wining[use]:
                self.human_wis += 1
                print(f'You got this one! {com}')
            else:
                print(f'Draw {com} - {use}')


    def easy(self):
        self.com_choice = random.choice(self.game_options)
        self.win_finder()

