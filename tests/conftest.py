import os
import sys
import tempfile

import pytest

fp = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'bw_plex')

# I dont like it..
sys.path.insert(1, fp)

# This is reimported by the tests.
# Do not delete.

import bw_plex
# Change default folder so we dont mess up the users normal things..
# This needs to deleted after all the tests are done.
bw_plex.DEFAULT_FOLDER = os.path.join(tempfile.gettempdir(), 'bw_plex_test_root')
if not os.path.exists(bw_plex.DEFAULT_FOLDER):
    os.makedirs(bw_plex.DEFAULT_FOLDER)


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
