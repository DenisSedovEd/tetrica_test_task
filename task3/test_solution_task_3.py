import pytest

from typing import List, Dict
from solution import *


@pytest.mark.parametrize("case", tests)
def test_appearance(case):
    assert appearance(case["intervals"]) == case["answer"]


def test_merge_intervals_basic():
    assert merge_intervals([1, 3, 2, 4, 5, 7]) == [[1, 4], [5, 7]]


def test_merge_intervals_overlap():
    assert merge_intervals([1, 5, 2, 6, 7, 8]) == [[1, 6], [7, 8]]


def test_merge_intervals_unsorted():
    assert merge_intervals([5, 7, 1, 3, 2, 4]) == [[1, 4], [5, 7]]


def test_valid_interval_to_lesson():
    assert valid_interval_to_lesson([[1, 10], [20, 30]], [5, 25]) == [[5, 10], [20, 25]]


def test_intersect_intervals():
    a = [[1, 5], [10, 15]]
    b = [[3, 7], [12, 18]]
    assert intersect_intervals(a, b) == [[3, 5], [12, 15]]


def test_appearance_no_overlap():
    intervals = {
        "lesson": [100, 200],
        "pupil": [50, 90, 210, 300],
        "tutor": [60, 80, 220, 240],
    }
    assert appearance(intervals) == 0


def test_appearance_full_overlap():
    intervals = {
        "lesson": [100, 200],
        "pupil": [100, 200],
        "tutor": [100, 200],
    }
    assert appearance(intervals) == 100
