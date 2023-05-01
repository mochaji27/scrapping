from urllib.parse import urlparse
from urllib.parse import parse_qs


def get_url_parameter(url, param):
    parsed_url = urlparse(url)
    captured_value = parse_qs(parsed_url.query)[param][0]
    #print(captured_value)
    return captured_value

