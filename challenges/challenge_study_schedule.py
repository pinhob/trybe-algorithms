def study_schedule(permanence_period, target_time):
    if target_time is None or type(target_time) != int:
        return None

    active_students = 0

    for student_study_time in permanence_period:
        start_time = student_study_time[0]
        finish_time = student_study_time[1]

        if (
            type(student_study_time) != tuple
            or type(start_time) != int
            or type(finish_time) != int
        ):
            return None

        if start_time <= target_time <= finish_time:
            active_students += 1

    return active_students


if __name__ == "__main__":
    arr = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
    print(study_schedule(arr, 2))
