'''
Michael Oliver
https://mcoliver.com

Alpaca Options Challenge
https://alpaca.markets/options


eyJzIjogeyJBQVBMIjogMC4yNTEzMzQyMjgyNzc5NTgzNywgIkdPT0ciOiAwLjMzMzQ0ODg2MjYwMDY5NjcsICJBTVpOIjogMC4zNzQwODEwOTg4Nzk4MTUyLCAiTlZEQSI6IDAuNTM4MDU1NTA1MTU3MTA2MiwgIlRTTEEiOiAwLjU5Nzg3OTcxNzcxNTMwNjEsICJMTFkiOiAwLjI3NjY4OTgzNjIwNDE4ODI0LCAiSlBNIjogMC4yMTc2OTk1ODA0ODg2OTkyMiwgIlhPTSI6IDAuMjYyMjk2MTMzMzUxNzYzMiwgIkFWR08iOiAwLjMyNzYyMDM5NTAwODc0MTQ2LCAiViI6IDAuMTg4NDk2MDM0NDY5ODMzNjIsICJKTkoiOiAwLjE2NDcwMTExMTkyMTc2NDY4LCAiUEciOiAwLjE1MDIwMjgzNDg2MTMzMTQzLCAiTUEiOiAwLjIwODU5MTc5MTUxNjIyODcsICJIRCI6IDAuMjM1MTYzMzg1NTE5OTkwNzgsICJBREJFIjogMC4zNDkxNjc1NzA2MzgxMDAzLCAiTVJLIjogMC4xOTMyODA0OTI1MzQyNTk5NywgIkNPU1QiOiAwLjIwMzk5MjQyMjMzODM4OTc3LCAiQ1ZYIjogMC4yNDQyNTIzMTQxMDMyMzU3LCAiQUJCViI6IDAuMTk4Mzg2MTI4Nzc5NTcyNSwgIldNVCI6IDAuMTU1Mjg2MDI4ODQ2OTMxNzcsICJQRVAiOiAwLjE1MTE0NzI4MzUxMDg2NjQsICJLTyI6IDAuMTQxOTI1MjE3OTc0MDMzMTgsICJDU0NPIjogMC4xOTc5ODI0NDkzNTI1NTk0MywgIkNSTSI6IDAuMzQzNjEzNzk5MTgwNzUyOTcsICJBQ04iOiAwLjI2MzIyOTE3NzcxMzgxMzE2LCAiTkZMWCI6IDAuNDIyNTg1NDIwODM0MzQxMzYsICJNQ0QiOiAwLjEzOTczNTQwNzAwNTU0NTcsICJMSU4iOiAwLjIwMjgzMzk4NDQxMTQxMjU3LCAiQU1EIjogMC40OTM5NTA1MDA2NzUxNjQ2LCAiQkFDIjogMC4yNjIzODI1OTU5Mzc4NjMwNiwgIk9SQ0wiOiAwLjI3NzIwNTIwODc1MDU1NDY1LCAiQ01DU0EiOiAwLjI1Mjc4NTQ4MjI2MDkyNTg0LCAiUEZFIjogMC4yMTc2ODkwODU4ODU3MjUzMywgIkFCVCI6IDAuMjExOTMyMzI3MDAzNzgxNTYsICJJTlRDIjogMC4zODg4MDQzMDQyOTQwOTQ0NiwgIkRJUyI6IDAuMzE3MjM5OTEwMDg4NzYxNCwgIlZaIjogMC4yNDE0MTAwMDc1NjYwMjIwMiwgIldGQyI6IDAuMjc4NzY0NjE0MjI2NDY3ODcsICJJTlRVIjogMC4zNDQ3NzIxMzkyNTk5OTcyLCAiQU1HTiI6IDAuMjExMTM1OTk4NjY1MzI5NDIsICJQTSI6IDAuMTc2NTEzMzAwNTU1MDk4NDIsICJRQ09NIjogMC4zNTk3ODQ3OTE0MTc0MTcxNSwgIkNPUCI6IDAuMzE0OTU4MTAyNjg5MDI4NCwgIklCTSI6IDAuMTc2OTc4Nzg1MTM2NTc4MDUsICJTUFkiOiAwLjE1NzAwNjg0MTM3NTMzMzIyLCAiUVFRIjogMC4yMTMxMzgxNTM1OTM0NzY3NH0sICJjIjogeyJBQVBMMjMxMjI5QzAwMTg1MDAwIjogeyJTIjogMTg4LjAxLCAiSyI6IDE4NS4wfSwgIkdPT0cyMzEyMjlDMDAxMzYwMDAiOiB7IlMiOiAxMzYuMzgsICJLIjogMTM2LjB9LCAiQU1aTjIzMTIyOUMwMDE0MzAwMCI6IHsiUyI6IDE0My4yLCAiSyI6IDE0My4wfSwgIk5WREEyMzEyMjlDMDA0ODUwMDAiOiB7IlMiOiA0ODguODgsICJLIjogNDg1LjB9LCAiVFNMQTIzMTIyOUMwMDI0MDAwMCI6IHsiUyI6IDI0Mi44NCwgIksiOiAyNDAuMH0sICJMTFkyMzEyMjlDMDA1ODUwMDAiOiB7IlMiOiA1ODguNTQsICJLIjogNTg1LjB9LCAiSlBNMjMxMjI5QzAwMTQ5MDAwIjogeyJTIjogMTQ5Ljc0LCAiSyI6IDE0OS4wfSwgIlhPTTIzMTIyOVAwMDEwNDAwMCI6IHsiUyI6IDEwMy42NiwgIksiOiAxMDQuMH0sICJBVkdPMjMxMjI5QzAwOTc1MDAwIjogeyJTIjogOTc1LjQsICJLIjogOTc1LjB9LCAiVjIzMTIyOUMwMDI0NTAwMCI6IHsiUyI6IDI0OC4xMSwgIksiOiAyNDUuMH0sICJKTkoyMzEyMjlDMDAxNDUwMDAiOiB7IlMiOiAxNDguOCwgIksiOiAxNDUuMH0sICJQRzIzMTIyOVAwMDE0NTAwMCI6IHsiUyI6IDE1MS40MiwgIksiOiAxNDUuMH0sICJNQTIzMTIyOVAwMDM5NTAwMCI6IHsiUyI6IDM5Ni44MywgIksiOiAzOTUuMH0sICJIRDIzMTIyOUMwMDMwNTAwMCI6IHsiUyI6IDMwOC4xOSwgIksiOiAzMDUuMH0sICJBREJFMjMxMjI5UDAwNTkwMDAwIjogeyJTIjogNTk1LjMxLCAiSyI6IDU5MC4wfSwgIk1SSzIzMTIyOVAwMDEwMjAwMCI6IHsiUyI6IDEwMS4zNSwgIksiOiAxMDIuMH0sICJDT1NUMjMxMjI5QzAwNTk1MDAwIjogeyJTIjogNTk2Ljc4LCAiSyI6IDU5NS4wfSwgIkNWWDIzMTIyOUMwMDE0NTAwMCI6IHsiUyI6IDE0NS41NiwgIksiOiAxNDUuMH0sICJBQkJWMjMxMjI5UDAwMTM4MDAwIjogeyJTIjogMTM3LjYsICJLIjogMTM4LjB9LCAiV01UMjMxMjI5QzAwMTY1MDAwIjogeyJTIjogMTY5Ljc4LCAiSyI6IDE2NS4wfSwgIlBFUDIzMTIyOUMwMDE2NTAwMCI6IHsiUyI6IDE2Ny4yNSwgIksiOiAxNjUuMH0sICJLTzIzMTIyOUMwMDA1NzAwMCI6IHsiUyI6IDU3LjIxLCAiSyI6IDU3LjB9LCAiQ1NDTzIzMTIyOUMwMDA1MzAwMCI6IHsiUyI6IDUzLjI4LCAiSyI6IDUzLjB9LCAiQ1JNMjMxMjI5UDAwMjIwMDAwIjogeyJTIjogMjE5LjQyLCAiSyI6IDIyMC4wfSwgIkFDTjIzMTIyOUMwMDMzNTAwMCI6IHsiUyI6IDMyNS41LCAiSyI6IDMzNS4wfSwgIk5GTFgyMzEyMjlDMDA0NjAwMDAiOiB7IlMiOiA0NjEuOTQsICJLIjogNDYwLjB9LCAiTUNEMjMxMjI5UDAwMjY1MDAwIjogeyJTIjogMjcwLjM5LCAiSyI6IDI2NS4wfSwgIkFNRDIzMTIyOVAwMDExOTAwMCI6IHsiUyI6IDExOC4wLCAiSyI6IDExOS4wfSwgIkJBQzIzMTIyOUMwMDAzMDAwMCI6IHsiUyI6IDI5LjYyLCAiSyI6IDMwLjB9LCAiT1JDTDIzMTIyOVAwMDExMTAwMCI6IHsiUyI6IDExNC4wNiwgIksiOiAxMTEuMH0sICJDTUNTQTIzMTIyOUMwMDA0MjAwMCI6IHsiUyI6IDQyLjUzLCAiSyI6IDQyLjB9LCAiUEZFMjMxMjI5QzAwMDMwMDAwIjogeyJTIjogMzAuMTksICJLIjogMzAuMH0sICJBQlQyMzEyMjlDMDAwOTgwMDAiOiB7IlMiOiA5OC4wLCAiSyI6IDk4LjB9LCAiSU5UQzIzMTIyOUMwMDA0MDAwMCI6IHsiUyI6IDQwLjYxLCAiSyI6IDQwLjB9LCAiRElTMjMxMjI5QzAwMDkzMDAwIjogeyJTIjogOTMuOTMsICJLIjogOTMuMH0sICJWWjIzMTIyOUMwMDAzNTAwMCI6IHsiUyI6IDM2LjAsICJLIjogMzUuMH0sICJXRkMyMzEyMjlDMDAwNDIwMDAiOiB7IlMiOiA0Mi44NCwgIksiOiA0Mi4wfSwgIkFNR04yMzEyMjlDMDAyNzAwMDAiOiB7IlMiOiAyNzMuMDMsICJLIjogMjcwLjB9LCAiUUNPTTIzMTIyOUMwMDEyODAwMCI6IHsiUyI6IDEyOC45MiwgIksiOiAxMjguMH0sICJDT1AyMzEyMjlQMDAxMTYwMDAiOiB7IlMiOiAxMTUuMDMsICJLIjogMTE2LjB9LCAiSUJNMjMxMjI5QzAwMTUyNTAwIjogeyJTIjogMTUyLjU4LCAiSyI6IDE1Mi41fSwgIlNQWTIzMTIyOUMwMDQ0OTAwMCI6IHsiUyI6IDQ0OS42OCwgIksiOiA0NDkuMH0sICJRUVEyMzEyMjlDMDAzNDkwMDAiOiB7IlMiOiAzODUuNjIsICJLIjogMzQ5LjB9fX0=
sum([round(premium(c, data.s, r=0.05, T=0.13778), 2) for c in data.c])

Analysis:
Base64 encoded string decodes to nested dicts data['c'] and data['s']
data['s'] is sigma / volatility
data['c']['S'] is stock price
data['c']['K'] is strike price (also in the contract name )

extract_contract allows you to:
    - evaluate the contract for the symbol to match with the sigma
    - determine whether it is a call or put

premium calculates the Black–Scholes based on Call or Put

total: 463.29

'''

