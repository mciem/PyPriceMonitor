from src.console import Console
from src.stockx  import StockX
from src.utils   import *

from currency_converter import CurrencyConverter

cc = CurrencyConverter()
cn = Console()
st = StockX()

def find_mean_price(sku: str, size: str):
    search = st.searchProducts(sku)
    if not search["success"]:
        cn.log("ERR", "failed to search products", {
            "body": search["body"]
        })

    b_search = getBestResult(search["body"])
    cn.log("DBG", "got best search", {
        "urlKey": b_search
    })

    lastSales = st.getProductLastSales(b_search, amount=250)
    if not lastSales["success"]:
        cn.log("ERR", "failed to scrape last sales", {
            "body": lastSales["body"]
        })

    p_lastSales = parseLastSales(lastSales["body"])
    if not p_lastSales.get(size):
        cn.log("ERR", "no last sale in size found", {
            "size": size
        })

    return sum(p_lastSales[size]) / len(p_lastSales[size])

m = find_mean_price("FZ8319-300", "9.5")
print(m*1.2)