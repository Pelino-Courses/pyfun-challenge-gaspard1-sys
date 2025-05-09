def process_inputs(*args, **kwargs):
    """
    Processes positional and keyword arguments for the calculation.
    
    Args:
        *args: Numbers to be used in the calculation.
        **kwargs: Operations to apply. Supported operations:
                  - add (bool)
                  - subtract (bool)
                  - multiply (bool)
                  - divide (bool)

    Returns:
        tuple: (list of numbers, dictionary of operations)

    Raises:
        ValueError: If any positional argument is not a number.
        ValueError: If no valid operation is specified.
    """
    # Validate all positional arguments are numbers
    numbers = []
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise ValueError(f"Invalid number: {arg}")
        numbers.append(arg)

    # Validate at least one valid operation is requested
    valid_operations = {'add', 'subtract', 'multiply', 'divide'}
    operations = {op: kwargs.get(op, False) for op in valid_operations}
    if not any(operations.values()):
        raise ValueError("At least one valid operation (add, subtract, multiply, divide) must be True.")

    return numbers, operations

def calculate(*args, **kwargs):
    """
    Performs calculations on given numbers based on specified operations.
    
    Usage:
        calculate(1, 2, 3, add=True, multiply=True)

    Args:
        *args: Numbers to be calculated.
        **kwargs: Operations to apply (add, subtract, multiply, divide).

    Returns:
        dict: Result of each requested operation.

    Raises:
        ValueError: For invalid inputs or operations.
    """
    numbers, operations = process_inputs(*args, **kwargs)
    
    results = {}

    if operations['add']:
        results['add'] = sum(numbers)

    if operations['subtract']:
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        results['subtract'] = result

    if operations['multiply']:
        result = 1
        for num in numbers:
            result *= num
        results['multiply'] = result

    if operations['divide']:
        result = numbers[0]
        try:
            for num in numbers[1:]:
                result /= num
            results['divide'] = result
        except ZeroDivisionError:
            results['divide'] = 'Error (division by zero)'

    return results

# Example Usage
RESULT = calculate(10, 5, 6, add=True, multiply=True, Subtrac=True, divide=True)
print(RESULT)