from pprint import pprint
from scipy.stats import norm
import base64
import json
import numpy as np
import re

def extract_contract(contract):
    options_contract_pattern = re.compile(r'([A-Z]+)(\d{6})([CP])(\d{8})')
    match = options_contract_pattern.match(contract)

    if match:
        data = {
            'name': contract,
            'symbol': match.group(1),
            'expdate': match.group(2),
            'type': match.group(3),
            'strike_str': match.group(4),
            'strike': float(match.group(4).lstrip('0'))/1000
        }
        # pprint(data)
        return data

def premium(contract, K, S, sigma, r, T):
    # print (f"Contract: {contract}")
    N = norm.cdf
    match extract_contract(contract)['type']:
        case 'C':
            d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
            d2 = d1 - sigma * np.sqrt(T)
            return S * N(d1) - K * np.exp(-r*T)* N(d2)
        case 'P':
            d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
            d2 = d1 - sigma * np.sqrt(T)
            return K * np.exp(-r*T)*N(-d2) - S*N(-d1)
        case _:
            raise Exception(f"Unable to determine Put or Call. Contract not valid format {contract}")

class Premium:
    def __init__(self, S, K, T, r, sigma, q=0):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.q = q

    @staticmethod
    def N(x):
        return norm.cdf(x)

    @property
    def params(self):
        return {'S': self.S,
                'K': self.K,
                'T': self.T,
                'r':self.r,
                'q':self.q,
                'sigma':self.sigma,
                }

    def d1(self):
        return (np.log(self.S/self.K) + (self.r -self.q + self.sigma**2/2)*self.T) \
                                / (self.sigma*np.sqrt(self.T))

    def d2(self):
        return self.d1() - self.sigma*np.sqrt(self.T)

    def _call_value(self):
        return self.S*np.exp(-self.q*self.T)*self.N(self.d1()) - \
                    self.K*np.exp(-self.r*self.T) * self.N(self.d2())

    def _put_value(self):
        return self.K*np.exp(-self.r*self.T) * self.N(-self.d2()) -\
                self.S*np.exp(-self.q*self.T)*self.N(-self.d1())

    def price(self, type_ = 'C'):
        if type_ == 'C':
            return self._call_value()
        if type_ == 'P':
            return self._put_value()
        if type_ == 'B':
            return  {'call': self._call_value(), 'put': self._put_value()}
        else:
            raise ValueError('Unrecognized type')

