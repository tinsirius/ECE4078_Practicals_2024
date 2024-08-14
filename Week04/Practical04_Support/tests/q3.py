test = {
	"name": "rrtc",
	"points": 6,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
>>> import sys
>>> start = np.array([1.0, 10.0])
>>> goal = np.array([14.0, 1.0])
>>> expand_dis = 2.0
>>> all_obstacles = [Circle(11.5, 5, 2), Circle(4.5, 2.5, 2),Circle(4.8, 8, 2.5)]
>>> rrtc = RRTC(start=start, goal=goal, width=16, height=10, obstacle_list=all_obstacles, expand_dis=expand_dis, path_resolution=1)
>>> sys.stdout.write('skip '); plan = rrtc.planning() # doctest:+ELLIPSIS
skip ...
>>> distances = []
>>> for i in range(len(plan)-1):
...     distances.append(np.linalg.norm(np.array(plan[i]) - np.array(plan[i+1])))
>>> in_collision = False
>>> for obs in all_obstacles:
...     in_collision &= obs.is_in_collision_with_points(plan)
>>> condition1 = np.all(np.isclose(plan[0], np.array(start))) and np.all(np.isclose(plan[-1], np.array(goal)))
>>> condition2 = np.all(np.isclose(plan[0], np.array(goal))) and np.all(np.isclose(plan[-1], np.array(start)))
>>> condition3 = np.all(np.round(np.array(distances), 4) <= expand_dis)
>>> (condition1 or condition2) and (condition3) and (not in_collision)
True
					""",
					"hidden": True,
					"locked": False,
                    "success_message": "Correctly implemented loop",
                    "failure_message": "Wrong implementation of loop",
				},
                {
					"code": r"""
>>> import sys
>>> start = np.array([15.0, 11.0])
>>> goal = np.array([14.0, 1.0])
>>> expand_dis = 2.0
>>> all_obstacles = [Circle(11.5, 5, 2), Circle(4.5, 2.5, 2),Circle(4.8, 8, 2.5)]
>>> rrtc = RRTC(start=start, goal=goal, width=16, height=10, obstacle_list=all_obstacles, expand_dis=expand_dis, path_resolution=1)
>>> sys.stdout.write('skip '); plan = rrtc.planning() # doctest:+ELLIPSIS
skip ...
>>> distances = []
>>> for i in range(len(plan)-1):
...     distances.append(np.linalg.norm(np.array(plan[i]) - np.array(plan[i+1])))
>>> in_collision = False
>>> for obs in all_obstacles:
...     in_collision &= obs.is_in_collision_with_points(plan)
>>> condition1 = np.all(np.isclose(plan[0], np.array(start))) and np.all(np.isclose(plan[-1], np.array(goal)))
>>> condition2 = np.all(np.isclose(plan[0], np.array(goal))) and np.all(np.isclose(plan[-1], np.array(start)))
>>> condition3 = np.all(np.round(np.array(distances), 4) <= expand_dis)
>>> (condition1 or condition2) and (condition3) and (not in_collision)
True
					""",
					"hidden": True,
					"locked": False,
                    "success_message": "Correctly implemented loop",
                    "failure_message": "Wrong implementation of loop",
				},
                {
					"code": r"""
>>> import sys
>>> start = np.array([14.0, 10.0])
>>> goal = np.array([1.0, 1.0])
>>> expand_dis = 2.0
>>> all_obstacles = [Circle(11.5, 5, 2), Circle(4.5, 2.5, 2),Circle(4.8, 8, 2.5)]
>>> rrtc = RRTC(start=start, goal=goal, width=16, height=10, obstacle_list=all_obstacles, expand_dis=expand_dis, path_resolution=1)
>>> sys.stdout.write('skip '); plan = rrtc.planning() # doctest:+ELLIPSIS
skip ...
>>> distances = []
>>> for i in range(len(plan)-1):
...     distances.append(np.linalg.norm(np.array(plan[i]) - np.array(plan[i+1])))
>>> in_collision = False
>>> for obs in all_obstacles:
...     in_collision &= obs.is_in_collision_with_points(plan)
>>> condition1 = np.all(np.isclose(plan[0], np.array(start))) and np.all(np.isclose(plan[-1], np.array(goal)))
>>> condition2 = np.all(np.isclose(plan[0], np.array(goal))) and np.all(np.isclose(plan[-1], np.array(start)))
>>> condition3 = np.all(np.round(np.array(distances), 4) <= expand_dis)
>>> (condition1 or condition2) and (condition3) and (not in_collision)
True
					""",
					"hidden": True,
					"locked": False,
                    "success_message": "Correctly implemented loop",
                    "failure_message": "Wrong implementation of loop",
				}
			],
			"scored": True,
			"setup": "",
			"teardown": "",
			"type": "doctest"
		}
	]
}