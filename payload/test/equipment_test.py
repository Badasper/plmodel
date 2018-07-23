from model.equipment import Equipment
from model.condition import Condition
from model.query import QueryData


class TestCaseEquipment:

    def test_get_data(self):
        equip = Equipment('WF1')
        condition = Condition(25, 'amb')
        query = QueryData(condition, 'GF')
        assert equip.get_pos_name() == 'WF1'
        assert equip.get_data(query) == {
            'x': [5725, 5800, 5900, 6225, 6725],
            'y': [-10, -20, -25, -19, -18]
        }
