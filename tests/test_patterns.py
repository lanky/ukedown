import re

import pytest

from ukedown import patterns


def pytest_generate_tests(metafunc: pytest.Metafunc):
    metafunc.parametrize(
        'case',
        getattr(metafunc.cls, metafunc.function.__name__.replace('test_', ''), []),
        scope='class'
    )


class Base:
    @property
    def pattern(self) -> re.Pattern:
        return re.compile(getattr(patterns, self.__class__.__name__.replace('Test', '').upper()))

    def test_matches(self, case: str):
        assert self.pattern.match(case)

    def test_failures(self, case: str):
        assert self.pattern.match(case) is None


class TestChord(Base):
    matches = [
        '(C)',
        '(C#)',
        '(Cb)',
        '(Dm)',
    ]
    failures = [
        '(H)',
    ]


class TestHyphens(Base):
    matches = [
        '-',
        '- ',
        ' -',
        '  -   ',
        '—',
    ]
    failures = [
        '_',
    ]


class TestVox(Base):
    matches = [
        '(I can mash potato)',
    ]
    failures = [
        '(I can (Bb)mash po(C)tato)',
        '(I can (mash) potato)',
    ]


class TestNotes(Base):
    matches = [
        '{repeat x2}',
        '{demented choir noises}',
    ]


class TestBox(Base):
    matches = [
        '| {repeat x2}',
        # New paragraph within box?
        '| |',
    ]
    failures = [
        # TODO: These should (probably) not fail?
        # https://github.com/birdcolour/ukulele-wednesdays/issues/24
        '| (D) (D) (D) (F) | (D) (D) (D) (F)',
        '| (C) (C) (A7sus4) (A7sus4) | (G) (G) (F) (F)',
        '| (D) (D) (D) (F) | (D) (D) (D) (F) |',
        '| (C) (C) (A7sus4) (A7sus4) | (G) (G) (F) (F) |',
        # https://github.com/birdcolour/ukulele-wednesdays/issues/25
        '|',
        '| ',
    ]


class TestHeader(Base):
    matches = [
        '[chorus]',
        '[bridge]',
    ]


class TestRepeats(Base):
    matches = [
        'x2',
    ]
    failures = [
        'x 3',
    ]
