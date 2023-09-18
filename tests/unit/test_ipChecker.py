from src.ipChecker import (IpCheck)

import pytest

ip = None
ip1 = None

# Function to initialize setup
def setup_module(module):
    print("\nRunning setup method...")
    global ip, ip1
    ip = IpCheck("257.120.223.13")
    ip1 = IpCheck("127.12.0.13")

# Clearing the resources after 
def teardown_module(module):
    print("Running teardown method...")
    global ip, ip1
    del ip1, ip

# Function to test the Validate_it function
def test_validity():
    print("Running test_validity...")
    assert ip.Validate_It() == "Invalid IP"
    assert ip1.Validate_It() == "Valid IPv4"

# Function to test the findClass function
def test_findClass():
    print("Running test_findClass...")
    assert ip.findClass() == "E"
    assert ip1.findClass() == "A"
        