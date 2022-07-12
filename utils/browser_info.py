import httpagentparser


def get_browser_info_from_useragent(http_user_agent):
    """Extracts OS Browser information from http user agent string."""
    try:
        response = httpagentparser.detect(http_user_agent)
    except KeyError:
        """If useragent is a web spider."""
        return "Unknown"
    return response
