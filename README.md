### Purpose

[main.py](main.py) will make a web request to a data broker or NZX.

Then parse it using Python, get the table data, rows and cells. 

Lastly then print out the results on screen if in terminal. I've added to save this to csv.


----

### Usage

Basic (out to screen/terminal)

```
python3 main.py
```

Output to CSV. In this example data and timestamp the filename. Or you could just name it data.csv

```
python3 main.py >> ./data/$(date "+%H%M%S_timezone_%b_%d_%Y").csv
```

----

### Github Actions

What the [actions](.github/workflows/actions.yml) file does:

* Runs main.py and temp save this to /data/raw.csv.

* Sort the raw.csv file using [sort.py](sort.py) then output to [/data/data.csv](./data/data.csv)

* Remove raw.csv

* Runs on a cron schedule at times that are important to NZX/NZSE trading. 

* Times adjusted for Github actions using UTC. UTC is usually -12 or -13 hours behinds NZT (manually adjust for any Daylight Savings changes).
* More info in the comments of the actions file for timings.
* [NZX Trading Hours and Boards](https://www.nzx.com/services/nzx-trading/hours-boards)


----

### Status

[![main.py](https://github.com/SystemJargon/nzx_data/actions/workflows/actions_mkt_close.yml/badge.svg)](https://github.com/SystemJargon/nzx_data/actions/workflows/actions_mkt_close.yml)

[![main.py](https://github.com/SystemJargon/nzx_data/actions/workflows/actions_mkt_open.yml/badge.svg)](https://github.com/SystemJargon/nzx_data/actions/workflows/actions_mkt_open.yml)
