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

    def test_extra_fields_system(self, mock):
        mock.get('http://localhost:2812/_status', text=self.text)
        mon = Monit()
        print mon['gw-0000']
        # TODO: really unstable interface here !!!
        assert mon['gw-0000'].type == "system"
        assert 'load' in mon['gw-0000']
        assert mon['gw-0000'].load is list
        assert 'cpu' in mon['gw-0000']
        assert mon['gw-0000'].cpu is dict
        assert 'memory' in mon['gw-0000']
        assert mon['gw-0000'].memory is dict
        assert 'swap' in mon['gw-0000']
        assert mon['gw-0000'].swap is dict

    def test_platform(self, mock):
        mock.get('http://localhost:2812/_status', text=self.text)
        mon = Monit()
        assert  mon['platform'].name == 'Linux'
        assert  mon['platform'].release == '3.12.70'
        assert  'memory' in mon['platform'].__dict__

if __name__ == '__main__':
    unittest.main()
