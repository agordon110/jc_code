import unittest
import json
from Action import Action


class TestAction(unittest.TestCase):

    action = Action()

    # Test data. Gets encoded to json during testing
    json_array = [1, 2, 3]

    good_json = {"action": "jump", "time": 57}
    none_json = {"action": None, "time": 57}
    empty_json = {"action": "", "time": 57}
    action_json_string = {"action": "sleep", "time": 57}

    time_string = {"action": "jump", "time": "57"}
    time_as_none = {"action": "jump", "time": None}
    negative_time = {"action": "jump", "time": -57}

    def test_addAction(self):
        """Start of a test for addAction"""
        self.action.action_types = ['jump', 'run']
        # Verify we decode dictionary by feeding it an array
        self.assertIsNotNone(self.action.addAction(
            json.dumps(self.json_array)))
        # Basic set of tests for actions. Nowhere near exhaustive
        self.assertIsNone(self.action.addAction(json.dumps(self.good_json)))
        # try with no action
        self.assertIsNone(self.action.addAction(json.dumps(self.good_json)))
        # try with an empty action
        self.assertIsNotNone(self.action.addAction(
            json.dumps(self.empty_json)))

        # Basic set of time validation
        # Time as a string
        self.assertIsNotNone(self.action.addAction(
            json.dumps(self.time_string)))
        # try with a negative int
        self.assertIsNone(self.action.addAction(
            json.dumps(self.negative_time)))

    def test_getStats(self):
        """Test getStats by feeding it a known quantity"""
        self.action.action_types = ['jump', 'run']
        self.action.addAction(json.dumps(self.good_json))
        # getStat returns an array and in testing we only care about enty 0
        results_back = json.loads(self.action.getStats())[0]
        res = 'action'
        self.assertEqual(results_back.get(res), self.good_json.get(res))

    def test_validate_action(self):
        self.action.action_types = ['jump', 'run']
        json_string = json.dumps(self.good_json)
        jp = 'jump'
        self.assertEqual(self.action.validate_action(json_string), (jp, 57))

    def test_create_json_string(self):
        self.action.action_types = ['jump', 'run']
        self.assertEqual(type(self.action.create_json_string()), type(str()))

    def test_avarage_stats(self):
        self.assertEqual(self.action.avarage_stats([1, 2, 3, 4, 5]), 3)
        self.assertNotEqual(self.action.avarage_stats([1, 2, 3, 4, 27]), 3)
        self.assertIsNone(self.action.avarage_stats([]))

    def test_get_avarage_for_action(self):
        self.action.action_types = ['jump', 'run']
        self.action.addAction(json.dumps(self.good_json))
        result_dict = self.action.get_avarage_for_action("jump")
        self.assertNotEqual(result_dict, {'action': 'jump', 'time': 57})


if __name__ == '__main__':
    unittest.main()
