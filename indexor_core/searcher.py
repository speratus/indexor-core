import requests


def search(querystring, config):
    url = config.engine_url

    full_path = f"{url}/search{querystring}"

    results = requests.get(full_path)

    return results.json()
