from test_helper import run_common_tests, failed, passed, import_task_file, get_answer_placeholders


def test_value():
    file = import_task_file()
    if not file.is_equal:
        passed()
    else:
        failed('benutze den == Operator')


def test_window():
    window = get_answer_placeholders()[0]
    if '==' in window:
        passed()
    else:
        failed('benutze den == Operator')


if __name__ == '__main__':
    run_common_tests('benutze den == Operator')

    test_value()
    test_window()
