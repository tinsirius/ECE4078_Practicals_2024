test = {
    "name": "grow_tree",
    "points": 2,
    "suites": [ 
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> import pickle
                    >>> start = np.array([14.0, 10.0])
                    >>> goal = np.array([1.0, 1.0])
                    >>> expand_dis = 2.0
                    >>> all_obstacles = [Circle(11.5, 5, 2), Circle(4.5, 2.5, 2),Circle(4.8, 8, 2.5)]
                    >>> rrtc = RRTC(start=start, goal=goal, width=16, height=10, obstacle_list=all_obstacles, expand_dis=expand_dis, path_resolution=1)
                    >>> rrtc.start_node_list = [rrtc.start]
                    >>> rrtc.end_node_list = [rrtc.end]
                    >>> node = rrtc.Node(12.0, 9.0)
                    >>> _ = rrtc.grow_tree(rrtc.start_node_list, node)
                    >>> with open("Practical04_Support/pickle/q1.pkl", "rb") as f:
                    ...     expected_start_list = pickle.load(f)
                    >>> expected_start_list[-1] == rrtc.start_node_list[-1]
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                    "success_message": "Correct implementation for adding node",
                    "failure_message": "Wrong implementation for adding node",
                },
                {
                    "code": r"""
                    >>> start = np.array([11.5, 8.0])
                    >>> goal = np.array([1.0, 1.0])
                    >>> expand_dis = 2.0
                    >>> all_obstacles = [Circle(11.5, 5, 2), Circle(4.5, 2.5, 2),Circle(4.8, 8, 2.5)]
                    >>> rrtc = RRTC(start=start, goal=goal, width=16, height=10, obstacle_list=all_obstacles, expand_dis=expand_dis, path_resolution=1)
                    >>> rrtc.start_node_list = [rrtc.start]
                    >>> init_list = [rrtc.start]
                    >>> rrtc.end_node_list = [rrtc.end]
                    >>> node = rrtc.Node(11.5, 6.0)
                    >>> _ = rrtc.grow_tree(rrtc.start_node_list, node)
                    >>> len(rrtc.start_node_list) == len(init_list)
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                    "success_message": "Correctly checking for collision",
                    "failure_message": "Wrong implementation of collision checking",
                }
            ],
            "scored": False,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}