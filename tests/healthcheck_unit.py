from fabplugins import healthcheck

from mock import patch
import unittest


class TestHealthcheck(unittest.TestCase):

    def test_without_parameters(self):
        with patch.object(healthcheck, 'run') as mocked_run:
            mocked_run.return_value = 'WORKING'
            healthcheck.do_healthcheck('http://test.com')

        mocked_run.assert_called_once_with('curl -L http://test.com/healthcheck')

    def test_with_custom_uri(self):
        with patch.object(healthcheck, 'run') as mocked_run:
            mocked_run.return_value = 'WORKING'
            healthcheck.do_healthcheck('http://test.com', uri='derpcheck')

        mocked_run.assert_called_once_with('curl -L http://test.com/derpcheck')

    def test_with_custom_body(self):
        with patch.object(healthcheck, 'run') as mocked_run:
            mocked_run.return_value = 'DERPING'
            healthcheck.do_healthcheck('http://test.com', body='DERPING')

        mocked_run.assert_called_once_with('curl -L http://test.com/healthcheck')
