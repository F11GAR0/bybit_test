import requests
import time
import json
import pybit

from pybit.unified_trading import HTTP


class Bybit:

    def __init__(self, key, secret):

        self.session = HTTP(
            api_key=key,
            api_secret=secret
        )

    def __del__(self):
        
        pass

    def _send_request(self):

        pass

    def _generate_timestamp(self):

        """
        Return a millisecond integer timestamp.
        """

        return int(time.time() * 10 ** 3)

    def withdraw(self, address : str, amount : str, coin="USDT", chain="TRX"):

        return self.session.withdraw(
                coin=coin,
                chain=chain,
                address=address,
                amount=amount,
                tag= None,
                timestamp=self._generate_timestamp(),
                accountType="FUND"
            )