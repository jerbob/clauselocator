"""Utility methods for use in the 'clauses' app."""

from string import punctuation
from typing import Generator, Iterable

from clauses.hints import IndexedChar
from clauses.logic import locator


def strip_punctuation(
    string: Iterable[IndexedChar],
) -> Generator[IndexedChar, None, None]:
    """
    Return the provided string, stripped of any punctuation.

    This needs to be applied after strings are split and indexed,
    so we can retain the original indexes for each character.
    """
    for index, character in string:
        if character not in punctuation:
            yield (index, character)


def sentence_matches_clause(
    sentence: list["locator.Word"], clause: list["locator.Word"]
) -> bool:
    """Check if the provided list of Words matches a clause so far."""
    for sentence_word, clause_word in zip(sentence, clause):
        if sentence_word != clause_word:
            return False
    return bool(sentence) and True
