test = {
    "name": "q1_accurate",
    "points": 2,
    "suites": [ 
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> from ece4078.Utility import enumerate_pickle
                    >>> pickle_name_list = (["q1_case1.pk", "q1_case2.pk", "q1_case3.pk"])
                    >>> pickle_list = enumerate_pickle(pickle_name_list, path = "Practical05_Support/pickle/")
                    >>> tol = np.array([0.001, 0.001, 0.23])
                    >>> delta_t = 0.01
                    >>> passed = True
                    >>> for data in pickle_list:
                    ...     start = data["start"]
                    ...     goal = data["goal"]
                    ...     bot = PenguinPi(init_state=start)
                    ...     controller = MoveToPoseController(bot)
                    ...     robot_states, robot_controls = controller.run(goal_position=goal, delta_time=delta_t)
                    ...     pose_error = abs(robot_states[-1,:] - goal)
                    ...     passed = passed and ((pose_error < tol).all())
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