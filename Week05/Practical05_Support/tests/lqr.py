test = {
    "name": "lqr",
    "points": 3,
    "suites": [ 
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> import pickle
                    >>> a_file = open("Practical05_Support/pickle/lqr_case1.pk", "rb")
                    >>> data = pickle.load(a_file)
                    >>> A = data["A"]
                    >>> B = data["B"]
                    >>> C = data["C"]
                    >>> desired_state = data["desired_state"]
                    >>> initial_state = data['initial_state']
                    >>> horizon = data["horizon"]
                    >>> Q = data["Q"]
                    >>> R = data["R"]
                    >>> control_output = data["control"]
                    >>> state_output = data["output"]
                    >>> robot = Robot1D(A=A, B=B, C=C, initial_state=initial_state)
                    >>> controller = DiscreteFiniteLQR(Q=Q, R=R)
                    >>> controller.solve(robot, horizon)
                    >>> (y_array, u_array) = controller.run_control_loop(robot, desired_state, horizon)
                    >>> np.all(np.isclose(u_array.flatten(), control_output.flatten())) & np.all(np.isclose(y_array.flatten(), state_output.flatten()))
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> import pickle
                    >>> a_file = open("Practical05_Support/pickle/lqr_case2.pk", "rb")
                    >>> data = pickle.load(a_file)
                    >>> A = data["A"]
                    >>> B = data["B"]
                    >>> C = data["C"]
                    >>> desired_state = data["desired_state"]
                    >>> initial_state = data['initial_state']
                    >>> horizon = data["horizon"]
                    >>> Q = data["Q"]
                    >>> R = data["R"]
                    >>> control_output = data["control"]
                    >>> state_output = data["output"]
                    >>> robot = Robot1D(A=A, B=B, C=C, initial_state=initial_state)
                    >>> controller = DiscreteFiniteLQR(Q=Q, R=R)
                    >>> controller.solve(robot, horizon)
                    >>> (y_array, u_array) = controller.run_control_loop(robot, desired_state, horizon)
                    >>> np.all(np.isclose(u_array.flatten(), control_output.flatten())) & np.all(np.isclose(y_array.flatten(), state_output.flatten()))
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
