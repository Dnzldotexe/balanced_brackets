""""
This code checks if a string has balanced brackets with Time Complexity of O(n/2)-ish
"""
def is_balanced(str_input: str) -> str:
    """
    This function checks if the string of brackets is balanced

    Returns:
        string of text YES / NO (str)
    """
    # Creating a dictionary for each bracket pairs
    brackets = {
        "(": ")",
        "[": "]",
        "{": "}",
    }

    # Creating a list with opening brackets
    opening = brackets.keys()

    # Calculating the middle and remainder of the input
    middle = len(str_input) // 2
    remainder = len(str_input) % 2

    # Returns no when string is odd
    if remainder:
        return "NO"

    # Getting the first and last half of the string
    first_half = str_input[:middle]
    last_half = str_input[middle:]

    # List for storing the replaced values
    replaced_brackets = []

    # For every item inside the first half
    for item in first_half:
        # When it's an opening bracket
        if item in opening:
            # Replace it with closing pair bracket
            replaced_brackets.append(brackets[f"{item}"])

    # When replaced list is equal to reversed last half list
    if replaced_brackets == list(last_half[::-1]):
        # Return yes
        return "YES"

    # Otherwise, return no
    return "NO"


def main() -> None:
    """
    This function contains the challenge edge cases
    """
    # Edge cases
    edge_cases = ["{[()]}", "{[(])}", "{{[[(())]]}}"]

    # For every case inside edge cases
    for case in edge_cases:
        # Storing the function's output
        output = is_balanced(case)

        # Printing the output
        print(output)


# Running the main function
if __name__ == "__main__":
    main()
