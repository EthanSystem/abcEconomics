import abcEconomics as abce
import random


class MoneyAgent(abce.Agent):
    """ agents move randomly on a grid and give_money to another agent in the same cell """

    def init(self, grid):
        self.grid = grid
        """ the grid on which agents live must be imported 初始化随机放置agents在地图"""
        x = random.randrange(self.grid.width)
        y = random.randrange(self.grid.height)
        self.pos = (x, y)
        self.grid.place_agent(self, (x, y))
        self.create('money', random.randrange(2, 10))

    def move(self):
        """ moves randomly 随机移动到邻近之位置1格"""
        possible_steps = self.grid.get_neighborhood(self.pos,
                                                    moore=True,
                                                    include_center=False)
        new_position = random.choice(possible_steps)
        self.grid.move_agent(self, new_position)

    def give_money(self):
        """ If the agent has wealth he gives it to cellmates 如果agent分配1单位财富给家庭成员 """
        cellmates = self.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = random.choice(cellmates)
            try:
                self.give(other.name, good='money', quantity=1)
            except abce.NotEnoughGoods:
                pass

    def report_wealth(self):
        return self['money']
