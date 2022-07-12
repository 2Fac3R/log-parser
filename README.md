# Log parser

This repository represents my implementation for the following code challenge:

== Overview ==
Create a log parser that can:
Read an access log file
Resolve Country and State from IP address (IE MaxMind GeoLite2 Free)
Translate useragent to device type (Mobile, Desktop, Tablet) and Browser (Safari, Chrome, etc)
Combine new Geo & Device fields with existing fields on access log file and output/export a CSV
The goal of this test is to showcase your ability to leverage existing libraries without writing an exhaustive amount of code. Reach out to us if you need additional direction.
Below is a sample access log you can use if you don't have one.
https://cti-developer-dropbox.s3.amazonaws.com/gobankingrates.com.access.log

== Requirements ==
Any libraries must be installed via a package manager
Must be run from the cli
Provide instructions on how to build and run
Must be written in either PHP, Python or NodeJS
Commit to Github/GitLab and provide link for ConsumerTrack Staff to Review

== Bonus ==
Do this all with Docker
Unit Test

# Usage
Clone this repository

```sh
git clone https://github.com/2Fac3R/log-parser.git
```

Create and start your virtual environment [venv](https://docs.python.org/3/library/venv.html)

```sh
python3 -m venv .venv
source .venv/bin/activate
```

Rename .env.example to .env and set your **ipgeolocation.io** API key

```python
API_KEY=<your-api-key>
```

Set files names (Or leave default) in main.py

Run the main.py script

```sh
python3 main.py
```

See results in output file.


# Tools
I am using the following resources

[IP Geolocation API](https://app.ipgeolocation.io/)
IP Geolocation API provides real-time and accurate geolocation, and security information for any IPv4 or IPv6 address and domain name along with the user-agent detail for the provided user-agent string. You can geolocate your online visitors and provide them the customized user-experience accordingly.

[httpagentparser](https://pypi.org/project/httpagentparser/)

Extracts OS Browser etc information from http user agent string



<u>You can find more details in the *requirements.txt* file.</u>



## TODO:
* Do this all with Docker
* Unit Test


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Any feedback is appreciated.