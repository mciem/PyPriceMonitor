from tls_client import Session


def buildClient(proxy: str = "") -> None:
    headers = {
        "accept": "application/json",
        "accept-language": "en-US",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="120", "Chromium";v="120"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }

    session = Session(random_tls_extension_order=True, client_identifier='chrome_120')
    session.proxies = f"http://{proxy}" if proxy else None
    session.headers = headers

    return session
