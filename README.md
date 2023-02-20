# Indexor Core
This library provides the core searching functionality required by the Casper discord bot. At the moment, its features
are fairly minimal, but the majority of Casper's planned features will be added here.

Examples of which features will be supported by this library:
* Results caching
* Improved support for getting results from specific search engines
* User based customization options
* User-added search engines

## Installation
You can install `indexor_core` by running the following command:
```bash
pip install git+https://github.com/speratus/indexor-core.git#egg=indexor_core
```

## Usage
Here is a basic usage example:
```py
from indexor_core.config import Config
from indexor_core.searcher import search

search_xng_instance_url = 'https://example.com'

c = Config(engine_url=search_xng_instance_url)

results = search('hello world', c)

```