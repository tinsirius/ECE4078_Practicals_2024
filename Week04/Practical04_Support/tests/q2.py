test = {
    "name": "check_trees_distance",
    "points": 1,
    "suites": [ 
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> start = np.array([12.0, 10.0])
                    >>> goal = np.array([1.0, 1.0])
                    >>> expand_dis = 3.0
                    >>> all_obstacles = [Circle(11.5, 5, 2), Circle(4.5, 2.5, 2),Circle(4.8, 8, 2.5)]
                    >>> rrtc = RRTC(start=start, goal=goal, width=16, height=10, obstacle_list=all_obstacles, expand_dis=expand_dis, path_resolution=1)
                    >>> rrtc.start_node_list = [rrtc.start]
                    >>> rrtc.end_node_list = [rrtc.end]
                    >>> false_cond = rrtc.check_trees_distance()
                    >>> rrtc.start_node_list.append(rrtc.Node(1.0, goal[-1]+expand_dis-0.01))
                    >>> true_cond = rrtc.check_trees_distance()
                    >>> true_cond and not false_cond
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                    "success_message": "Correct implementation for distance checking",
                    "failure_message": "Wrong implementation for distance checking",
                }
            ],
            "scored": False,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}