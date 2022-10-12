from test_helper import run_common_tests, failed, get_answer_placeholders, passed


def test_window():
    window = get_answer_placeholders()[0]
    if 'fun' in window:
        passed()
    else:
        failed('Bennene deine Funktion \'fun\'')


def test_window1():
    window = get_answer_placeholders()[0]
    if 'def ' in window:
        passed()
    else:
        failed('Benutze \'def\' um eine Funktion zu erstellen')


def test_column():
    window = get_answer_placeholders()[0]
    if ':' in window:
        passed()
    else:
        failed('Vergiss den Doppeltpunkt am Eder der Zeile nicht')


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_column()
    test_window1()
