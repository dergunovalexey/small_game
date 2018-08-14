#!/usr/bin/env python


class BasicGame():
    def __init__(self, start_balance, base_cost):
        # money must by funny in the rich mans world
        self.balance_first_player = start_balance
        self.balance_second_player = start_balance

        # units
        self.archer = 'archer'
        self.knight = 'knight'
        self.soldier = 'soldier'
        self.all_units = (self.archer, self.knight, self.soldier)

        # ids units
        self.id_archer = '0'
        self.id_knight = '1'
        self.id_soldier = '2'
        self.id_exit = '3'
        self.id_all = (self.id_archer, self.id_knight,
                       self.id_soldier, self.id_exit)

        # cost units
        self.cost_unit_map = {self.archer: base_cost,
                              self.knight: base_cost,
                              self.soldier: base_cost}

        # battle
        self.battle = {self.archer: {'win': [self.soldier],
                                     'loss': [self.knight],
                                     'tie': [self.archer]},
                       self.knight: {'win': [self.archer],
                                     'loss': [self.soldier],
                                     'tie': [self.knight]},
                       self.soldier: {'win': [self.knight],
                                      'loss': [self.archer],
                                      'tie': [self.soldier]}}

        # army
        self.army_first_player = []
        self.army_second_player = []

    def add_unit(self, flag_second, unit):
        if not flag_second:
            if self.balance_first_player - self.cost_unit_map[unit] >= 0:
                self.balance_first_player -= self.cost_unit_map[unit]
                self.army_first_player.append(unit)
            else:
                print('not money')
        else:
            if self.balance_second_player - self.cost_unit_map[unit] >= 0:
                self.balance_second_player -= self.cost_unit_map[unit]
                self.army_second_player.append(unit)
            else:
                print('not money')

    def purchase_units(self):
        flag = False
        while True:
            if not flag:
                print('1st user select unit')
                print('Available funds: {}'.format(self.balance_first_player))
            else:
                print('2nd user select unit')
                print('Available funds: {}'.format(self.balance_second_player))

            print('{} - {}'.format(self.id_archer, self.archer))
            print('{} - {}'.format(self.id_knight, self.knight))
            print('{} - {}'.format(self.id_soldier, self.soldier))
            print('{} - exit'.format(self.id_exit))

            unit = input()
            if unit not in self.id_all:
                print('incorrect input. Please try again.')
                continue

            if unit == self.id_exit:
                if not flag:
                    flag = True
                    continue
                else:
                    break

            elif unit == self.id_archer:
                self.add_unit(flag, self.archer)

            elif unit == self.id_knight:
                self.add_unit(flag, self.knight)

            elif unit == self.id_soldier:
                self.add_unit(flag, self.soldier)

    def battle_phase(self):
        while True:
            clashs = tuple(zip(self.army_first_player, self.army_second_player))

            first_army_coef = 0
            second_army_coef = 0

            if not clashs:
                if not self.army_first_player and not self.army_second_player:
                    print('draw')
                elif not self.army_first_player:
                    print('win 2nd player')
                elif not self.army_second_player:
                    print('win 1st player')
                break

            for idx, clash in enumerate(clashs):
                first = clash[0]
                second = clash[1]

                print('{} vs {}'.format(first, second))

                c = self.battle[first]
                if second in c['win']:
                    self.army_second_player.pop(idx - first_army_coef)
                    first_army_coef += 1
                    print('{} win'.format(first))
                elif second in c['loss']:
                    self.army_first_player.pop(idx - second_army_coef)
                    second_army_coef += 1
                    print('{} win'.format(second))
                elif second in c['tie']:
                    self.army_first_player.pop(idx - second_army_coef)
                    self.army_second_player.pop(idx - first_army_coef)
                    first_army_coef += 1
                    second_army_coef += 1
                    print('tie')

    def run_game(self):
        # buy units
        self.purchase_units()
        # run battle
        self.battle_phase()


if __name__ == '__main__':
    game = BasicGame(10, 1)
    game.run_game()
