from test_helper import run_common_tests, failed, passed, import_task_file, get_answer_placeholders


def test_task_window():
    window = get_answer_placeholders()[0]
    if 'ändere diesen Wert' == window:
        failed('Du solltest die Variablen \'hello\' neu definieren.')
    else:
        passed()


def test_value():
    file = import_task_file()

    if file.greetings == 'hallo':
        failed('Du solltest der Variablen einen anderen Wert zuweisen')
    else:
        passed()


if __name__ == '__main__':
    test_task_window()
    run_common_tests('Du solltest die Variablen \'hello\' neu definieren.')
    test_value()
