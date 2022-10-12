from test_helper import run_common_tests, passed, failed, import_task_file, get_answer_placeholders


def test_value():
    file = import_task_file()
    if hasattr(file, 'hello_world') and file.hello_world == 'HalloWelt':
        failed('Benutze einen Leerzeichen String ' ' in der Konkatonation.')
    else:
        passed()


def test_value_2():
    file = import_task_file()
    if hasattr(file, 'hello_world') and file.hello_world == 'Hallo Welt':
        passed()
    else:
        failed('benutze den + Operator')


def test_concat_used():
    window = get_answer_placeholders()[0]
    if 'hello' in window and 'world' in window and '+' in window:
        passed()
    else:
        failed('Verwende die zuvor definierte Variablen und Stringverkettung (+), um Variablen zu kombinieren')


if __name__ == '__main__':
    run_common_tests()
    test_value()
    test_value_2()
    test_concat_used()
