test = {
    "name": "update_func",
    "points": 2,
    "suites": [ 
        {
            "cases": [
                 {
                    "code": r"""
                    >>> import pickle
                    >>> test_bot = PenguinPi(0.16, 0.1)
                    >>> test_P = np.eye(3)*15
                    >>> test_z = np.array([[i]*2 for i in range(markers.shape[1])]).reshape(-1, 1)
                    >>> test_x_bar = np.array([0]*3)
                    >>> test_R = np.identity(2 * markers.shape[1])
                    >>> _, _ = update_step(test_bot, test_P, test_R, test_z, test_x_bar, tags)
                    """,
                    "hidden": False,
                    "locked": False,
                    "success_message": "This function ran successfully.",
                    "failure_message": "This function cannot run without error.",
                },
                {
                    "code": r"""
                    >>> import pickle
                    >>> with open("Practical03_Support/pickle/q3.pkl", "rb") as f:
                    ...     expected_x, _ = pickle.load(f)
                    >>> test_bot = PenguinPi(0.16, 0.1)
                    >>> test_P = np.eye(3)*15
                    >>> test_z = np.array([[i]*2 for i in range(markers.shape[1])]).reshape(-1, 1)
                    >>> test_x_bar = np.array([0]*3)
                    >>> test_R = np.identity(2 * markers.shape[1])
                    >>> corrected_x, _ = update_step(test_bot, test_P, test_R, test_z, test_x_bar, tags)
                    >>> np.all(np.isclose(expected_x, corrected_x)) 
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                    "success_message": "Implemented corrected_x correctly.",
                    "failure_message": "Implemented corrected_x wrong.",
                },
                {
                    "code": r"""
                    >>> import pickle
                    >>> with open("Practical03_Support/pickle/q3.pkl", "rb") as f:
                    ...     _, expected_P = pickle.load(f)
                    >>> test_bot = PenguinPi(0.16, 0.1)
                    >>> test_P = np.eye(3)*15
                    >>> test_z = np.array([[i]*2 for i in range(markers.shape[1])]).reshape(-1, 1)
                    >>> test_x_bar = np.array([0]*3)
                    >>> test_R = np.identity(2 * markers.shape[1])
                    >>> _, corrected_P = update_step(test_bot, test_P, test_R, test_z, test_x_bar, tags)
                    >>> np.all(np.isclose(expected_P, corrected_P)) 
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                    "success_message": "Implemented corrected_P correctly.",
                    "failure_message": "Implemented corrected_P wrong.",
                }
            ],
            "scored": False,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}