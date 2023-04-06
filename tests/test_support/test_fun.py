from code.support import import_folder


def test_import_folder():
    """return list"""
    t_imp_folder = import_folder('graphics/character/idle')
    t_list = t_imp_folder._aslist()

    expected = ['1.png', '2.png', '3.png', '4.png', '5.png']

    assert t_list == expected


