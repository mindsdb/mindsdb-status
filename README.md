# Mindsdb Status

mindsdb-status hosts integration tests to ensure the daily availability and proper functioning of MindsDB Cloud and its various integrations, such as MySQL, PostgreSQL, Snowflake, ClickHouse, and MongoDB. The test results are published on the MindsDB status page: https://mindsdb.instatus.com/


## Table of Contents

* [Getting Started](#getting-started)
    * Prerequisites
    * Installation
* [Running the Tests](#running-the-tests)
* [License](#license)

## Getting Started

These instructions will guide you through setting up the project and running the tests on your local machine.

### Prerequisites

* Python 3.7.x or higher
* An active [MindsDB Cloud account](https://cloud.mindsdb.com/) and [InstaStatus API key](https://instatus.com/help/api)

## Installation

Clone the repository:

```
git clone https://github.com/mindsdb/mindsdb-status.git
```

Navigate to the project directory:

```
cd mindsdb-status
```
Create a virtual environment (recommended):

```
python -m venv venv
```
Activate the virtual environment:

* On Windows:

```
venv\Scripts\activate
```

* On macOS and Linux:

```
source venv/bin/activate
```

Install the required dependencies:

```
pip install -r requirements.txt
```

## Running the Tests

Set the necessary environment variables:

* On Windows:

```
set MINDSDB_CLOUD_USER=
set MINDSDB_CLOUD_PASS=
set INSTA_API_KEY=
set INSTA_API_BASE_URL=
```

* On macOS and Linux:

```
export MINDSDB_CLOUD_USER=
export MINDSDB_CLOUD_PASS=
export INSTA_API_KEY=
export INSTA_API_BASE_URL=
```

Run the tests:

```
python -m unittest
```

or to run specific set of tests e.g for connectors:

```
python -m unittest discover connectors/
```

## License

mindsdb-status is licensed under the MIT License.
