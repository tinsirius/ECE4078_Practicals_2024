test = {
    "name": "policy",
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
                    ...     expected_opt_pol = data['optimal_policy']
                    ...     grid_world = GridEnv(gamma=data['gamma'], noise=data['noise'], living_reward=data['living_reward'])
                    ...     _, optimal_policy = value_iteration(grid_world, plot=False)
                    ...     total_correct = np.sum(np.isclose(expected_opt_pol.flatten(), optimal_policy.flatten()))
                    ...     passed = passed and (total_correct >= len(expected_opt_pol.flatten()) * 0.3)
                    >>> passed
                    True
                    """,
                    "success_message": f"Policy: You have more than {round(12 * 0.3 - 0.5)} square correct in 3 different scenarios",
                    "failure_message": f"Policy: You have less than {round(12 * 0.3 + 0.5)} square correct in 3 different scenarios",
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
                    ...     expected_opt_pol = data['optimal_policy']
                    ...     grid_world = GridEnv(gamma=data['gamma'], noise=data['noise'], living_reward=data['living_reward'])
                    ...     _, optimal_policy = value_iteration(grid_world, plot=False)
                    ...     total_correct = np.sum(np.isclose(expected_opt_pol.flatten(), optimal_policy.flatten()))
                    ...     passed = passed and total_correct >= len(expected_opt_pol.flatten()) * 0.7
                    >>> passed
                    True
                    """,
                    "success_message": f"Policy: You have more than {round(12 * 0.7 - 0.5)} square correct in 3 different scenarios",
                    "failure_message": f"Policy: You have less than {round(12 * 0.7 + 0.5)} square correct in 3 different scenarios",
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
                    ...     expected_opt_pol = data['optimal_policy']
                    ...     grid_world = GridEnv(gamma=data['gamma'], noise=data['noise'], living_reward=data['living_reward'])
                    ...     _, optimal_policy = value_iteration(grid_world, plot=False)
                    ...     total_correct = np.sum(np.isclose(expected_opt_pol.flatten(), optimal_policy.flatten()))
                    ...     passed = passed and total_correct >= len(expected_opt_pol.flatten()) * 0.92
                    >>> passed
                    True
                    """,
                    "success_message": "Policy: All your squares are correct in 3 different scenarios",
                    "failure_message": "Policy: Not all your squares are correct in 3 different scenarios",
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
