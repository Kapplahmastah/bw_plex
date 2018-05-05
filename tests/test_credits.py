import math
import os
import glob

from conftest import credits, TEST_DATA

image_type = ('.png', '.jpeg', '.jpg')


def test_locate_text():
    files = glob.glob('%s\*.*' % TEST_DATA)

    for f in sorted(files):
        if f.endswith(image_type):
            if 'fail' in f:
                assert not credits.locate_text(f)
            else:
                assert credits.locate_text(f)


def test_extract_text():
    fp = os.path.join(TEST_DATA, 'blacktext_whitebg_2.png')

    assert credits.extract_text(fp) == b'A\n\nJOHN GOLDWYN\n\nPRODUCTION'


def test_find_credits2(video_file):
    start, end = credits.find_credits(video_file, offset=3, frame_range=False, check=7)
    assert math.floor(start) == 3
    assert math.floor(end) == 3
    print('start', start)
    print('end', end)


def test_find_credits(video_file):
    start, end = credits.find_credits(video_file, frame_range=True, check=9999)
    assert math.floor(start) == 4.0
    assert math.floor(end) == 58
