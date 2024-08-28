test = {
    "name": "architecture",
    "points": 3,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> import pickle
                    >>> a_file = open("Practical06_Support/pickle/expected_architecture.pk", "rb")
                    >>> true_model = pickle.load(a_file)
                    >>> st_model = ConvNet()
                    >>> layers_condition = []
                    >>> for param_tensor, param_tensor_size in zip(st_model.state_dict(), true_model):
                    ...     layers_condition.append(st_model.state_dict()[param_tensor].size() ==  param_tensor_size)
                    >>> all(layers_condition)
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                }
            ],
            "scored": True,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}
