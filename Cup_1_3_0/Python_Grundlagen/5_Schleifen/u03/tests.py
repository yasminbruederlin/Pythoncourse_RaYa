from test_helper import run_common_tests, passed, failed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "Tiger" in window and "animal" in window:
        passed()
    else:
        failed("benutze == zur Überprüfung ob animal gleich 'Elefant'")


if __name__ == '__main__':
    run_common_tests()
    test_window()