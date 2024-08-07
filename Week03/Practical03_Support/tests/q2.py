test = {
    "name": "R_func",
    "points": 2,
    "suites": [ 
        {
            "cases": [
                {
                    "code": r"""
                    >>> correct = True
                    >>> for k in [3, 7]:
                    ...     test_measurements = [MarkerMeasurement(np.array([i]*2), i, np.identity(2) * (i + 1) * 10) for i in range(k)]
                    ...     _, R = construct_R(test_measurements)
                    ...     correct = correct and (R.shape == (2*k,2*k))
                    >>> correct
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                    "success_message": "Correct R dimension",
                    "failure_message": "R has wrong dimension",
                },
                {
                    "code": r"""
                    >>> import pickle
                    >>> with open("Practical03_Support/pickle/q2.pkl", "rb") as f:
                    ...     expected_R = pickle.load(f)
                    >>> test_measurements = [MarkerMeasurement(np.array([i]*2), i, np.identity(2) * (i + 1) * 10) for i in range(3)]
                    >>> _, R = construct_R(test_measurements)
                    >>> np.all(np.isclose(R, expected_R)) 
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                    "success_message": "Filling the number correctly.",
                    "failure_message": "Filling the number wrong.",
                }
            ],
            "scored": False,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}