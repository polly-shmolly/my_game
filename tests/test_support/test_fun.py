from code.support import save_high_score


def test_save_high_score():
    """:return data"""
    t_save_data = save_high_score('polly', 5, path_f='code/high_score.txt')
    expected = 'polly 5'
    assert t_save_data == expected


