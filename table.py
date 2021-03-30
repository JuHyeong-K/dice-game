class Table:
    def __init__(self, player, banker):
        self.player = player
        self.banker = banker
    
    def start_game(self):
        print(f"player's balance: {self.player.balance}")
        balance_input = int(input('배팅 금액: '))
        self.player.balance = balance_input

    def print_status(self):
        print(f'[BANK] HP: {self.banker.hp}/10, DICE: {self.banker.dice}/15, SHIELD: {self.banker.shield}/6\n[PLAYER] HP: {self.player.hp}/10, DICE: {self.player.dice}/15, SHIELD: {self.player.shield}/6')

    def player_turn(self):
        # run_double
        if self.player.dice < 5:
            dice = Dice()
            dice.trial = self.player.dice
            self.player.dice = 0
            dice = dice.roll()
            self.player.dice += dice['double']
        else:
            dice = Dice().roll()
            self.player.dice -= 5
            self.player.dice += dice['double']
        # run_shiled
        if self.player.shield + dice['double'] >= 6:
            self.player.shield = 6
        else:
            self.player.shield += dice['shield']
        # run_skull
        if self.player.shield > 0:
            if self.player.shield < dice['skull']:
                dice['skull'] -= self.player.shield
                self.player.shield = 0
            else:
                self.player.shield -= dice['skull']
                dice['skull'] = 0
        if self.player.hp - dice['skull'] <= 0:
            self.player.hp = 0
        else:
            self.player.hp -= dice['skull']
        # run_acttack
        if self.banker.shield > 0:
            if self.banker.shield < dice['attack']:
                dice['attack'] -= self.banker.shield
                self.banker.shield = 0
            else:
                self.banker.shield -= dice['attack']
                dice['attack'] = 0
        if self.banker.hp - dice['attack'] <= 0:
            self.banker.hp = 0
        else:
            self.banker.hp -= dice['attack']
        print(f'[BANK] HP: {self.banker.hp}/10, DICE: {self.banker.dice}/15, SHIELD: {self.banker.shield}/6\n[PLAYER] HP: {self.player.hp}/10, DICE: {self.player.dice}/15, SHIELD: {self.player.shield}/6')
    
    def banker_turn(self):
        # run_double
        if self.banker.dice < 5:
            dice = Dice()
            dice.trial = self.banker.dice
            self.banker.dice = 0
            dice = dice.roll()
            self.banker.dice += dice['double']
        else:
            dice = Dice().roll()
            self.banker.dice -= 5
            self.banker.dice += dice['double']
        # run_shiled
        if self.banker.shield + dice['double'] >= 6:
            self.banker.shield = 6
        else:
            self.banker.shield += dice['shield']
        # run_skull
        if self.banker.shield > 0:
            if self.banker.shield < dice['skull']:
                dice['skull'] -= self.banker.shield
                self.banker.shield = 0
            else:
                self.banker.shield -= dice['skull']
                dice['skull'] = 0
        if self.banker.hp - dice['skull'] <= 0:
            self.banker.hp = 0
        else:
            self.banker.hp -= dice['skull']
        # run_acttack
        if self.player.shield > 0:
            if self.player.shield < dice['attack']:
                dice['attack'] -= self.player.shield
                self.player.shield = 0
            else:
                self.player.shield -= dice['attack']
                dice['attack'] = 0
        if self.player.hp - dice['attack'] <= 0:
            self.player.hp = 0
        else:
            self.player.hp -= dice['attack']
        print(f'[BANK] HP: {self.banker.hp}/10, DICE: {self.banker.dice}/15, SHIELD: {self.banker.shield}/6\n[PLAYER] HP: {self.player.hp}/10, DICE: {self.player.dice}/15, SHIELD: {self.player.shield}/6')
            

    def choose_winner(self):
        if self.player.hp > self.banker.hp:
            print('플레이어 승!')
        elif self.player.hp < self.banker.hp:
            print('플레이어 패배..')
        else:
            print('무승부')

