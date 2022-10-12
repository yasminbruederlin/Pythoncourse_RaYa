from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_initial():
    window = get_answer_placeholders()[0]
    if window == 'füge hier einen Kommentar ein':
        failed('Du solltest die Datei bearbeiten')
    else:
        passed()


if __name__ == '__main__':
    run_common_tests('Gib deinen Namen ein')
    test_initial()
