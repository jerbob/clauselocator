"""Utility methods for use in the 'clauses' app."""

from functools import lru_cache
from string import punctuation
from typing import Generator, Iterable

from clauses.hints import IndexedChar
from clauses.logic import locator


__all__ = ["strip_punctuation", "sentence_matches_clause"]


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


@lru_cache
def _sentence_matches_clause(
    sentence: tuple["locator.Word"], clause: tuple["locator.Word"]
) -> bool:
    """
    Check if the provided sentence matches a clause.

    Cached functions must take hashable inputs, so these must be tuples.
    """
    for sentence_word, clause_word in zip(sentence, clause):
        if sentence_word != clause_word:
            return False
    return bool(sentence) and True


def sentence_matches_clause(
    sentence: list["locator.Word"], clause: list["locator.Word"]
) -> bool:
    """
    A public function for checking if lists of words match relevant clauses.

    This function simply casts the provided input to tuples, and calls the lru_cached method.
    """
    return _sentence_matches_clause(tuple(sentence), tuple(clause))
