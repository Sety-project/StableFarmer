import requests
import json
import pandas as pd

def get_swaps_query(pool_address, start_timestamp, first, skip):
  query = '''
  {
    swaps(
      first: %d
      skip: %d
      where: { pool: "%s", timestamp_gte: %d }
      orderBy: timestamp
      orderDirection: desc
    ) {
      timestamp
      tokenIn {
        symbol
      }
      tokenOut {
        symbol
      }
      amountIn
      amountOut
    }
  }
  ''' % (first, skip, pool_address, start_timestamp)
  return query

def get_liquidity_query(pool_address, start_timestamp, first, skip):
  query = '''
  {
    liquidityPoolHourlySnapshots(
      first: %d
      skip: %d
      where: { pool: "%s", timestamp_gte: %d }
      orderBy: timestamp
      orderDirection: desc
    ) {
      timestamp
      activeLiquidity
      tick
    }
  }
  ''' % (first, skip, pool_address, start_timestamp)
  return query

url = 'https://gateway-arbitrum.network.thegraph.com/api/dc503f11ca670638eb3ba20139dc400f/subgraphs/id/FQ6JYszEKApsBpAmiHesRsd9Ygc6mzmpNRANeVQFYoVX'
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
}

### Get swaps
data = {
  'query': get_swaps_query('0x7CF803e8d82A50504180f417B8bC7a493C0a0503', 1635724800, 1000, 0)
}
response = requests.post(url, headers=headers, json=data)
swaps = response.json()
with open('swaps.json', 'w') as f:
  json.dump(swaps, f)

### Get liquidity
data = {
  'query': get_liquidity_query('0x7CF803e8d82A50504180f417B8bC7a493C0a0503', 1635724800, 1000, 0)
}
response = requests.post(url, headers=headers, json=data)
liquidity = response.json()
with open('liquidity.json', 'w') as f2:
  json.dump(liquidity, f2)
