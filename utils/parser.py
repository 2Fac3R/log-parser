import re

from .ip import get_ip_geolocation
from .browser_info import get_browser_info_from_useragent


def do_stuff(input_file_name, output_file_name, pattern):
    """Combine new Geo & Device fields with existing fields on access log file and output a file."""
    with open(output_file_name, 'w') as output_file:
        with open(input_file_name) as input_file:
            logs_data = list(input_file)

            for row in logs_data:
                fields = re.split(pattern, row)
                ip = fields[0]
                # date = fields[1]
                # http_request = fields[2]
                # status_code = fields[3]
                # resource = fields[4]
                user_agent = fields[6]
                country_name = get_ip_geolocation(ip)['country_name']
                state_prov = get_ip_geolocation(ip)['state_prov']
                device_type = get_browser_info_from_useragent(user_agent)
                browser = get_browser_info_from_useragent(user_agent)
                geolocation = f"[{country_name}, {state_prov}]"
                device = f"[{device_type}, {browser}]"
                output_file.write(row.rstrip("\n") +
                                  f" {geolocation} {device}" + "\n")
