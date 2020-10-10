from Practice.__init__ import Data


class PDEShare(Data):
    def get_id1(self):
        return self.data['PDEShareID1']

    def get_id2(self):
        return self.data['PDEShareID2']
