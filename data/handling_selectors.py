

def cargo_category_dropdown(number: int) -> str: 
    return f'div#vs{number}__combobox'


def cargo_input_field(number: int) -> str:
    return f"input[aria-labelledby='vs{number}__combobox']"


def cargo_select_field(number: int) -> str:
    return f"li#vs{number}__option-0"

