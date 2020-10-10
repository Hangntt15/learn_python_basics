from Practice.__init__ import Data


class PDETradingFee(Data):
    def get_id1(self):
        return self.data['PDETradingFeeID1']

    def get_id2(self):
        return self.data['PDETradingFeeID2']
