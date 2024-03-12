import json


def parseProductInfo(data: dict):
    return data["data"]["product"]["description"]

def parseLastSales(data: dict):
    l_sales = {}

    sales = data["data"]["product"]["market"]["sales"]["edges"]
    for sale in sales:
        if not l_sales.get(sale["node"]["associatedVariant"]["traits"]["size"]):
            l_sales[sale["node"]["associatedVariant"]["traits"]["size"]] = []

        l_sales[sale["node"]["associatedVariant"]["traits"]["size"]].append(float(sale["node"]["amount"]))

    return l_sales


def getBestResult(data: dict):
    return data["Products"][0]["urlKey"]
