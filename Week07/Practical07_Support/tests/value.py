test = {
    "name": "value",
    "points": 3,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> from ece4078.Utility import enumerate_pickle
                    >>> pickle_name_list = (["value_q1.pk", "value_q2.pk", "value_q3.pk"])
                    >>> pickle_list = enumerate_pickle(pickle_name_list, path = "Practical07_Support/pickle/")
                    >>> passed = True
                    >>> for data in pickle_list:
                    ...     expected_opt_state = data['value_state_function']
                    ...     grid_world = GridEnv(gamma=data['gamma'], noise=data['noise'], living_reward=data['living_reward'])
                    ...     optimal_state_function, _ = value_iteration(grid_world, plot=False)
                    ...     total_correct = 0
                    ...     for computed_value, expected_value in zip(optimal_state_function, expected_opt_state):             
                    ...         total_correct += np.isclose(computed_value, expected_value)         
                    ...     passed = passed and total_correct >= len(optimal_state_function) * 0.3
                    >>> passed
                    True
                    """,
                    "success_message": f"Value Function: You have more than {round(11 * 0.3 - 0.5)} square correct in 3 different scenarios",
                    "failure_message": f"Value Function: You have less than {round(11 * 0.3 + 0.5)} square correct in 3 different scenarios",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> from ece4078.Utility import enumerate_pickle
                    >>> pickle_name_list = (["value_q1.pk", "value_q2.pk", "value_q3.pk"])
                    >>> pickle_list = enumerate_pickle(pickle_name_list, path = "Practical07_Support/pickle/")
                    >>> passed = True
                    >>> for data in pickle_list:
                    ...     expected_opt_state = data['value_state_function']
                    ...     grid_world = GridEnv(gamma=data['gamma'], noise=data['noise'], living_reward=data['living_reward'])
                    ...     optimal_state_function, _ = value_iteration(grid_world, plot=False)
                    ...     total_correct = 0
                    ...     for computed_value, expected_value in zip(optimal_state_function, expected_opt_state):             
                    ...         total_correct += np.isclose(computed_value, expected_value)         
                    ...     passed = passed and total_correct >= len(optimal_state_function) * 0.7
                    >>> passed
                    True
                    """,
                    "success_message": f"Value Function: You have more than {round(11 * 0.7 - 0.5)} square correct in 3 different scenarios",
                    "failure_message": f"Value Function: You have less than {round(11 * 0.7 + 0.5)} square correct in 3 different scenarios",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> from ece4078.Utility import enumerate_pickle
                    >>> pickle_name_list = (["value_q1.pk", "value_q2.pk", "value_q3.pk"])
                    >>> pickle_list = enumerate_pickle(pickle_name_list, path = "Practical07_Support/pickle/")
                    >>> passed = True
                    >>> for data in pickle_list:
                    ...     expected_opt_state = data['value_state_function']
                    ...     grid_world = GridEnv(gamma=data['gamma'], noise=data['noise'], living_reward=data['living_reward'])
                    ...     optimal_state_function, _ = value_iteration(grid_world, plot=False)
                    ...     total_correct = 0
                    ...     for computed_value, expected_value in zip(optimal_state_function, expected_opt_state):             
                    ...         total_correct += np.isclose(computed_value, expected_value)         
                    ...     passed = passed and total_correct >= len(optimal_state_function) * 0.9
                    >>> passed
                    True
                    """,
                    "success_message": f"Value Function: All your squares are correct in 3 different scenarios",
                    "failure_message": f"Value Function: All your squares are correct in 3 different scenarioss",
                    "hidden": False,
                    "locked": False,
                }
            ],
            "scored": False,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}