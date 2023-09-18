from src.ip_checker import (ip_check)

import pytest

# Function to initialize setup
@pytest.fixture
def setup_module(request) -> tuple:
    print("\nRunning setup method...")
    ip = ip_check("257.120.223.13")
    ip1 = ip_check("127.0.0.0")
    yield ip, ip1
    
    # Clearing the resources after
    print("Running teardown method...")
    del ip1, ip

# Function to test the validate_it function
def test_validity(setup_module) -> None:
    ip, ip1 = setup_module
    print("Running test_validity...")
    assert ip.validate_it() == "Invalid IP"
    assert ip1.validate_it() == "Valid IPv4"

# Function to test the find_class function
def test_find_class(setup_module) -> None:
    ip, ip1 = setup_module
    print("Running test_find_class...")
    assert ip.find_class() == "E"
    assert ip1.find_class() == "A"

 
        