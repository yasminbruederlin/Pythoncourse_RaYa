from test_helper import test_is_not_empty, test_answer_placeholders_text_deleted, passed, failed, import_task_file


def test_is_identifier():
    try:
        import_task_file()
    except NameError:
        passed()
        return
    except SyntaxError:
        failed("Benutzung eines ungültigen Variablennamens")
        return
    failed("benutze eine undefinierte Variable")


if __name__ == '__main__':
    error_text = "du solltest den Variablennamen ändern"

    test_is_not_empty()
    test_answer_placeholders_text_deleted(error_text)
    test_is_identifier()
