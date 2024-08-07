test = {
    "name": "predict_func",
    "points": 2,
    "suites": [ 
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> import pickle
                    >>> with open("Practical03_Support/pickle/q1.pkl", "rb") as f:
                    ...     expected_P = pickle.load(f)
                    >>> test_bot = PenguinPi(0.15, 0.1)
                    >>> test_P = np.eye(3)*10
                    >>> test_drive_signal = DriveMeasurement(10, 11 , 0.2 , 5, 5)
                    >>> P, _ = predict_step(test_bot, test_P, test_drive_signal)
                    >>> np.all(np.isclose(P, expected_P)) 
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                    "success_message": "Good Job",
                    "failure_message": "Wrong implementation of P",
                }
            ],
            "scored": False,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}