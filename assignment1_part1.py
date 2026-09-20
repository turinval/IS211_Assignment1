class ListDivideException(Exception):
    pass


def list_divide(numbers, divide=2):
    """
    Returns the number of elements in the numbers list that are divisible by divide.
    """
    return sum(1 for num in numbers if num % divide == 0)


def test_list_divide():
    """
    Tests list_divide with various inputs. Raises ListDivideException if any test fails.
    """
    if list_divide([1, 2, 3, 4, 5]) != 2:
        raise ListDivideException("Test 1 failed")
    
    if list_divide([2, 4, 6, 8, 10]) != 5:
        raise ListDivideException("Test 2 failed")
    
    if list_divide([30, 54, 63, 98, 100], divide=10) != 2:
        raise ListDivideException("Test 3 failed")
    
    if list_divide([]) != 0:
        raise ListDivideException("Test 4 failed")
    
    if list_divide([1, 2, 3, 4, 5], 1) != 5:
        raise ListDivideException("Test 5 failed")


if __name__ == "__main__":
    test_list_divide()

# 1. Check current repository status
git status

# 2. Stage assignment1_part1.py
git add assignment1_part1.py

# 3. Commit the file with a descriptive message
git commit -m "Add list_divide implementation and test suite for Assignment 1 Part 1"

# 4. Push the commit to your remote GitHub repository
git push origin main
