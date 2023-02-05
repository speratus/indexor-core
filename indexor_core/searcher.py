import requests
import aiohttp

from indexor_core.query import Query


def run_search(querystring, config):
    url = config.engine_url

    full_path = f"{url}/search{querystring}"

    results = requests.get(full_path)

    return results.json()


def search(terms, config):
    query = Query.build_query(terms)

    return run_search(query, config)


async def run_search_async(querystring, config):
    url = config.engine_url

    full_path = f"{url}/search{querystring}"

    async with aiohttp.ClientSession() as session:
        async with session.get(full_path) as response:
            return await response.json()


async def search_async(terms, config):
    query = Query.build_query(terms)

    return await run_search_async(query, config)
