
from tests.test_search_property import SearchPropertyTest
from unittest import TestLoader, TestSuite, TextTestRunner

if __name__ == '__main__':

    loader = TestLoader()
    suite = TestSuite(
        loader.loadTestsFromTestCase(SearchPropertyTest),
        # loader.loadTestsFromTestCase(MyTestCase2)
        # if we need to run many unittest.TestCase add here using comma separated
    )

    runner = TextTestRunner(verbosity=1)
    runner.run(suite)

