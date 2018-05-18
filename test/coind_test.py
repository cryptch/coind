import unittest
import json
from test import config
from coind import Coind


# Test
# Coind class test
class CoindTest(unittest.TestCase):
    def test_getinfo(self):
        """
        Test correct getinfo, using vsync and type cli
        If vsync is running, will return version inside json
        If vsync is not running, will return error message
        It will validate both situations
        """

        coind = Coind(config.COIND_NAME, config.COIND_TYPE, config.COIND_PATH, config.COIND_DEBUG)
        raw_result = coind.run('getinfo')
        try:
            result = json.loads(raw_result)
            expected = 3080500
            self.assertEqual(result['version'], expected)
        except ValueError:
            expected = 'error: couldn\'t connect to server'
            self.assertEqual(raw_result, expected)

    def test_getinfo_as_type_d(self):
        """
        Test uncorrect getinfo, using vsync and type d
        vsync not support command for vsyncd
        Message return:
        "Error: There is no RPC client functionality in vsyncd anymore. Use the vsync-cli utility instead."
        But is I/O output error and current method not return
        """

        coind = Coind(config.COIND_NAME, Coind.TYPE_D, config.COIND_PATH, config.COIND_DEBUG)
        result = coind.run('getinfo')
        expected = 'Error: There is no RPC client functionality in vsyncd anymore. Use the vsync-cli utility instead.'
        self.assertEqual(result, expected)

    def test_getinfo_as_method_name(self):
        """
        Test calling getinfo as method
        """

        coind = Coind(config.COIND_NAME, config.COIND_TYPE, config.COIND_PATH, config.COIND_DEBUG)
        raw_result = coind.getinfo()
        try:
            result = json.loads(raw_result)
            expected = 3050000
            self.assertEqual(result['version'], expected)
        except ValueError:
            expected = 'error: couldn\'t connect to server'
            self.assertEqual(raw_result, expected)


if __name__ == '__main__':
    unittest.main()
