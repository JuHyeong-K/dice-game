import random


class Dice:
    def __init__(self,trial = 5):
        self.dice_options = ('double', 'double','shield', 'skull', 'attack', 'attack') ##주사위의 옵션들
        self.rolled_dice = [] ## 테이블위 주사위들
        self.trial = trial #trial은 총 던질 주사위 갯수
        self.dice_result = {} ## 굴린다음 주사위의 각 이벤트들의 갯수 in dictionary
        
        
    def roll(self):
        for _ in range(1, self.trial+1):
            self.rolled_dice.append(self.dice_options[random.randint(0, 5)])
            
        self.double_num = self.rolled_dice.count('double')
        self.shield_num = self.rolled_dice.count('shield')
        self.skull_num = self.rolled_dice.count('skull')
        self.attack_num = self.rolled_dice.count('attack')
        self.dice_result = {'double': self.double_num, 'shield': self.shield_num, 'skull': self.skull_num, 'attack': self.attack_num}
        print(self.rolled_dice)
        print(self.dice_result)
        return self.dice_result
