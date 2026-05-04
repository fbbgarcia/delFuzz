import pytest
import delfuzz

print(delfuzz.score("Resurecion", "Resurección"))


def within_tolerance(score, expected):
    return abs(score - expected) <= 5


# interchangeable characters

def test_interchangeable_characters():
    assert within_tolerance(delfuzz.score("María Antonia", "Maria Antonia"), 99.00) 
    assert within_tolerance(delfuzz.score("Valerio", "Balerio"), 92.86)
    assert within_tolerance(delfuzz.score("Beatris", "Beatriz"), 92.86)
    assert within_tolerance(delfuzz.score("Vásquez", "Vasques"), 91.43)
    assert within_tolerance(delfuzz.score("Ygnacio", "Ignacio"), 92.86)
    assert within_tolerance(delfuzz.score("Gutierez", "Gutiérres"), 80.00)
    assert within_tolerance(delfuzz.score("Rafael", "Raphael"), 91.67)
    assert within_tolerance(delfuzz.score("Argüello", "Arguello"), 96.43)
    assert within_tolerance(delfuzz.score("Santyago", "Santiago"), 93.75)
    assert within_tolerance(delfuzz.score("Raÿmundo", "Raymundo"), 96.88)
    assert within_tolerance(delfuzz.score("Amesquita", "Amézquita"), 93.33)


# other spelling variations

def test_spelling_variations():
    assert within_tolerance(delfuzz.score("Francisco Javier", "Francisco Xavier"), 92.50)
    assert within_tolerance(delfuzz.score("Guillermo", "Guiyermo"), 87.50)
    assert within_tolerance(delfuzz.score("Cayetano", "Calletano"), 87.50)
    assert within_tolerance(delfuzz.score("Resurecion", "Resurección"), 89.90)
    assert within_tolerance(delfuzz.score("Juan Huilson", "Juan Wilson"), 89.29)
    assert within_tolerance(delfuzz.score("Maria Felipa Fernandez", "Maria Hernandez"), 87.96)
    assert within_tolerance(delfuzz.score("Concepción", "Concepsion"), 94.00)
    assert within_tolerance(delfuzz.score("Guadalupe", "Guadalup"), 88.89)
    assert within_tolerance(delfuzz.score("Anastacio Fihelis", "Anastacio Feliz"), 85.71)
    assert within_tolerance(delfuzz.score("Juan Chrisostomo", "Juan Crisostomo"), 95.00)
    assert within_tolerance(delfuzz.score("Refuxio", "Refugio"), 85.71)


# nicknames and English variants

def test_nicknames_and_english_variants():
    assert within_tolerance(delfuzz.score("Alejandro", "Alejo"), 85.00)
    assert within_tolerance(delfuzz.score("Alejandro", "Alexander"), 85.00)
    assert within_tolerance(delfuzz.score("Alejo", "Alexander"), 75.00)
    assert within_tolerance(delfuzz.score("Alejo", "Alexandro"), 73.89)
    assert within_tolerance(delfuzz.score("Alejandro", "Alexandro"), 88.89)
    assert within_tolerance(delfuzz.score("Alejandro Antonio", "Alejo Antonio"), 92.50)
    assert within_tolerance(delfuzz.score("Alejandro Antonio", "Alejo"), 80.00)
    assert within_tolerance(delfuzz.score("Alejandro Antonio", "Alexander Anthony"), 85.00)
    assert within_tolerance(delfuzz.score("Alejandro", "Alejo Feliciano"), 80.00)
    assert within_tolerance(delfuzz.score("Joaquin", "Joachín"), 81.90)
    assert within_tolerance(delfuzz.score("Mabel", "Maria Isabel"), 85.00)
    assert within_tolerance(delfuzz.score("Mabel", "Mary Isabelle"), 85.00)
    assert within_tolerance(delfuzz.score("Juampa", "Juan Pablo"), 85.00)
    assert within_tolerance(delfuzz.score("Juampa", "John Paul"), 85.00)


# prepositions and articles

def test_prepositions_and_articles():
    assert within_tolerance(delfuzz.score("María Gertrudis", "Maria Gertrudes de la Merced"), 87.30)
    assert within_tolerance(delfuzz.score("Maria de los Reyes", "Maria Reyes"), 91.67)
    assert within_tolerance(delfuzz.score("Maria del Carmen", "Maria Carmen"), 93.33)


# extra/missing tokens

def test_extra_missing_tokens():
    assert within_tolerance(delfuzz.score("María Antonia", "Maria"), 86.50)
    assert within_tolerance(delfuzz.score("María Antonia", "Antonia"), 92.50)
    assert within_tolerance(delfuzz.score("María Manuela Antonia", "Maria Antonia"), 91.00)
    assert within_tolerance(delfuzz.score("Alejandro Antonio", "Josef Alejandro Antonio"), 91.67)


# unlikely matches

def test_unlikely_matches():
    assert within_tolerance(delfuzz.score("María Antonia", "María Antonio"), 92.86)
    assert within_tolerance(delfuzz.score("María Manuela Antonia", "Maria Josefa Antonia"), 66.00)
    assert within_tolerance(delfuzz.score("María Manuela Antonia", "Juan José"), 30.00)
    assert within_tolerance(delfuzz.score("Alejandro Antonio", "Alejandro Feliciano"), 50.00)
    assert within_tolerance(delfuzz.score("Alejandro Antonio", "Cristobal Antonio"), 50.00)
    assert within_tolerance(delfuzz.score("Alejandro Antonio", "Juan Pablo"), 25.00)


# edge cases

def test_identical():
    assert delfuzz.score("Juan", "Juan") == 100.0
    assert delfuzz.score("María del Carmen", "María del Carmen") == 100.0
    assert delfuzz.score("Jose de Gracia", "Jose de Gracia") == 100.0


def test_empty_strings():
    with pytest.warns(UserWarning):
        result = delfuzz.score("", "")
    assert result == 100.0

    with pytest.warns(UserWarning):
        result = delfuzz.score("Juan", "")
    assert result == 0.0

    with pytest.warns(UserWarning):
        result = delfuzz.score("", "Juan")
    assert result == 0.0