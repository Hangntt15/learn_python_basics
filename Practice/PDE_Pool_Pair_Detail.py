from Practice.__init__ import Data


class PDEPoolPair(Data):
    def get_token1_id_str(self):
        return self.data['Token1IDStr']

    def get_token1_pool_value(self):
        return self.data['Token1PoolValue']

    def get_token2_id_str(self):
        return self.data['Token2IDStr']

    def get_token2_pool_value(self):
        return self.data['Token2PoolValue']
