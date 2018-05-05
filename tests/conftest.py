import os
import sys

import pytest

fp = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'bw_plex')

# I dont like it..
sys.path.insert(1, fp)

import bw_plex.plex as plex
import bw_plex.misc as misc
import bw_plex.credits as credits

TEST_DATA = os.path.join(os.path.dirname(__file__), 'test_data')


@pytest.fixture()
def video_file():
    fp = os.path.join(TEST_DATA, 'out.mkv')
    return fp
