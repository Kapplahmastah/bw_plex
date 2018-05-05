import os
import glob
from conftest import credits, TEST_DATA

image_type = ('.png', '.jpeg', '.jpg')


def _test_locate_text():
    files = glob.glob('%s\*.*' % TEST_DATA)

    for f in sorted(files):
        if f.endswith(image_type):
            if 'fail' in f:
                assert not credits.locate_text(f)
            else:
                assert credits.locate_text(f)


def _test_extract_text():
    fp = os.path.join(TEST_DATA, 'blacktext_whitebg_2.png')

    assert credits.extract_text(fp) == b'A\n\nJOHN GOLDWYN\n\nPRODUCTION'


def _test_find_credits2(video_file):
    #fp = os.path.join(TEST_DATA, 'out.mkv')

    t = credits.find_credits(video_file, offset=1)
    print(t)##


def test_find_credits(video_file):
    #fp = os.path.join(TEST_DATA, 'out.mkv')

    t = credits.find_credits(video_file, frame_range=True, check=9999)
    print(t)


#def test_video_frame_by_frame():
#    fp = os.path.join(TEST_DATA, 'out.mkv')
#    t = list(credits.video_frame_by_frame(fp, offset=50, frame_range=True))
#    print(t)

