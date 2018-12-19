#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import requests_mock

import unittest
from monit import Monit

class TestMonitClass(unittest.TestCase):
    mon = None

    @requests_mock.Mocker()
    def setUp(self, mock):
        with open('tests/fixture1.xml', 'r') as file:
            self.text = file.read().replace('\n', '')
            mock.get('http://localhost:2812/_status', text=self.text)
            self.mon = Monit()

    def test_process(self):
        assert "type" in self.mon['agent-1'].__dict__
        assert self.mon['agent-1'].type == "process"

    def test_platform(self):
        assert  self.mon['platform'].name == 'Linux'
        assert  self.mon['platform'].release == '3.12.70'
        assert  'memory' in self.mon['platform'].__dict__

if __name__ == '__main__':
    unittest.main()
