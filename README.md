# Gerrit Stats

[![PyPI](https://img.shields.io/pypi/v/gerritstats.svg?color=brightgreen)](https://pypi.org/project/gerritstats/)
[![Travis](https://travis-ci.com/craftslab/gerritstats.svg?branch=master)](https://travis-ci.com/craftslab/gerritstats)
[![Coverage](https://coveralls.io/repos/github/craftslab/gerritstats/badge.svg?branch=master)](https://coveralls.io/github/craftslab/gerritstats?branch=master)
[![License](https://img.shields.io/github/license/craftslab/gerritstats.svg?color=brightgreen)](https://github.com/craftslab/gerritstats/blob/master/LICENSE)



*Gerrit Stats* is a tool used for Gerrit stats via Gerrit API.



## Requirement

- python (3.7+)
- pip
- python-dev



## Installation

On Ubuntu / Mint, install *Gerrit Stats* with the following commands:

```bash
apt update
apt install python3-dev python3-pip python3-setuptools
pip install gerritstats
```

On OS X, install *Gerrit Stats* via [Homebrew](https://brew.sh/) (or via [Linuxbrew](https://linuxbrew.sh/) on Linux):

```
TBD
```

On Windows, install *Gerrit Stats* with the following commands:

```
pip install -U pywin32
pip install -U pyinstaller
pip install -Ur requirements.txt

pyinstaller --clean --name gerritstats -F stats.py
```



## Updating

```bash
pip install gerritstats --upgrade
```



## Running

```bash
gerritstats \
    --config-file config.json \
    --gerrit-query "since:2020-06-01 until:2020-06-02" \
    --output-file output.json
```



## Setting

*Gerrit Stats* parameters can be set in the directory [config](https://github.com/craftslab/gerritstats/blob/master/gerritstats/config).

An example of configuration in [config.json](https://github.com/craftslab/gerritstats/blob/master/gerritstats/config/config.json):

```
{
  "gerrit": {
    "host": "localhost",
    "pass": "pass",
    "port": 80,
    "query": {
      "option": ["CURRENT_REVISION"]
    },
    "user": "user"
  }
}
```



## License

Project License can be found [here](https://github.com/craftslab/gerritstats/blob/master/LICENSE).
