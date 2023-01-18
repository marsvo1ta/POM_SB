

def cargo_category_dropdown(number: str) -> str: 
    return f'div#vs{number}__combobox'


def cargo_input_field(number: str) -> str:
    return f"input[aria-labelledby='vs{number}__combobox']"


def cargo_select_field(number: str) -> str:
    return f"li#vs{number}__option-0"

