import unittest
import shutil
import re
import os
import bz2file
from loggers import Loggers

def decomp_bz2(log_file):
    with bz2file.open(log_file) as mfile:
        datalog = mfile.read()
    return datalog

class LoggersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logpath = '/tmp/logTest'
        os.mkdir(cls.logpath)
        cls.logTest = Loggers('logTest', log_folder_path=cls.logpath)
        cls.logTest.set_log_rotate_handler(True)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.logpath)

    def perform_regex_test(self, log_level, log_function, log_message, log_level_dst):
        self.logTest.set_log_level(log_level)
        log_function(log_message)
        datalog = decomp_bz2(self.logpath+'/logTest.'+log_level_dst+'.log.bz2')
        match = re.match('Log: '+log_message+' | Log level:'+log_level+
                         r' | Date:\d{2}\/\d{2}\/\d{4} d{2}:\d{2}:\d{2}',
                         datalog.splitlines()[-1])
        return match

    def test_debug_log(self):
        self.assertIsNotNone(self.perform_regex_test('DEBUG', self.logTest.log.debug,
                                                     'Debug Test.', 'debug'))

    def test_info_log(self):
        self.assertIsNotNone(self.perform_regex_test('INFO', self.logTest.log.info,
                                                     'Info Test.', 'debug'))

    def test_warning_log(self):
        self.assertIsNotNone(self.perform_regex_test('WARNING', self.logTest.log.warning,
                                                     'Warning Test.', 'debug'))

    def test_error_log(self):
        self.assertIsNotNone(self.perform_regex_test('ERROR', self.logTest.log.error,
                                                     'Error Test.', 'error'))

    def test_critical_log(self):
        self.assertIsNotNone(self.perform_regex_test('CRITICAL', self.logTest.log.critical,
                                                     'Critical Test.', 'error'))

    def test_log_hierarchy(self):
        log_message = 'Debug log in CRITICAL log level Test.'
        self.assertIsNone(self.perform_regex_test('CRITICAL', self.logTest.log.debug,
                                                  log_message, 'error'))
        log_message = 'Info log in CRITICAL log level Test.'
        self.assertIsNone(self.perform_regex_test('CRITICAL', self.logTest.log.info,
                                                  log_message, 'error'))
        log_message = 'Warning log in CRITICAL log level Test.'
        self.assertIsNone(self.perform_regex_test('CRITICAL', self.logTest.log.warning,
                                                  log_message, 'error'))
        log_message = 'Error log in CRITICAL log level Test.'
        self.assertIsNone(self.perform_regex_test('CRITICAL', self.logTest.log.error,
                                                  log_message, 'error'))
        log_message = 'Critical log in CRITICAL log level Test.'
        self.assertIsNotNone(self.perform_regex_test('CRITICAL', self.logTest.log.critical,
                                                     log_message, 'error'))

if __name__ == "__main__":
    unittest.main()
