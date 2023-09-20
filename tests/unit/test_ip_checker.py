from src.ip_checker import (ip_check)

import pytest

# Function to initialize setup
@pytest.fixture
def ip_test_config(request) -> tuple:
    print("Automatic test running...\nRunning setup method...")
    ip = ip_check("257.120.223.13")
    ip1 = ip_check("127.0.0.0")
    yield ip, ip1

# Function to test the validate_it function
def test_validity(ip_test_config) -> None:
    ip, ip1 = ip_test_config
    print("Running test_validity...")
    assert ip.validate_it() == "Invalid IP"
    assert ip1.validate_it() == "Valid IPv4"

# Function to test the find_class function
def test_find_class(ip_test_config) -> None:
    ip, ip1 = ip_test_config
    print("Running test_find_class...")
    assert ip.find_class() == "E"
    assert ip1.find_class() == "A"


# Function to run test with setup and teardown manually
def test_ip_manually(request) -> None:
    # Managing resources
    print("\nManual test running...\nRunning manual setup method...")
    ip = ip_check("200.10.223.13")
    ip1 = ip_check("127.0.1.0")

    print("Testing the validity...")
    assert ip.validate_it() == "Valid IPv4"
    assert ip1.validate_it() == "Valid IPv4"

    print("Testing the class...")
    assert ip.find_class() == "C"
    assert ip1.find_class() == "A"

    # Clearing the resources after
    print("\nRunning manual teardown method...")
    del ip, ip1

 
        