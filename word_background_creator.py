import random

def generate_repeating_text(terms, target_word_count, separator="•", min_distance=3):
    """
    Generates a string of randomly ordered terms with a minimum distance
    constraint between identical terms.

    Args:
        terms (list): A list of strings (the terms to repeat).
        target_word_count (int): The desired number of terms in the output string.
        separator (str): The string to place between terms. Defaults to "•".
        min_distance (int): The minimum number of other terms that must appear
                           between two occurrences of the same term.
                           Must be less than the number of unique terms.
                           Defaults to 3.

    Returns:
        str: A string containing the randomly ordered terms joined by the
             separator, approximately matching the target word count,
             or None if the constraints cannot be met.
    """
    num_unique_terms = len(terms)
    if min_distance >= num_unique_terms:
        print(f"Error: min_distance ({min_distance}) must be less than the number "
              f"of unique terms ({num_unique_terms}). Cannot guarantee constraint.")
        return None

    result_terms = []
    recent_terms = []

    if not terms:
        return ""

    while len(result_terms) < target_word_count:
        possible_choices = [term for term in terms if term not in recent_terms]

        if not possible_choices:
             print("Warning: Could not find a valid term respecting the distance constraint. "
                   "Picking a random term.")
             chosen_term = random.choice(terms)
        else:
            chosen_term = random.choice(possible_choices)

        result_terms.append(chosen_term)

        recent_terms.append(chosen_term)
        recent_terms = recent_terms[-min_distance:]

    return separator.join(result_terms)

term_list = []


word_count = 500
separator_symbol = "•"
minimum_separation = 3

playerInput = input("Enter terms that you would like for your background.  Type 'done' when ready to output your background text: ")

while playerInput.lower() != "done":
    term_list.append(playerInput.upper())
    playerInput = input("Enter terms that you would like for your background.  Type 'done' when ready to output your background text: ")

background_text = generate_repeating_text(
    terms=term_list,
    target_word_count=word_count,
    separator=separator_symbol,
    min_distance=minimum_separation
)

if background_text:
    print(f"Generated text ({len(background_text.split(separator_symbol))} words):\n")
    print(background_text)
else:
    print("Could not generate text due to parameter constraints.")