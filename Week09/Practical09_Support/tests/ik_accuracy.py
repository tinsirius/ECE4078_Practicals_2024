test = {
    "name": "ik_accuracy",
    "points": 7,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> link1 = RevoluteDH(d=0.8, a=0, alpha=np.pi/2)
                    >>> link2 = RevoluteDH(d=0, a=0.8, alpha=0)
                    >>> link3 = RevoluteDH(d=0, a=0.8, alpha=0)
                    >>> my_bot = DHRobot([link1, link2, link3], name='3dof-manipulator')
                    >>> with open('Practical09_Support/pickle/IK_q3.pk', 'rb') as my_file:
                    ...     data = pickle.load(my_file)
                    ...     target = SE3(data['target'])
                    ...     my_bot.q = data['initial_q']
                    ...     expected_q = data['q_sequence']
                    >>> predicted_q = inverse_kinematics(my_bot, target,  max_iterations=100, delta=0.1)
                    >>> np.all(np.isclose(expected_q, predicted_q))
                    True
                    """,
                    "success_message": "passing from [ 0., pi/6, -pi/6] to [0., 0., 2.4]",
                    "failure_message": "failing from [ 0., pi/6, -pi/6] to [0., 0., 2.4]",
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> link1 = RevoluteDH(d=0.8, a=0, alpha=np.pi/2)
                    >>> link2 = RevoluteDH(d=0, a=0.8, alpha=0)
                    >>> link3 = RevoluteDH(d=0, a=0.8, alpha=0)
                    >>> my_bot = DHRobot([link1, link2, link3], name='3dof-manipulator')
                    >>> with open('Practical09_Support/pickle/IK_q5.pk', 'rb') as my_file:
                    ...     data = pickle.load(my_file)
                    ...     target = SE3(data['target'])
                    ...     my_bot.q = data['initial_q']
                    ...     expected_q = data['q_sequence']
                    >>> predicted_q = inverse_kinematics(my_bot, target,  max_iterations=100, delta=0.1)
                    >>> np.all(np.isclose(expected_q, predicted_q))
                    True
                    """,
                    "success_message": "passing from [0., 0., pi/4] to [-0.009, 0., 1.93 ]",
                    "failure_message": "failing from [0., 0., pi/4] to [-0.009, 0., 1.93 ]",
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
