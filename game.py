class BasicGame():
    def __init__(self):
        # money must by funny in the rich mans world
        self.start_balance = 10  # $
        self.balance_first_player = self.start_balance
        self.balance_second_player = self.start_balance

        # units
        self.archer = 'archer'
        self.knight = 'knight'
        self.soldier = 'soldier'
        self.all_units = (self.archer, self.knight, self.soldier)

        # cost units
        self.base_cost = 1  # $
        self.cost_unit_map = {self.archer: self.base_cost,
                              self.knight: self.base_cost,
                              self.soldier: self.base_cost}

        # battle
        # self.battle = {'{0.archer}_{0.archer}'.format(self): 'tie',
        #                ''}

        # army
        self.army_first_player = []
        self.army_second_player = []

    def purchase_units(self, units, first_player):
        """

        :param units: list or smph
        :param first_player: bool
        :return:
        """
        if first_player:
            army = self.army_first_player
            balance = self.balance_first_player
        else:
            army = self.army_second_player
            balance = self.balance_second_player

        if not isinstance(units, (list, tuple)):
            raise Exception, 'units not list or tuple'

        for unit in units:
            if unit not in self.all_units:
                raise Exception, 'unit is not acceptable'

            cost = self.cost_unit_map[unit]

            if balance - cost >= 0:
                balance -= cost
                army.append(unit)

    # def battle_phase(self):
    #     while True:
    #         for index in range(len(len))
