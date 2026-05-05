import copy
import warnings
import pandas as pd

from .defaults import CHAR_COSTS, TOKEN_COSTS


def _to_dict(cost_dict: "CostDictionary | dict"):
    """
    Returns the raw dict representation of a cost dictionary.
    """
    if isinstance(cost_dict, CostDictionary):
        return cost_dict._costs
    return cost_dict


def _to_tuple(value: str, level: str):
    """
    Converts a string to a lowercase tuple unit.

    For character-level costs, each character becomes an element.
    For token-level costs, splits on whitespace.

    Args:
        value (str): The string to convert.
        level (str): "char" for character-level, "token" for token-level.

    Returns:
        tuple: The converted unit.
    """
    if level == "char":
        return tuple(value.lower())
    return tuple(value.lower().split())


class CostDictionary:
    """
    Base class for managing custom cost dictionaries.

    Provides methods for adding, removing, editing, and displaying
    substitution, insertion, and deletion costs.
    """

    def __init__(self, defaults: dict, empty: bool = False):
        if empty:
            self._costs = {"sub": {}, "ins": {}, "del": {}}
        else:
            self._costs = copy.deepcopy(defaults)


    # substitution

    def add_sub_cost(
        self,
        unit1: str,
        unit2: str,
        cost: float,
        bidirectional: bool = True,
    ):
        """
        Adds a substitution cost between two units if it doesn't already exist.
        Warns and does nothing if the pair already exists.

        Args:
            unit1 (str): First unit.
            unit2 (str): Second unit.
            cost (float): Substitution cost (0.0-1.0).
            bidirectional (bool): If True, adds the reverse mapping as well.
                Defaults to True.
        """
        u1 = _to_tuple(unit1, self._level)
        u2 = _to_tuple(unit2, self._level)
        if self._sub_cost_exists(u1, u2):
            warnings.warn(
                f"Substitution cost for {unit1!r} -> {unit2!r} already exists. "
                f"Use edit_sub_cost to update it.",
                UserWarning,
            )
            return
        self._set_sub_cost(u1, u2, cost)
        if bidirectional:
            if not self._sub_cost_exists(u2, u1):
                self._set_sub_cost(u2, u1, cost)

    def remove_sub_cost(
        self,
        unit1: str,
        unit2: str,
        bidirectional: bool = True,
    ):
        """
        Removes a substitution cost between two units if it exists.

        Args:
            unit1 (str): First unit.
            unit2 (str): Second unit.
            bidirectional (bool): If True, removes the reverse mapping as well.
                Defaults to True.
        """
        u1 = _to_tuple(unit1, self._level)
        u2 = _to_tuple(unit2, self._level)
        self._del_sub_cost(u1, u2)
        if bidirectional:
            self._del_sub_cost(u2, u1)

    def edit_sub_cost(
        self,
        unit1: str,
        unit2: str,
        cost: float,
        bidirectional: bool = True,
    ):
        """
        Updates the substitution cost between two units if it exists.
        Raises a KeyError if the pair does not exist.

        Args:
            unit1 (str): First unit.
            unit2 (str): Second unit.
            cost (float): New substitution cost (0.0-1.0).
            bidirectional (bool): If True, updates the reverse mapping as well.
                Defaults to True.
        """
        u1 = _to_tuple(unit1, self._level)
        u2 = _to_tuple(unit2, self._level)
        if not self._sub_cost_exists(u1, u2):
            raise KeyError(f"No substitution cost found for {unit1!r} -> {unit2!r}.")
        self._set_sub_cost(u1, u2, cost)
        if bidirectional:
            if not self._sub_cost_exists(u2, u1):
                raise KeyError(f"No substitution cost found for {unit2!r} -> {unit1!r}.")
            self._set_sub_cost(u2, u1, cost)


    # insertion

    def add_ins_cost(self, unit: str, cost: float):
        """
        Adds an insertion cost for a unit if it doesn't already exist.

        Args:
            unit (str): The unit.
            cost (float): Insertion cost (0.0-1.0).
        """
        u = _to_tuple(unit, self._level)
        if u in self._costs["ins"]:
            warnings.warn(
                f"Insertion cost for {unit!r} already exists. "
                f"Use edit_ins_cost to update it.",
                UserWarning,
            )
            return
        self._costs["ins"][u] = cost

    def remove_ins_cost(self, unit: str):
        """
        Removes an insertion cost for a unit if it exists.

        Args:
            unit (str): The unit.
        """
        u = _to_tuple(unit, self._level)
        self._costs["ins"].pop(u, None)

    def edit_ins_cost(self, unit: str, cost: float):
        """
        Updates the insertion cost for a unit if it exists.
        Raises a KeyError if the unit does not exist.

        Args:
            unit (str): The unit.
            cost (float): New insertion cost (0.0-1.0).
        """
        u = _to_tuple(unit, self._level)
        if u not in self._costs["ins"]:
            raise KeyError(f"No insertion cost found for {unit!r}.")
        self._costs["ins"][u] = cost


    # deletion

    def add_del_cost(self, unit: str, cost: float):
        """
        Adds a deletion cost for a unit if it doesn't already exist.

        Args:
            unit (str): The unit.
            cost (float): Deletion cost (0.0-1.0).
        """
        u = _to_tuple(unit, self._level)
        if u in self._costs["del"]:
            warnings.warn(
                f"Deletion cost for {unit!r} already exists. "
                f"Use edit_del_cost to update it.",
                UserWarning,
            )
            return
        self._costs["del"][u] = cost

    def remove_del_cost(self, unit: str):
        """
        Removes a deletion cost for a unit if it exists.

        Args:
            unit (str): The unit.
        """
        u = _to_tuple(unit, self._level)
        self._costs["del"].pop(u, None)

    def edit_del_cost(self, unit: str, cost: float):
        """
        Updates the deletion cost for a unit if it exists.
        Raises a KeyError if the unit does not exist.

        Args:
            unit (str): The unit.
            cost (float): New deletion cost (0.0-1.0).
        """
        u = _to_tuple(unit, self._level)
        if u not in self._costs["del"]:
            raise KeyError(f"No deletion cost found for {unit!r}.")
        self._costs["del"][u] = cost


    # display

    def show_sub_costs(self, unit: str = None):
        """
        Displays substitution costs as a table and returns a DataFrame.
        If unit is provided, only rows where that unit is involved are shown.

        Args:
            unit (str): Optional unit to filter by.

        Returns:
            pd.DataFrame: DataFrame of substitution costs.
        """
        col = "char" if self._level == "char" else "token"
        rows = []
        for key, values in self._costs["sub"].items():
            for target, cost in values:
                rows.append({
                    f"{col} 1": " ".join(key),
                    f"{col} 2": " ".join(target),
                    "cost": cost,
                })
        df = pd.DataFrame(rows, columns=[f"{col} 1", f"{col} 2", "cost"])
        if unit is not None:
            u = " ".join(_to_tuple(unit, self._level))
            df = df[(df[f"{col} 1"] == u) | (df[f"{col} 2"] == u)]
        print(df.to_string(index=False))
        return df

    def show_ins_costs(self):
        """
        Displays insertion costs as a table and returns a DataFrame.

        Returns:
            pd.DataFrame: DataFrame of insertion costs.
        """
        col = "char" if self._level == "char" else "token"
        rows = [{col: " ".join(key), "cost": cost} for key, cost in self._costs["ins"].items()]
        df = pd.DataFrame(rows, columns=[col, "cost"])
        print(df.to_string(index=False))
        return df

    def show_del_costs(self):
        """
        Displays deletion costs as a table and returns a DataFrame.

        Returns:
            pd.DataFrame: DataFrame of deletion costs.
        """
        col = "char" if self._level == "char" else "token"
        rows = [{col: " ".join(key), "cost": cost} for key, cost in self._costs["del"].items()]
        df = pd.DataFrame(rows, columns=[col, "cost"])
        print(df.to_string(index=False))
        return df


    # internal helpers

    def _set_sub_cost(self, unit1: tuple, unit2: tuple, cost: float):
        """Adds or updates a one-way substitution cost."""
        entries = self._costs["sub"].setdefault(unit1, [])
        for i, (target, _) in enumerate(entries):
            if target == unit2:
                entries[i] = (unit2, cost)
                return
        entries.append((unit2, cost))

    def _del_sub_cost(self, unit1: tuple, unit2: tuple):
        """Removes a one-way substitution cost. Silently does nothing if not found."""
        entries = self._costs["sub"].get(unit1)
        if entries is None:
            return
        self._costs["sub"][unit1] = [(t, c) for t, c in entries if t != unit2]
        if not self._costs["sub"][unit1]:
            del self._costs["sub"][unit1]

    def _sub_cost_exists(self, unit1: tuple, unit2: tuple):
        """Returns True if a one-way substitution cost exists."""
        entries = self._costs["sub"].get(unit1)
        if entries is None:
            return False
        return any(target == unit2 for target, _ in entries)


class CharCostDictionary(CostDictionary):
    """
    Cost dictionary for character-level edit operations.
    Defaults to CHAR_COSTS if not empty.

    Args:
        empty (bool): If True, starts with an empty cost dictionary.
            Defaults to False.
    """

    _level = "char"

    def __init__(self, empty: bool = False):
        super().__init__(defaults=CHAR_COSTS, empty=empty)


class TokenCostDictionary(CostDictionary):
    """
    Cost dictionary for token-level edit operations.
    Defaults to TOKEN_COSTS if not empty.

    Args:
        empty (bool): If True, starts with an empty cost dictionary.
            Defaults to False.
    """

    _level = "token"

    def __init__(self, empty: bool = False):
        super().__init__(defaults=TOKEN_COSTS, empty=empty)