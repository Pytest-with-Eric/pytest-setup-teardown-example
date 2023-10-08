import pytest

def calculate_square(x):
    return x * x

@pytest.fixture
def setup_data(request):
    print("\nSetting up resources...")
    data = 5
    
    # Define a finalizer function for teardown
    def finalizer():
        print("\nPerforming teardown...")
        # Clean up any resources if needed

    # Register the finalizer to ensure cleanup
    request.addfinalizer(finalizer)

    return data  # Provide the data to the test

# Test cases
def test_square_positive_number(setup_data):
    result = calculate_square(setup_data)
    assert result == 25
    print("Running test case for positive number")

def test_square_negative_number(setup_data):
    print("Intentional error during setup")
    raise ValueError("Intentional error during setup")
    result = calculate_square(-setup_data)
    assert result == 25  # The square of -5 is also 25
    print("Running test case for negative number")
