from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_column():
    window = get_answer_placeholders()[0]
    if ':' in window:
        passed()
    else:
        failed('Vergiss den Doppelpunkt am Ende nicht.')


def test_window():
    window = get_answer_placeholders()[0]
    if 'while ' in window:
        passed()
    else:
        failed('Benutze einen while loop zum Iterieren.')


def test_window1():
    window = get_answer_placeholders()[0]
    if 'number' in window:
        passed()
    elif 'square' in window:
        passed()
    else:
        failed('Benutze die \'number\' Variable in der while Kondition')


def test_window2():
    window = get_answer_placeholders()[0]
    if '9' in window or '10' in window:
        if '<' in window or '<=>' in window:
            passed()
    elif 'square' in window:
        if '<' and '81' in window:
            passed()
    else:
        failed('Überprüfe, dass \'number\' in der Kondition kleiner als 10 ist.')


# def test_output():
#     output = get_file_output()
#     if 'fertig' not in output:
#         failed('Sorry, die Antwort ist falsch')
#         return
#     border = output.index('Feretig')
#     user_squares = output[border + 1:]
#     user_squares = [x for x in user_squares if x]
#     correct_answer = list(map(str, [x * x for x in range(1, 10)]))
#     if correct_answer == user_squares:
#         passed()
#     else:
#         failed('Sorry, die Antwort ist falsch')


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window1()
    test_window2()
    test_column()
    # test_output()
