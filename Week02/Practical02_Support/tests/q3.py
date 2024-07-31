test = {
	"name": "q3",
	"points": 2,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
>>> from ece4078.Utility import _eval_timeout_print_str, enumerate_pickle
>>> exec(_eval_timeout_print_str())
>>> states = eval_timeout_print("get_penguipi_trajectory(initial_state=np.array([0, 0, np.pi/2]), max_t=200, right_rate=10, left_rate=10)") # doctest:+ELLIPSIS
skip ...
>>> pickle_name_list = (["q3_file1.pk"])
>>> pickle_list = enumerate_pickle(pickle_name_list, path = "Practical02_Support/pickle/")
>>> expected_result = False
>>> for my_pickle in pickle_list:
...    result = np.all(np.isclose(my_pickle[:, :], states[:, :])) 
...    expected_result = expected_result or result
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
>>> states = eval_timeout_print("get_penguipi_trajectory(initial_state=np.array([1, -1, np.pi/4]), max_t=200, right_rate=20, left_rate=10)") # doctest:+ELLIPSIS
skip ...
>>> pickle_name_list = (["q3_file2.pk"])
>>> pickle_list = enumerate_pickle(pickle_name_list, path = "Practical02_Support/pickle/")
>>> expected_result = False
>>> for my_pickle in pickle_list:
...    result = np.all(np.isclose(my_pickle[:, :], states[:, :])) 
...    expected_result = expected_result or result
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
>>> states = eval_timeout_print("get_penguipi_trajectory(initial_state=np.array([1, -1, np.pi/4]), max_t=200, right_rate=10, left_rate=20)") # doctest:+ELLIPSIS
skip ...
>>> pickle_name_list = (["q3_file3.pk"])
>>> pickle_list = enumerate_pickle(pickle_name_list, path = "Practical02_Support/pickle/")
>>> expected_result = False
>>> for my_pickle in pickle_list:
...    result = np.all(np.isclose(my_pickle[:, :], states[:, :])) 
...    expected_result = expected_result or result
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