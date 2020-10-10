from Practice.__init__ import Data


class PDEContribution(Data):
    def get_contributor_address_str(self):
        return self.data['ContributorAddressStr']

    def get_token_id_str(self):
        return self.data['TokenIDStr']

    def get_amount(self):
        return self.data['Amount']

    def get_tx_req_id(self):
        return self.data['TxReqID']

    def get_id_contributor(self):
        return self.data['ContributionID']
