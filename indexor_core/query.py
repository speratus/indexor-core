import urllib.parse


class Query:

    @classmethod
    def build_query(cls, terms, user_preferences={}):
        sanitized_terms = urllib.parse.quote_plus(terms)

        return f"?q={sanitized_terms}&format=json"
