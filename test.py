#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import requests_mock

import unittest
from monit import Monit

@requests_mock.Mocker()
class TestMonitClass(unittest.TestCase):
    text = ''

    def setUp(self):
        with open('tests/fixture1.xml', 'r') as file:
            self.text = file.read().replace('\n', '')

    def test_process(self, mock):
        mock.get('http://localhost:2812/_status', text=self.text)
        mon = Monit()
        assert "type" in mon['agent-1'].__dict__
        assert mon['agent-1'].type == "process"

        mock.get('http://localhost:2812/_status', text=self.text)
        mon = Monit()
        assert "Process" in str(mon['agent-1'])

if __name__ == '__main__':
    unittest.main()
