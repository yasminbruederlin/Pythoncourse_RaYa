from test_helper import run_common_tests, failed, passed, import_task_file, get_answer_placeholders


def test_value():
    file = import_task_file()
    if hasattr(file, 'python') and file.python == 'Python':
        passed()
    else:
        failed('Überprüfe die Indizen die du in der Teilung benutzt hast.')


def test_monty_python():
    window = get_answer_placeholders()[0]
    if 'monty_python' in window:
        passed()
    else:
        failed('benutze die Stringteilung')


if __name__ == '__main__':
    run_common_tests()
    test_value()
    test_monty_python()
