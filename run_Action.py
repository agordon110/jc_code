#!/usr/bin/python

import threading
# Action should be the only library needed that is not out of the box
from Action import Action


def do_method(action_object, *args):
    """Function is called with an optional argument.
    We use the presence of the arg to determine which of the core
    functions to call. No arg and we get stats, arg and we add the action"""
    if args:
        errorBack = action_object.addAction(args[0])
        if errorBack:
            print("Got an error %s" % errorBack)
    else:
        statArrayString = action_object.getStats()
        print("Current stat:\n%s" % statArrayString)


def main():
    """Action object is is created. We then loop a range generating
    new action strings. Halfway through we make a call to getStats.
    Threading is intended to try and exersise the concurrency protection"""
    action = Action()
    # Pad by one to support calling for stats in the middle
    loop_count = 0
    for i in range(0, 11):
        # Spawn work threads. When calling do_method we pass the action object
        # and a json string to trigger addition instead of getting stats
        if i == 5:
            # Call do_method with no arg to trigger the stats call
            thread_object = threading.Thread(target=do_method, args=(action, ))
        else:
            # Create JSON string and call do method passing in the string
            thread_object = threading.Thread(
                                            target=do_method,
                                            args=(
                                                    action,
                                                    action.create_json_string()
                                                    )
                                            )
        # Start the thread and join so we wait til done.
        thread_object.start()
        thread_object.join()
        loop_count += 1

    # Final Check of the stats
    stats_back = action.getStats()
    print("Final stats for %s loops:\n%s" % (loop_count, stats_back))


if __name__ == "__main__":
    main()
