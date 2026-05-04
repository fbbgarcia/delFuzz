# delFuzz

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

## Overview

delFuzz is a tool for fuzzy matching Spanish names. It uses modified character and token-level Levenshtein Distance algorithms to compute a normalized similarity score between two names (0-100). Custom character-level edit costs account for Spanish spelling conventions such as interchangeable letters and the use of diacritics. Custom token-level costs account for name usage conventions such as nicknames and the inclusion of Spanish prepositions and articles. 

## Requirements

- Python 3.9 or higher

## Installation
```bash
pip install delfuzz
```

## Usage

### Examples

```python
import delfuzz

# example with diacritic
>>> delfuzz.score("María del Carmen", "Maria del Carmen")
99.33

# example with diacritic and missing "del"
>>> delfuzz.score("María del Carmen", "Maria Carmen")
92.67

# example with nickname
>>> delfuzz.score("María del Carmen", "Maricarmen")
85.0

# example with English variant
>>> delfuzz.score("María del Carmen", "Mary del Carmen")
95.0
```

### Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| name1 | str |  | First name to be compared. |
| name2 | str |  | Second name to be compared. |
| char_cost_dict | dict | [CHAR_COSTS](https://github.com/fbbgarcia/delfuzz/blob/main/src/delfuzz/defaults.py) | Dictionary of custom character-level costs. |
| token_cost_dict | dict | [TOKEN_COSTS](https://github.com/fbbgarcia/delfuzz/blob/main/src/delfuzz/defaults.py) | Dictionary of custom token-level costs. |
| placeholders | list[tuple[str, str]] | [MULTIGRAPH_PLACEHOLDERS](https://github.com/fbbgarcia/delfuzz/blob/main/src/delfuzz/defaults.py) | List of multigraph-to-placeholder mappings used to treat common Spanish multigraphs as their own singular characters. |
| sim_threshold | float | 70.0 | Minimum similarity (0-100) required to soft match a token/token span to a key in token_cost_dict. Allows the algorithm to tolerate minor spelling variations and errors. |
| max_char_span_len | int | 2 | Maximum length of character spans to consider. Allows the algorithm to support edit operations on spans of characters (e.g. multigraphs). |
| max_token_span_len | int | 3 | Maximum length of token spans to consider. Allows the algorithm to support edit operations on spans of tokens. |

### Custom Cost Dictionaries

`score` accepts custom cost dictionaries, allowing you to modify or replace the defaults ([CHAR_COSTS](https://github.com/fbbgarcia/delfuzz/blob/main/src/delfuzz/defaults.py) and/or [TOKEN_COSTS](https://github.com/fbbgarcia/delfuzz/blob/main/src/delfuzz/defaults.py)).

The easiest way to manage cost dictionaries is with the built-in `CharCostDictionary` and `TokenCostDictionary` classes:

```python
import delfuzz

# start from defaults
char_costs = delfuzz.CharCostDictionary()
token_costs = delfuzz.TokenCostDictionary()

# or start empty
char_costs = delfuzz.CharCostDictionary(empty=True)
token_costs = delfuzz.TokenCostDictionary(empty=True)
```

Both classes provide the same methods for adding, editing, removing, and displaying costs:

```python
# add a new substitution cost
token_costs.add_sub_cost("Jose", "Joseph", 0.15)

# edit an existing substitution cost
token_costs.edit_sub_cost("José", "Joseph", 0.10)

# remove a substitution cost
token_costs.remove_sub_cost("José", "Joseph")

# adding, editing, and removing insertion and deletion costs work the same way
token_costs.add_ins_cost("de la", 0.20)
token_costs.edit_ins_cost("la", 0.15)
token_costs.remove_ins_cost("la")

# display costs as a table
token_costs.show_sub_costs()
token_costs.show_ins_costs()
token_costs.show_del_costs()

# display substitution costs filtered to only costs involving 
# a given char/char span or token/token span
token_costs.show_sub_costs("s")

```

Pass your custom dictionary to `score`:

```python
delfuzz.score("Felipe de la Cruz", "Philip de la Cruz", token_cost_dict=token_costs)
```

#### Notes

1. All inputs are automatically lowercased.

2. Multi-character and multi-token spans are supported and treated as single units during similarity calculations. For example, `"ph"` in a `CharCostDictionary` or `"Juan Pablo"` in a `TokenCostDictionary`.

3. Substitution costs are bidirectional by default. Pass `bidirectional=False` to add a one-way mapping.

4. If you add costs for edit operations on spans longer than the default span length, make sure to pass the appropriate `max_char_span_len` or `max_token_span_len` argument to match the longest span in your cost dictionary. The defaults are 2 for character spans and 3 for token spans — any costs defined on longer spans will not be found during lookup otherwise.

## Comparison

General-purpose fuzzy or string matching libraries like RapidFuzz treat names as plain strings. Without context of Spanish spelling or name usage conventions, they tend to underestimate the similarity between Spanish names.

For example, here's how delFuzz's scores compare to RapidFuzz's ratio scores:

| Name 1 | Name 2 | delFuzz | RapidFuzz Ratio |
| --- | --- | --- | --- |
| María del Carmen | Maria del Carmen | 99.33 | 93.75 |
| María del Carmen | Maria Carmen | 92.67 | 78.57 |
| María del Carmen | Maricarmen | 85.00 | 61.54 |
| María del Carmen | Mary del Carmen | 95.00 | 90.32 |

RapidFuzz scores computed using `rapidfuzz.fuzz.ratio`.


## Acknowledgements

This algorithm was developed as part of a Data Science capstone project at California Polytechnic State University, San Luis Obispo, in contribution to the [African Californios](https://www.africancalifornios.org/) research project.

The capstone project was conducted in collaboration with African Californios project directors Dr. Cameron D. Jones, Lecturer in History, and Dr. Foaad Khosmood, Professor of Computer Science. Additional collaboration was provided by Jack T. Martin, a Visiting Scholar in History. It was advised by Dr. Alex Dekhtyar, Professor of Computer Science, and Dr. Kelly N. Bodwin, Associate Professor of Statistics.


## License

MIT License. See [LICENSE](LICENSE) for details.