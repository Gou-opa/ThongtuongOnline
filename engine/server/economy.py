from engine.db.mysql import db
from configs import *
import datetime, humanize
class Economy:
    table_name = ECONOMY_TABLE_NAME
    @staticmethod
    def tick():
        update_time = datetime.datetime.utcnow()
        db.new_execute(
            "update {} as e inner join (select user_id, sum(gdp*population) as increase from {} group by user_id) as p on p.user_id = e.user_id set e.balance = e.balance + p.increase/86400*(TIME_TO_SEC(TIMEDIFF(%s,IFNULL(e.last_paid, %s)))), income = p.increase, last_paid=%s".format(ECONOMY_TABLE_NAME, PLANET_TABLE_NAME),
            (update_time, update_time, update_time)
        )
    def __init__(self, user_id):
        self.user_id = user_id
        self.balance = 0
        self.income = 0
    def reload(self):
        self.balance, self.income = tuple(db.new_execute(
            "SELECT balance, income FROM {} WHERE user_id = %s".format(ECONOMY_TABLE_NAME),
            (self.user_id)
        ).fetchone().values())
    def display(self, UI_class):
        print(UI_class.content.game.economy.hello)
        print(UI_class.content.game.economy.display.format(humanize.intword(self.balance), humanize.intword(self.income)))