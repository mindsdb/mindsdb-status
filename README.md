# Mindsdb Status

mindsdb-statuses hosts integration tests to ensure the daily availability and proper functioning of MindsDB Cloud and its various integrations, such as MySQL, PostgreSQL, Snowflake, ClickHouse, and MongoDB. The test results are published on the MindsDB status page: https://mindsdb.instatus.com/


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
* An active MindsDB Cloud account and InstaStatus API key

## Installation

    Clone the repository:

```
git clone https://github.com/ZoranPandovski/mindsdb-statuses.git
```

Navigate to the project directory:

```
cd mindsdb-statuses
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

Set the necessary environment variables (replace your_api_key with your MindsDB Cloud API key):

* On Windows:

```
set API_KEY=your_api_key
```
* On macOS and Linux:

```
export API_KEY=your_api_key
```

Run the tests:

```
python -m unittest
```

## License

mindsdb-statuses is licensed under the MIT License.
