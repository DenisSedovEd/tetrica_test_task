def merge_intervals(intervals):
    res = []
    pairs = [(intervals[i], intervals[i + 1]) for i in range(0, len(intervals), 2)]
    pairs.sort()

    for start, end in pairs:
        if not res or res[-1][1] < start:
            res.append([start, end])
        else:
            res[-1][1] = max(res[-1][1], end)
    return res


def valid_interval_to_lesson(interval, lesson):
    lesson_start, lesson_end = lesson
    valid_interval = []
    for start, end in interval:
        s = max(start, lesson_start)
        e = min(end, lesson_end)
        if s < e:
            valid_interval.append([s, e])
    return valid_interval


def intersect_intervals(interval_a, interval_b):
    result = []
    i = j = 0
    while i < len(interval_a) and j < len(interval_b):
        start = max(interval_a[i][0], interval_b[j][0])
        end = min(interval_a[i][1], interval_b[j][1])
        if start < end:
            result.append([start, end])
        if interval_a[i][1] < interval_b[j][1]:
            i += 1
        else:
            j += 1

    return result


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson = intervals["lesson"]
    pupil = intervals["pupil"]
    tutor = intervals["tutor"]

    valid_pupil_intervals = valid_interval_to_lesson(merge_intervals(pupil), lesson)
    valid_tutor_intervals = valid_interval_to_lesson(merge_intervals(tutor), lesson)

    intersect_interval = intersect_intervals(
        valid_pupil_intervals, valid_tutor_intervals
    )

    time_count = sum(end - start for start, end in intersect_interval)

    return time_count


tests = [
    {
        "intervals": {
            "lesson": [1594663200, 1594666800],
            "pupil": [
                1594663340,
                1594663389,
                1594663390,
                1594663395,
                1594663396,
                1594666472,
            ],
            "tutor": [1594663290, 1594663430, 1594663443, 1594666473],
        },
        "answer": 3117,
    },
    {
        "intervals": {
            "lesson": [1594702800, 1594706400],
            "pupil": [
                1594702789,
                1594704500,
                1594702807,
                1594704542,
                1594704512,
                1594704513,
                1594704564,
                1594705150,
                1594704581,
                1594704582,
                1594704734,
                1594705009,
                1594705095,
                1594705096,
                1594705106,
                1594706480,
                1594705158,
                1594705773,
                1594705849,
                1594706480,
                1594706500,
                1594706875,
                1594706502,
                1594706503,
                1594706524,
                1594706524,
                1594706579,
                1594706641,
            ],
            "tutor": [
                1594700035,
                1594700364,
                1594702749,
                1594705148,
                1594705149,
                1594706463,
            ],
        },
        "answer": 3577,
    },
    {
        "intervals": {
            "lesson": [1594692000, 1594695600],
            "pupil": [1594692033, 1594696347],
            "tutor": [1594692017, 1594692066, 1594692068, 1594696341],
        },
        "answer": 3565,
    },
]

if __name__ == "__main__":
    # appearance(tests)

    for i, test in enumerate(tests):
        test_answer = appearance(test["intervals"])
        print(test_answer)
        assert (
            test_answer == test["answer"]
        ), f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
