from dexscreener import DexscreenerClient

client = DexscreenerClient()

pair = client.get_token_pair("harmony", "0xcd818813f038a4d1a27c84d24d74bbc21551fa83")

pairs = client.get_token_pairs("0x2170Ed0880ac9A755fd29B2688956BD959F933F8")

search = client.search_pairs("WBTC")
