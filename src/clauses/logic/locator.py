"""Utility methods for use in the 'clauses' app."""

import itertools
import string
from dataclasses import InitVar, dataclass, field
from typing import Any, Final, Generator, Optional

from clauses.hints import IndexedChar
from clauses.logic.utils import sentence_matches_clause, strip_punctuation

WORD_CHARS: Final[str] = string.ascii_lowercase + string.digits


@dataclass
class ClauseLocator:
    """Stores and locates clauses within relevant context."""

    clause_str: InitVar[str]
    context_str: InitVar[str]

    clause: list["Word"] = field(default_factory=list)
    context: list["Word"] = field(default_factory=list)

    def __post_init__(self, clause_str: str, context_str: str) -> None:
        """Split the provided clause and context into Words."""
        self.clause.extend(Word.from_string(clause_str))
        self.context.extend(Word.from_string(context_str))

    def locate(self) -> Optional[tuple[int, int]]:
        """Locate the provided clause in the given context."""
        sentence: list[Word] = []
        sentences: list[list[Word]] = []

        for word, target in itertools.product(self.context, self.clause):
            if target == word:
                sentence.append(word)

                if not sentence_matches_clause(sentence, self.clause):
                    previous_match = sentence[:-1]

                    # Ensure the previous sentence was matching
                    # This method implements an LRU cache, so no compute is repeated.
                    if sentence_matches_clause(previous_match, self.clause):
                        sentences.append(previous_match)
                        sentence = [sentence[-1]]
                    else:
                        sentence.clear()

        if sentence:
            sentences.append(sentence)

        if not sentences:
            return None

        longest_match = max(sentences, key=len)
        first, last = longest_match[0], longest_match[-1]

        return first[0][0], last[-1][0]


@dataclass(frozen=True)
class Word:
    """Represents a collection of IndexedChars bounded by whitespace."""

    characters: tuple[IndexedChar, ...] = ()

    @classmethod
    def from_string(cls, string: str) -> Generator["Word", None, None]:
        """Given a string, yield all contained Words."""
        word: list[IndexedChar] = []

        for index, character in strip_punctuation(enumerate(string.lower())):
            if character not in WORD_CHARS and word:
                yield cls(tuple(word.copy()))
                word.clear()
                continue
            word.append((index, character))

        if word:
            yield cls(tuple(word))

    def __eq__(self, other: Any) -> bool:
        """Check that two words are equal."""
        if type(other) is not Word:
            return False

        for self_char, other_char in zip(self.characters, other.characters):
            if self_char[1] != other_char[1]:
                return False
        return True

    def __getitem__(self, index: Any) -> IndexedChar:
        """Slicing on this Word should apply to its characters."""
        index, character = self.characters[index]
        return (index, character)
