from test_helper import run_common_tests, passed, failed, import_task_file, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if '[' in window and '1' in window and ']' in window:
        passed()
    else:
        failed('benutze die Indexierung')


def test_value():
    file = import_task_file()
    if hasattr(file, 'y_letter') and file.y_letter == 'y':
        passed()
    else:
        failed('String Index startet mit 0')


if __name__ == '__main__':
    run_common_tests()

    test_value()
    test_window()
