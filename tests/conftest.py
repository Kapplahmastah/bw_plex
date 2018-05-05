import os
import sys

import pytest

fp = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'bw_plex')

# I dont like it..
sys.path.insert(1, fp)

# This is reimported by the tests.
# Do not delete.
import bw_plex.plex as plex
import bw_plex.misc as misc
import bw_plex.credits as credits


TEST_DATA = os.path.join(os.path.dirname(__file__), 'test_data')


@pytest.fixture()
def outro_file():
    fp = os.path.join(TEST_DATA, 'out.mkv')
    return fp


@pytest.fixture()
def intro_file():
    fp = os.path.join(TEST_DATA, 'dexter_s03e01_intro.mkv')
    return fp


@pytest.fixture()
def HT():
    return misc.get_hashtable()


@pytest.fixture()
def media(mocker):
    media = mocker.Mock()
    media.TYPE = 'show'
    media.name = 'dexter'
    media.ratingKey = 1337
    media.theme = ''
    media._server = ''
    media.title = 'dexter'

    return media
