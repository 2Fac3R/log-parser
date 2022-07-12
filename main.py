"""
Create a log parser that can:
Read an access log file
Resolve Country and State from IP address (IE MaxMind GeoLite2 Free)
Translate useragent to device type (Mobile, Desktop, Tablet) and Browser (Safari, Chrome, etc)
Combine new Geo & Device fields with existing fields on access log file and output/export a CSV.
"""

from utils.parser import do_stuff


def main():
    input_file_name = 'gobankingrates.com.access.log'
    output_file_name = 'output.csv'
    pattern = " - - |\" |\"|\""

    do_stuff(input_file_name, output_file_name, pattern)


if __name__ == "__main__":
    main()
