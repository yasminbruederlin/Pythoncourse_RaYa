from test_helper import run_common_tests, passed, failed, import_task_file, get_answer_placeholders


def test_value():
    file = import_task_file()
    if hasattr(file, 'contains') and file.contains:
        passed()
    else:
        failed('Benutze den ' in ' Operator für diesen Test.')


def test_window():
    window = get_answer_placeholders()[0]

    if ' in ' in window:
        passed()
    else:
        failed('Benutze den ' in ' Operator für diesen Test.')


def test_ice_cream():
    window = get_answer_placeholders()[0]

    if 'Eis' in window and 'ice_cream':
        passed()
    else:
        failed('prüfe auf Eis in Eiscreme')


if __name__ == '__main__':
    run_common_tests()

    test_value()
    test_window()
    test_ice_cream()
