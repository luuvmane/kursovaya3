from src.utils import get_data, filter_data, last_five_operations, get_data_format

def test_get_data():
    data = get_data()
    assert type(data) is list
    assert len(data) > 0

def test_filter_data():
    sample_data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 4, "state": "EXECUTED"},
        {"id": 5, "state": "CANCELED"},
    ]
    filtered_data = filter_data(sample_data)
    assert len(filtered_data) == 3
    assert all(operation["state"] == "EXECUTED" for operation in filtered_data)

def test_last_five_operations():
    sample_data = [
        {"id": 1, "date": "2022-01-01"},
        {"id": 2, "date": "2022-01-02"},
        {"id": 3, "date": "2022-01-03"},
        {"id": 4, "date": "2022-01-04"},
        {"id": 5, "date": "2022-01-05"},
        {"id": 6, "date": "2022-01-06"},
    ]
    last_five = last_five_operations(sample_data)
    assert len(last_five) == 5
    assert last_five[0]["id"] == 6

def test_get_data_format():
    sample_data = [
        {"id": 1, "date": "2022-01-01", "operationAmount": {"amount": "100", "currency": "USD"}, "from": "A", "to": "B", "description": "Transaction"},
        {"id": 2, "date": "2022-01-02", "operationAmount": {"amount": "200", "currency": "EUR"}, "from": "B", "to": "C", "description": "Transfer"},
    ]
    formatted_operations = get_data_format(sample_data)
    assert len(formatted_operations) == 2
    assert all(isinstance(operation, str) for operation in formatted_operations)
