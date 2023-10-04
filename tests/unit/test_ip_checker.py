from src.ip_checker import (ip_check)

import pytest

# Function to initialize setup
@pytest.fixture
def ip_test_config(request) -> tuple:
    print("Automatic test running...\nRunning setup method...")
    ip = ip_check("257.120.223.13")
    ip1 = ip_check("127.0.0.0")
    
    yield ip, ip1

    # Teardown code
    ip.delete_objects()
    ip1.delete_objects()

@pytest.fixture
def ip_test_config_using_addfinalizer(request) -> tuple:
    print("Automatic test running...\nRunning setup method...")
    ip = ip_check("257.120.223.13")
    ip1 = ip_check("127.0.0.0")

    # Function to clear the resources
    def clear_resource():
        print("Running the teardown code")
        ip.delete_objects()
        ip1.delete_objects()
    
    request.addfinalizer(clear_resource)

    return ip, ip1

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

# Function to run test with setup and teardown using addfinalizer
def test_ip_with_addfinalizer(ip_test_config_using_addfinalizer) -> None:

    ip, ip1 = ip_test_config_using_addfinalizer
    print("Testing the validity...")
    assert ip.validate_it() == "Invalid IP"
    assert ip1.validate_it() == "Valid IPv4"

    print("Testing the class...")
    assert ip.find_class() == "E"
    assert ip1.find_class() == "A"
    
    
 
        