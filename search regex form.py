import re

# List of strings
s = ["i go to school", " he goes......to!--sfsdds i schi", " she went go djskjfd to fdsfd"]

# Function to convert the user input pattern to a regex pattern
def convert_to_regex(user_pattern):
    # Escape any special regex characters in the user pattern except *
    escaped_pattern = re.escape(user_pattern)
    # Replace escaped * with .*
    regex_pattern = escaped_pattern.replace(r'\*', '.*')
    return re.compile(regex_pattern)

# Function to search for the pattern in the list of strings
def find_pattern(strings, pattern):
    matches = []
    for string in strings:
        if pattern.search(string):
            matches.append(string)
    return matches

# User input pattern
while True:
    user_pattern=""
    user_pattern=input ()
    # *go*sf*gConvert the user input pattern to a regex pattern
    regex_pattern = convert_to_regex(user_pattern)

    # Search for the pattern in the list
    matches = find_pattern(s, regex_pattern)

    # Output the results
    print(matches)
