import json
import dspy


def read_examples_from_json(file_path, input_fields):
    """
    Reads examples from a JSON file.

    Parameters:
    - file_path: Path to the JSON file containing the examples. Defaults to 'examples.json'.

    Returns:
    A list of dictionaries, each representing an example.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

            # iterate over the examples and extract the input fields
            examples = []
            for example in data:
                example_dict = dspy.Example(**example).with_inputs(*input_fields)
                examples.append(example_dict)

            return examples
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"There was an error decoding the JSON file {file_path}.")
        return []


