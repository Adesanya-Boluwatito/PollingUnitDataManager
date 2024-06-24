# PollingUnitDataManager

PollingUnitDataManager is a collection of Flask applications designed to interact with a MySQL database for managing and displaying polling unit data. Each application within this repository serves a unique purpose, from fetching results to storing and displaying data. This project includes three main applications:

1. ****
2. **LocalGovernmentResultsAggregator**
3. **PollingUnitResultsStorer**

## Features

- Fetch results for specific polling units based on their IDs.
- Aggregate and display results by local government.
- Store polling unit results in a structured database format.

## Requirements

- Python 3.x
- Flask
- MySQL
- mysql-connector-python

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/PollingUnitDataManager.git
    cd PollingUnitDataManager
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the MySQL database**:
    - Ensure MySQL is installed and running on your local machine.
    - Create a database named `bincom_test`.
    - Update the `host`, `user`, `passwd`, and `database` fields in the `mydb` connection object within each application file as necessary.

5. **Run the desired application**:
    ```sh
    python app_name.py  # Replace 'app_name.py' with the specific application file you want to run
    ```

## Applications Overview

### 1. PollingUnitResultsFetcher

**Description**: This application fetches and displays results for specific polling units based on their IDs. It provides a simple web interface to input a polling unit ID and retrieve its corresponding results.

**File**: `polling_unit_results_fetcher.py`

#### Routes
- `/polling_unit`: Renders a form to input polling unit ID and displays the results.

#### Functions
- `get_polling_unit_results(polling_id)`: Fetches and returns the results for a specified polling unit ID.

### 2. LocalGovernmentResultsAggregator

**Description**: This application aggregates and displays the total results by local government. It sums the results of each polling unit within a local government and provides a web interface to view these results.

**File**: `local_government_results_aggregator.py`

#### Routes
- `/total_results`: Renders a form to select a local government and displays the total results.

#### Functions
- `sum_of_each_polling_unit_result()`: Fetches and sums the results for each polling unit.
- `name_of_each_lga()`: Fetches and returns the names of each local government.
- `local_government_data()`: Aggregates data by local government.
- `get_total_result_by_local_government(lga)`: Retrieves total results for a specified local government.
- `get_local_governments()`: Returns a list of local governments.

### 3. PollingUnitResultsStorer

**Description**: This application stores polling unit results in a structured format within the database. It provides a web interface to input and store results for different parties.

**File**: `polling_unit_results_storer.py`

#### Routes
- `/polling_unit_form`: Renders a form to input polling unit results.
- `/store_results`: Stores the submitted results in the database.

#### Functions
- `parties_names()`: Fetches and returns the names of all parties.
- `store_results()`: Stores the results in the database.

## Project Structure

- `polling_unit_results_fetcher.py`: Application for fetching polling unit results.
- `local_government_results_aggregator.py`: Application for aggregating and displaying local government results.
- `polling_unit_results_storer.py`: Application for storing polling unit results.
- `templates/`: Directory containing HTML templates for rendering web pages.
- `requirements.txt`: List of Python dependencies.

## Templates

### `templates/polling_unit_form.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Polling Unit Form</title>
</head>
<body>
    <h1>Enter Polling Unit ID</h1>
    <form action="/polling_unit" method="post">
        <label for="polling_id">Polling Unit ID:</label>
        <input type="text" id="polling_id" name="polling_id" required>
        <br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
