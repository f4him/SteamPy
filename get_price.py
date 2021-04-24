
import SteamMarket 
import requests
import json
 
 
def main():
    get_curr_price("prisma 2 case")

def get_curr_price(name):
    hash_name=SteamMarket.get_hash_name(730 , name)
    base = "https://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name="
    url=base+hash_name
    r =requests.get(url)
    y = json.loads(r.text)
    return float(y["lowest_price"][1:])
    









if __name__ == "__main__":
    main()