if __name__ == '__main__':
    datab64 = "eyJzIjogeyJBQVBMIjogMC4yNTEzMzQyMjgyNzc5NTgzNywgIkdPT0ciOiAwLjMzMzQ0ODg2MjYwMDY5NjcsICJBTVpOIjogMC4zNzQwODEwOTg4Nzk4MTUyLCAiTlZEQSI6IDAuNTM4MDU1NTA1MTU3MTA2MiwgIlRTTEEiOiAwLjU5Nzg3OTcxNzcxNTMwNjEsICJMTFkiOiAwLjI3NjY4OTgzNjIwNDE4ODI0LCAiSlBNIjogMC4yMTc2OTk1ODA0ODg2OTkyMiwgIlhPTSI6IDAuMjYyMjk2MTMzMzUxNzYzMiwgIkFWR08iOiAwLjMyNzYyMDM5NTAwODc0MTQ2LCAiViI6IDAuMTg4NDk2MDM0NDY5ODMzNjIsICJKTkoiOiAwLjE2NDcwMTExMTkyMTc2NDY4LCAiUEciOiAwLjE1MDIwMjgzNDg2MTMzMTQzLCAiTUEiOiAwLjIwODU5MTc5MTUxNjIyODcsICJIRCI6IDAuMjM1MTYzMzg1NTE5OTkwNzgsICJBREJFIjogMC4zNDkxNjc1NzA2MzgxMDAzLCAiTVJLIjogMC4xOTMyODA0OTI1MzQyNTk5NywgIkNPU1QiOiAwLjIwMzk5MjQyMjMzODM4OTc3LCAiQ1ZYIjogMC4yNDQyNTIzMTQxMDMyMzU3LCAiQUJCViI6IDAuMTk4Mzg2MTI4Nzc5NTcyNSwgIldNVCI6IDAuMTU1Mjg2MDI4ODQ2OTMxNzcsICJQRVAiOiAwLjE1MTE0NzI4MzUxMDg2NjQsICJLTyI6IDAuMTQxOTI1MjE3OTc0MDMzMTgsICJDU0NPIjogMC4xOTc5ODI0NDkzNTI1NTk0MywgIkNSTSI6IDAuMzQzNjEzNzk5MTgwNzUyOTcsICJBQ04iOiAwLjI2MzIyOTE3NzcxMzgxMzE2LCAiTkZMWCI6IDAuNDIyNTg1NDIwODM0MzQxMzYsICJNQ0QiOiAwLjEzOTczNTQwNzAwNTU0NTcsICJMSU4iOiAwLjIwMjgzMzk4NDQxMTQxMjU3LCAiQU1EIjogMC40OTM5NTA1MDA2NzUxNjQ2LCAiQkFDIjogMC4yNjIzODI1OTU5Mzc4NjMwNiwgIk9SQ0wiOiAwLjI3NzIwNTIwODc1MDU1NDY1LCAiQ01DU0EiOiAwLjI1Mjc4NTQ4MjI2MDkyNTg0LCAiUEZFIjogMC4yMTc2ODkwODU4ODU3MjUzMywgIkFCVCI6IDAuMjExOTMyMzI3MDAzNzgxNTYsICJJTlRDIjogMC4zODg4MDQzMDQyOTQwOTQ0NiwgIkRJUyI6IDAuMzE3MjM5OTEwMDg4NzYxNCwgIlZaIjogMC4yNDE0MTAwMDc1NjYwMjIwMiwgIldGQyI6IDAuMjc4NzY0NjE0MjI2NDY3ODcsICJJTlRVIjogMC4zNDQ3NzIxMzkyNTk5OTcyLCAiQU1HTiI6IDAuMjExMTM1OTk4NjY1MzI5NDIsICJQTSI6IDAuMTc2NTEzMzAwNTU1MDk4NDIsICJRQ09NIjogMC4zNTk3ODQ3OTE0MTc0MTcxNSwgIkNPUCI6IDAuMzE0OTU4MTAyNjg5MDI4NCwgIklCTSI6IDAuMTc2OTc4Nzg1MTM2NTc4MDUsICJTUFkiOiAwLjE1NzAwNjg0MTM3NTMzMzIyLCAiUVFRIjogMC4yMTMxMzgxNTM1OTM0NzY3NH0sICJjIjogeyJBQVBMMjMxMjI5QzAwMTg1MDAwIjogeyJTIjogMTg4LjAxLCAiSyI6IDE4NS4wfSwgIkdPT0cyMzEyMjlDMDAxMzYwMDAiOiB7IlMiOiAxMzYuMzgsICJLIjogMTM2LjB9LCAiQU1aTjIzMTIyOUMwMDE0MzAwMCI6IHsiUyI6IDE0My4yLCAiSyI6IDE0My4wfSwgIk5WREEyMzEyMjlDMDA0ODUwMDAiOiB7IlMiOiA0ODguODgsICJLIjogNDg1LjB9LCAiVFNMQTIzMTIyOUMwMDI0MDAwMCI6IHsiUyI6IDI0Mi44NCwgIksiOiAyNDAuMH0sICJMTFkyMzEyMjlDMDA1ODUwMDAiOiB7IlMiOiA1ODguNTQsICJLIjogNTg1LjB9LCAiSlBNMjMxMjI5QzAwMTQ5MDAwIjogeyJTIjogMTQ5Ljc0LCAiSyI6IDE0OS4wfSwgIlhPTTIzMTIyOVAwMDEwNDAwMCI6IHsiUyI6IDEwMy42NiwgIksiOiAxMDQuMH0sICJBVkdPMjMxMjI5QzAwOTc1MDAwIjogeyJTIjogOTc1LjQsICJLIjogOTc1LjB9LCAiVjIzMTIyOUMwMDI0NTAwMCI6IHsiUyI6IDI0OC4xMSwgIksiOiAyNDUuMH0sICJKTkoyMzEyMjlDMDAxNDUwMDAiOiB7IlMiOiAxNDguOCwgIksiOiAxNDUuMH0sICJQRzIzMTIyOVAwMDE0NTAwMCI6IHsiUyI6IDE1MS40MiwgIksiOiAxNDUuMH0sICJNQTIzMTIyOVAwMDM5NTAwMCI6IHsiUyI6IDM5Ni44MywgIksiOiAzOTUuMH0sICJIRDIzMTIyOUMwMDMwNTAwMCI6IHsiUyI6IDMwOC4xOSwgIksiOiAzMDUuMH0sICJBREJFMjMxMjI5UDAwNTkwMDAwIjogeyJTIjogNTk1LjMxLCAiSyI6IDU5MC4wfSwgIk1SSzIzMTIyOVAwMDEwMjAwMCI6IHsiUyI6IDEwMS4zNSwgIksiOiAxMDIuMH0sICJDT1NUMjMxMjI5QzAwNTk1MDAwIjogeyJTIjogNTk2Ljc4LCAiSyI6IDU5NS4wfSwgIkNWWDIzMTIyOUMwMDE0NTAwMCI6IHsiUyI6IDE0NS41NiwgIksiOiAxNDUuMH0sICJBQkJWMjMxMjI5UDAwMTM4MDAwIjogeyJTIjogMTM3LjYsICJLIjogMTM4LjB9LCAiV01UMjMxMjI5QzAwMTY1MDAwIjogeyJTIjogMTY5Ljc4LCAiSyI6IDE2NS4wfSwgIlBFUDIzMTIyOUMwMDE2NTAwMCI6IHsiUyI6IDE2Ny4yNSwgIksiOiAxNjUuMH0sICJLTzIzMTIyOUMwMDA1NzAwMCI6IHsiUyI6IDU3LjIxLCAiSyI6IDU3LjB9LCAiQ1NDTzIzMTIyOUMwMDA1MzAwMCI6IHsiUyI6IDUzLjI4LCAiSyI6IDUzLjB9LCAiQ1JNMjMxMjI5UDAwMjIwMDAwIjogeyJTIjogMjE5LjQyLCAiSyI6IDIyMC4wfSwgIkFDTjIzMTIyOUMwMDMzNTAwMCI6IHsiUyI6IDMyNS41LCAiSyI6IDMzNS4wfSwgIk5GTFgyMzEyMjlDMDA0NjAwMDAiOiB7IlMiOiA0NjEuOTQsICJLIjogNDYwLjB9LCAiTUNEMjMxMjI5UDAwMjY1MDAwIjogeyJTIjogMjcwLjM5LCAiSyI6IDI2NS4wfSwgIkFNRDIzMTIyOVAwMDExOTAwMCI6IHsiUyI6IDExOC4wLCAiSyI6IDExOS4wfSwgIkJBQzIzMTIyOUMwMDAzMDAwMCI6IHsiUyI6IDI5LjYyLCAiSyI6IDMwLjB9LCAiT1JDTDIzMTIyOVAwMDExMTAwMCI6IHsiUyI6IDExNC4wNiwgIksiOiAxMTEuMH0sICJDTUNTQTIzMTIyOUMwMDA0MjAwMCI6IHsiUyI6IDQyLjUzLCAiSyI6IDQyLjB9LCAiUEZFMjMxMjI5QzAwMDMwMDAwIjogeyJTIjogMzAuMTksICJLIjogMzAuMH0sICJBQlQyMzEyMjlDMDAwOTgwMDAiOiB7IlMiOiA5OC4wLCAiSyI6IDk4LjB9LCAiSU5UQzIzMTIyOUMwMDA0MDAwMCI6IHsiUyI6IDQwLjYxLCAiSyI6IDQwLjB9LCAiRElTMjMxMjI5QzAwMDkzMDAwIjogeyJTIjogOTMuOTMsICJLIjogOTMuMH0sICJWWjIzMTIyOUMwMDAzNTAwMCI6IHsiUyI6IDM2LjAsICJLIjogMzUuMH0sICJXRkMyMzEyMjlDMDAwNDIwMDAiOiB7IlMiOiA0Mi44NCwgIksiOiA0Mi4wfSwgIkFNR04yMzEyMjlDMDAyNzAwMDAiOiB7IlMiOiAyNzMuMDMsICJLIjogMjcwLjB9LCAiUUNPTTIzMTIyOUMwMDEyODAwMCI6IHsiUyI6IDEyOC45MiwgIksiOiAxMjguMH0sICJDT1AyMzEyMjlQMDAxMTYwMDAiOiB7IlMiOiAxMTUuMDMsICJLIjogMTE2LjB9LCAiSUJNMjMxMjI5QzAwMTUyNTAwIjogeyJTIjogMTUyLjU4LCAiSyI6IDE1Mi41fSwgIlNQWTIzMTIyOUMwMDQ0OTAwMCI6IHsiUyI6IDQ0OS42OCwgIksiOiA0NDkuMH0sICJRUVEyMzEyMjlDMDAzNDkwMDAiOiB7IlMiOiAzODUuNjIsICJLIjogMzQ5LjB9fX0="
    data = json.loads(base64.b64decode(datab64))
    # pprint(data)

    # rounded = [round(Premium(K=v['K'], S=v['S'], sigma=data['s'][extract_contract(c)['symbol']], r=0.05, T=0.13778).price(extract_contract(c)['type']), 2) for c,v in data['c'].items()]
    rounded = [round(premium(contract=c, K=v['K'], S=v['S'], sigma=data['s'][extract_contract(c)['symbol']], r=0.05, T=0.13778), 2) for c,v in data['c'].items()]
    # pprint(rounded)
    total = sum(rounded)
    print(f'total: {total}')
