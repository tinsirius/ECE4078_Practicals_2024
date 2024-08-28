test = {
    "name": "performance",
    "points": 3,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> st_model = ConvNet()
                    >>> _ = st_model.load_state_dict(weights)
                    >>> _ = st_model.eval()
                    >>> total = 0
                    >>> correct = 0
                    >>> for data in testloader:
                    ...     images, labels = data
                    ...     outputs = st_model(images)
                    ...     _, predicted = torch.max(outputs, 1)
                    ...     total += labels.size(0)
                    ...     correct += (predicted == labels).sum().item()
                    >>> accuracy = 100*correct/total
                    >>> accuracy >= 60.0
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                    "failure_message": "Your accuracy is not higher than 60%"
                },
                {
                    "code": r"""
                    >>> st_model = ConvNet()
                    >>> _ = st_model.load_state_dict(weights)
                    >>> _ = st_model.eval()
                    >>> total = 0
                    >>> correct = 0
                    >>> for data in testloader:
                    ...     images, labels = data
                    ...     outputs = st_model(images)
                    ...     _, predicted = torch.max(outputs, 1)
                    ...     total += labels.size(0)
                    ...     correct += (predicted == labels).sum().item()
                    >>> accuracy = 100*correct/total
                    >>> accuracy >= 90.0
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                    "failure_message": "Your accuracy is not higher than 90%"
                },
                {
                    "code": r"""
                    >>> st_model = ConvNet()
                    >>> _ = st_model.load_state_dict(weights)
                    >>> _ = st_model.eval()
                    >>> total = 0
                    >>> correct = 0
                    >>> for data in testloader:
                    ...     images, labels = data
                    ...     outputs = st_model(images)
                    ...     _, predicted = torch.max(outputs, 1)
                    ...     total += labels.size(0)
                    ...     correct += (predicted == labels).sum().item()
                    >>> accuracy = 100*correct/total
                    >>> accuracy >= 95.0
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                    "success_message": "Good job",
                    "failure_message": "Your accuracy is not higher than 95%"
                }
            ],
            "scored": True,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}
