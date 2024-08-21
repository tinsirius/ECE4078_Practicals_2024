test = {
    "name": "q1_reached",
    "points": 1,
    "suites": [ 
        {
            "cases": [ 
                {
                    "code": r"""
					>>> from ece4078.Utility import enumerate_pickle
                    >>> pickle_name_list = (["q1_case1.pk", "q1_case2.pk", "q1_case3.pk"])
                    >>> pickle_list = enumerate_pickle(pickle_name_list, path = "Practical05_Support/pickle/")
                    >>> delta_t = 0.01
                    >>> passed = True
                    >>> for data in pickle_list:
                    ...     start = data["start"]
                    ...     goal = data["goal"]
                    ...     bot = PenguinPi(init_state=start)
                    ...     controller = MoveToPoseController(bot)
                    ...     robot_states, robot_controls = controller.run(goal_position=goal, delta_time=delta_t)
                    ...     dist_travel = np.sum((np.power(robot_states[1:-1,0:2]-robot_states[0:-2,0:2],2) @ np.ones([2,1]))**0.5)
                    ...     example_states = data["states"]
                    ...     ref_dist_travel = np.sum((np.power(example_states[0:-2,0:2]-example_states[1:-1,0:2],2) @ np.ones([2,1]))**0.5)
                    ...     passed = passed and (dist_travel < ref_dist_travel)
                    >>> passed 
                    True
                    """,
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
