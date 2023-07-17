from widgets_actions import validate_input


# Test cases for validate_input function
def test_valid_inputs():
    """Test validate_input with valid inputs"""
    result, message = validate_input("x^2 + 3*x + 2", "1", "10")
    assert result is True
    assert message == ""


def test_invalid_input_function():
    """Test validate_input with invalid function input"""
    result, message = validate_input("some text", "1", "10")
    assert result is False
    assert "Invalid function" in message


def test_invalid_min_value():
    """Test validate_input with invalid min value input"""
    result, message = validate_input("x^2 + 3*x + 2", "abc", "10")
    assert result is False
    assert "Invalid min/max values" in message


def test_invalid_max_value():
    """Test validate_input with invalid max value input"""
    result, message = validate_input("x^2 + 3*x + 2", "5", "abc")
    assert result is False
    assert "Invalid min/max values" in message


def test_max_value_smaller_than_min_value():
    """Test validate_input with invalid max < min"""
    result, message = validate_input("x^2 + 3*x + 2", "10", "5")
    assert result is False
    assert "Max value should be greater than min value" in message
