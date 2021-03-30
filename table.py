class Table:
  def __init__(self, name):
    self.name = name

  def start_game(self, bet):
    self.bet = bet
    player.set_init()
    bank.set_init()

  def print_status(self):
    print('[BANK] HP: {}/10, DICE: {}/15, SHIELD: {}/6'.format(bank.hp, bank.dice_left, bank.shield_left), [PLAYER] HP: {}/10, DICE: {}/15, SHIELD: {}/6'.format(player.hp, player.dice_left, player.shiled_left), sep='\n')
