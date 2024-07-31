test = {
	"name": "q2",
	"points": 3,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
>>> from ece4078.Utility import _eval_timeout_print_str, enumerate_pickle
>>> exec(_eval_timeout_print_str())
>>> states = eval_timeout_print("get_bicycle_trajectory(initial_state=np.array([5, -5, np.pi/4, 0.1]), max_t=200, v=2.3, phi=0.01)") # doctest:+ELLIPSIS
skip ...
>>> pickle_name_list = (["q2_file1.pk"])
>>> pickle_list = enumerate_pickle(pickle_name_list, path = "Practical02_Support/pickle/")
>>> expected_result = False
>>> for my_pickle in pickle_list:
...     result = np.all(np.isclose(my_pickle[:, :], states[:, :])) 
...     expected_result = expected_result or result
>>> expected_result
True
					""",
					"hidden": True,
					"locked": False,
				},
                {
					"code": r"""
>>> from ece4078.Utility import _eval_timeout_print_str, enumerate_pickle
>>> exec(_eval_timeout_print_str())
>>> states = eval_timeout_print("get_bicycle_trajectory(initial_state=np.array([1, 1, 0, 0.05]), max_t=200, v=1.3, phi=0.05)") # doctest:+ELLIPSIS
skip ...
>>> pickle_name_list = (["q2_file2.pk"])
>>> pickle_list = enumerate_pickle(pickle_name_list, path = "Practical02_Support/pickle/")
>>> expected_result = False
>>> for my_pickle in pickle_list:
...     result = np.all(np.isclose(my_pickle[:, :], states[:, :])) 
...     expected_result = expected_result or result
>>> expected_result
True
					""",
					"hidden": True,
					"locked": False,
				},
                {
					"code": r"""
>>> from ece4078.Utility import _eval_timeout_print_str, enumerate_pickle
>>> exec(_eval_timeout_print_str())
>>> states = eval_timeout_print("get_bicycle_trajectory(initial_state=np.array([5, -5, np.pi/4, 0.1]), max_t=200, v=0, phi=0.01)") # doctest:+ELLIPSIS
skip ...
>>> pickle_name_list = (["q2_file3.pk"])
>>> pickle_list = enumerate_pickle(pickle_name_list, path = "Practical02_Support/pickle/")
>>> expected_result = False
>>> for my_pickle in pickle_list:
...     result = np.all(np.isclose(my_pickle[:, :], states[:, :])) 
...     expected_result = expected_result or result
>>> expected_result
True
					""",
					"hidden": True,
					"locked": False,
				},
                {
					"code": r"""
>>> from ece4078.Utility import _eval_timeout_print_str, enumerate_pickle
>>> exec(_eval_timeout_print_str())
>>> states = eval_timeout_print("get_bicycle_trajectory(initial_state=np.array([1, 1, 0, 0.05]), max_t=200, v=0, phi=0.05)") # doctest:+ELLIPSIS
skip ...
>>> pickle_name_list = (["q2_file4.pk"])
>>> pickle_list = enumerate_pickle(pickle_name_list, path = "Practical02_Support/pickle/")
>>> expected_result = False
>>> for my_pickle in pickle_list:
...     result = np.all(np.isclose(my_pickle[:, :], states[:, :])) 
...     expected_result = expected_result or result
>>> expected_result
True
					""",
					"hidden": True,
					"locked": False,
				},
                {
					"code": r"""
>>> from ece4078.Utility import _eval_timeout_print_str, enumerate_pickle
>>> exec(_eval_timeout_print_str())
>>> states = eval_timeout_print("get_bicycle_trajectory(initial_state=np.array([1, 1, 0, 0]), max_t=200, v=0, phi=0)") # doctest:+ELLIPSIS
skip ...
>>> pickle_name_list = (["q2_file5.pk"])
>>> pickle_list = enumerate_pickle(pickle_name_list, path = "Practical02_Support/pickle/")
>>> expected_result = False
>>> for my_pickle in pickle_list:
...     result = np.all(np.isclose(my_pickle[:, :], states[:, :])) 
...     expected_result = expected_result or result
>>> expected_result
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