import json
import threading
import random


class Action(object):

    def __init__(self):
        """Set up the defaults for the Action object."""
        self.actions_data = {}
        self.action_types = ['jump', 'run']
        self.error_string = None
        self.lock = threading.Lock()
        self.json_string = None
        # Only used to generate a json data structure
        self.json_data_source = None

    def addAction(self, json_string_in):
        """Takes a string representation of a JSON dictionary.
        Parses the action from the dictionary and adds
        the value of the time key to the storage list."""
        error_string = None
        try:
            with self.lock:
                action, actionTime = self.validate_action(json_string_in)
                if action not in self.actions_data.keys():
                    self.actions_data[action] = []
                self.actions_data[action].append(actionTime)
        except Exception as err:
            error_string = str(err)
        return error_string

    def getStats(self):
        """Calculates the avarages of the current actions and returns a
        JSON string representation of the array of actions"""
        array_back = []
        with self.lock:
            for local_action in self.actions_data.keys():
                array_back.append(self.get_avarage_for_action(local_action))
        return json.dumps(array_back, indent=4)

    def validate_action(self, action_string):
        """Takes an action string and verifies that it
        • Converts from JSON to a dictionary
        • Contains the correct keys
        • Validates the action
        • Check time for positive int
        Returns the validated action and time"""
        self.json_data = json.loads(action_string)
        if not isinstance(self.json_data, dict):
            raise TypeError("String did not generate a dictionary")
        action = self.json_data.get('action')
        time = self.json_data.get('time')
        if action is None or time is None:
            raise TypeError(
                            "Time Type %s. Action Type %s"
                            % (type(time), type(action))
                            )
        if len(self.action_types) == 0:
            raise TypeError("Action type array is empty")
        if action not in self.action_types:
            raise ValueError("Action %s not in action types" % action)
        if not isinstance(time, int):
            raise ValueError("Bad Time %s" % time)
        return action, time

    def create_json_string(self):
        """Creates a dictionary with an action and time.
        Returns a JSON string"""
        action_dictionary = {}
        action_dictionary['action'] = self.action_types[random.randint(0, 1)]
        action_dictionary['time'] = random.randint(0, 150)
        return(json.dumps(action_dictionary))

    def avarage_stats(self, arrayIn):
        """Average the stats for returning.
        Takes a list of intigers, return the sum or None"""
        if len(arrayIn) != 0:
            return sum(arrayIn) / len(arrayIn)
        return None

    def get_avarage_for_action(self, action_in):
        """Takes the action to audit. Creates a dictionary with the
        action and an avarage of the time"""
        dict_to_json = {
                        'action': action_in,
                        'time': int(self.avarage_stats(
                                                   self.actions_data[action_in]
                                                   ))
                        }
        return dict_to_json
