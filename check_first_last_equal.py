# Defining function to check if the first and last number are equal
def check_first_last_equal(input_list):
    # Check if the list is not empty
    if input_list:
        # Compare the first and last elements of the list
        return input_list[0] == input_list[-1]
    else:
        # If the list is empty, return False
        return False
# If the list is empty, return False
# Test cases


