This repo contains the sample code for the article **A comprehensive guide on Pytest Setup Teardown**

## Code
The source code is a simple Python script that finds the code of a weekday and can be found at `src/ip_checker.py`. 

Unit Tests can be found at `tests/unit/test_ip_checker.py`

## Requirements
* Python (3.8+)

Please create a virtual environment and activate it.

Install the dependencies via the `requirements.txt` file using 

```commandline
pip install -r requirements.txt
```
If you don't have Pip installed please follow instructions online on how to do it.

## How To Run the Tests

You can run the test by using the command below,
```cmd
pytest
```

For more detailed result,

```cmd
pytest -s
```