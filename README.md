# Gerrit Stats

[![PyPI](https://img.shields.io/pypi/v/gerritstats.svg?color=brightgreen)](https://pypi.org/project/gerritstats/)
[![Travis](https://travis-ci.com/craftslab/gerritstats.svg?branch=master)](https://travis-ci.com/craftslab/gerritstats)
[![Coverage](https://coveralls.io/repos/github/craftslab/gerritstats/badge.svg?branch=master)](https://coveralls.io/github/craftslab/gerritstats?branch=master)
[![License](https://img.shields.io/github/license/craftslab/gerritstats.svg?color=brightgreen)](https://github.com/craftslab/gerritstats/blob/master/LICENSE)



*Gerrit Stats* is a tool used for Gerrit stats via Gerrit API.



## Requirement

- python >= 3.7



## Build

```
pip install -U pywin32
pip install -U pyinstaller
pip install -Ur requirements.txt

pyinstaller --clean --name gerritstats -F stats.py
```



## Installation

```bash
pip install gerritstats
```



## Update

```bash
pip install gerritstats --upgrade
```



## Run

```bash
gerritstats --config-file config.json --gerrit-query "since:2020-06-01 until:2020-06-02" --output-file output.json
```



## Settings

*Gerrit Stats* parameters can be set in the directory [config](https://github.com/craftslab/gerritstats/blob/master/gerritstats/config).

An example of configuration in [config.json](https://github.com/craftslab/gerritstats/blob/master/gerritstats/config/config.json):

```
{
  "gerrit": {
    "host": "localhost:80",
    "pass": "pass",
    "query": {
      "option": ["CURRENT_REVISION"]
    },
    "user": "user"
  }
}
```



## License

Project License can be found [here](https://github.com/craftslab/gerritstats/blob/master/LICENSE).
