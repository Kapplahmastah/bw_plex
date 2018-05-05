import math
import pytest
from conftest import misc


def test_to_sec():

    assert misc.to_sec(1) == 1
    assert misc.to_sec('00:01') == 1

    assert misc.to_sec('10:59') == 659


def test_get_valid_filename():
    assert misc.get_valid_filename('M*A*S*H') == 'MASH'


@pytest.mark.xfail
def test_find_offset_ffmpeg(intro_file):
    x = misc.find_offset_ffmpeg(intro_file)
    assert x == 214
    # This failed it isnt really the intro file.
    #assert x == -1
    # failes as find_offset_ffmpeg selects the intro, not the end of the intro..


def test_download_theme_and_get_offset_end(mocker, media, HT, intro_file, tmpdir):
    # ooops, been to patch convert_and_trim

    #mocker.patch('bw_plex.misc.THEMES', return_value=str(tmpdir)) # <-- fix me download the the real location..
    files = misc.download_theme(media, HT, theme_source='youtube', url='https://www.youtube.com/watch?v=BIqBQWB7IUM')
    assert len(files)
    assert len(HT.get_theme(media)) == 1

    new_files = misc.download_theme(media, HT, theme_source='tvtunes')
    assert len(new_files)

    start, end = misc.get_offset_end(intro_file, HT)
    assert math.floor(start) == 116
    assert math.floor(end) == 208


def test_has_recap_audio(intro_file):
    audio = misc.convert_and_trim(intro_file)
    assert misc.has_recap_audio(audio, phrase=['previously on'])


def test_search_tunes():
    d = misc.search_tunes('dexter', 1337, url=None)
    assert d


def test_choose(monkeypatch, mocker):
    l = []
    for r in range(10):
        m = mocker.Mock()
        m.title = r
        l.append(m)

    with mocker.patch('click.prompt', side_effect=['0']):
        x = misc.choose('select', l, 'title')
        assert x[0].title == 0
