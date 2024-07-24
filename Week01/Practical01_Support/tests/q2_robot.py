test = {
	"name": "q2_robot",
	"points": 2,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> r = np.round(get_point_in_robot_frame(point_c=np.array([0, 1, 3]), gamma=0, disp_c=2), 2).flatten()
					>>> answer = np.array([0., 3., 3.]).flatten()
					>>> np.all(np.isclose(r, answer))
					True
					""",
					"hidden": True,
					"locked": False,
				},
				{
					"code": r"""
					>>> r = np.round(get_point_in_robot_frame(point_c=np.array([2, 0, 2]), gamma=np.pi/2, disp_c=2), 2).flatten()
					>>> answer = np.array([-2., 2., 2.]).flatten()
					>>> np.all(np.isclose(r, answer))
					True
					""",
					"hidden": True,
					"locked": False,
				},
				{
					"code": r"""
					>>> r = np.round(get_point_in_robot_frame(point_c=np.array([1, 1, 1]), gamma=-np.pi/3, disp_c=5), 2).flatten()
					>>> answer = np.array([5.7, 2.13, 1.]).flatten()
					>>> np.all(np.isclose(r, answer))
					True
					""",
					"hidden": True,
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
