
test = {
    "name": "dqn_performance",
    "points": 6,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> np.isnan(mean_return)
                    False
                    """,
                    "success_message": "Your network is outputting something",
                    "failure_message": "Your network is not outputing anything",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> mean_return > 0
                    True
                    """,
                    "success_message": "Average return is > 0",
                    "failure_message": "Average return is < 0",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> mean_return >= 50
                    True
                    """,
                    "success_message": "Average return is >= 50",
                    "failure_message": "Average return is < 50",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> mean_return >= 100
                    True
                    """,
                    "success_message": "Average return is >= 100",
                    "failure_message": "Average return is < 100",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> mean_return >= 150
                    True
                    """,
                    "success_message": "Average return is >= 150",
                    "failure_message": "Average return is < 150",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> mean_return >= 200
                    True
                    """,
                    "success_message": "Average return is >= 200",
                    "failure_message": "Average return is < 200",
                    "hidden": False,
                    "locked": False,
                },
            ],
            "scored": True,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}