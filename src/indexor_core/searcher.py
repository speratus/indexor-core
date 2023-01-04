import requests

from src.indexor_core.query import Query


def run_search(querystring, config):
    url = config.engine_url

    full_path = f"{url}/search{querystring}"

    results = requests.get(full_path)

    return results.json()


def search(terms, config):
    query = Query.build_query(terms)

    return run_search(query, config)
