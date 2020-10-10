from Practice.__init__ import Data
from Practice.PDE_Contribution_Detail import PDEContribution
from Practice.PDE_Pool_Pair_Detail import PDEPoolPair
from Practice.PDE_Share_Detail import PDEShare
from Practice.PDE_Trading_Fee_Detail import PDETradingFee

import re


class ObjectDetail(Data):
    def get_pde_contributions_list(self):
        raw_contributions_list = self.data['WaitingPDEContributions']
        contributions_list = []
        for raw_contribution in raw_contributions_list:
            name_contribution = re.match(r"\b(waitingpdecontribution)-(\d+)-([\w|-]+)\b", raw_contribution)
            id_contribution = name_contribution.group(3)
            contribution = PDEContribution(raw_contributions_list[raw_contribution])
            contribution.data['ContributionID'] = id_contribution
            contributions_list.append(contribution)
        return contributions_list

    def get_pde_pool_pairs_list(self):
        raw_pool_pairs_list = self.data['PDEPoolPairs']
        pool_pair_list = []
        for raw_pool_pair in raw_pool_pairs_list:
            pool_pair = PDEPoolPair(raw_pool_pairs_list[raw_pool_pair])
            pool_pair_list.append(pool_pair)
        return pool_pair_list

    def get_pde_shares_list(self):
        raw_shares_list = self.data['PDEShares']
        pde_shares_list = []
        for raw_pde_share in raw_shares_list:
            raw_pde_share = re.match(r"(\bpdeshare)-(\d+)-([a-z0-9]+)-([a-z0-9]+)-([a-z0-9A-Z]+\b)", raw_pde_share)
            pde_share_id1 = raw_pde_share.group(4)
            pde_share_id2 = raw_pde_share.group(5)
            pde_share = PDEShare(None)
            pde_share.data['PDEShareID1'] = pde_share_id1
            pde_share.data['PDEShareID2'] = pde_share_id2
            pde_shares_list.append(pde_share)
        return pde_shares_list

    def get_pde_trading_fees_list(self):
        raw_trading_fees_list = self.data['PDETradingFees']
        pde_trading_fees_list = []
        for raw_trading_fee in raw_trading_fees_list:
            raw_trading_fee = re.match(r"(\bpdeshare)-(\d+)-([a-z0-9]+)-([a-z0-9]+)-([a-z0-9A-Z]+\b)",
                                       raw_trading_fee)
            trading_fee_id1 = raw_trading_fee.group(4)
            trading_fee_id2 = raw_trading_fee.group(5)
            pde_trading_fee = PDETradingFee(None)
            pde_trading_fee.data['PDETradingFeeID1'] = trading_fee_id1
            pde_trading_fee.data['PDETradingFeeID2'] = trading_fee_id2
            pde_trading_fees_list.append(pde_trading_fee)
        return pde_trading_fees_list

    def get_beacon_time_stamp(self):
        return self.data['BeaconTimeStamp']
