import subprocess

from .. enums import POSSIBLE_INPUTS
from .. sys_functions.find_files_in_folder import find_files
from .. sys_functions.read_files import read_xml

def calculate_fibers(inputs):
	print("\n== Calculating fibers ==")
	
	# Get inputs
	file_to_calculate = inputs[POSSIBLE_INPUTS.FEB_NAME]
	geom_d_folder = inputs[POSSIBLE_INPUTS.GEOMETRY_DATA_FOLDER]
	path_o_folder = inputs[POSSIBLE_INPUTS.OUTPUT_FOLDER]
	path_m_folder = inputs[POSSIBLE_INPUTS.PATH_TO_MATLAB_FOLDER]

	# Get avaiable files 
	files = find_files(geom_d_folder,("fileFormat","csv"))

	# Get only needed files (if user did not requested all)
	if file_to_calculate != "all":
		files = [f for f in files if f[1].find(file_to_calculate) != -1]

	nodes_files = [f for f in files if f[1].find("_nodes") != -1 and f[1].find("hex") == -1]
	elems_files = [f for f in files if f[1].find("_elems") != -1 and f[1].find("hex") == -1]
	nodes_files_hex = [f for f in files if f[1].find("_nodes") != -1 and f[1].find("hex") != -1]
	elems_files_hex = [f for f in files if f[1].find("_elems") != -1 and f[1].find("hex") != -1]

	for node_file in nodes_files:
		fname = node_file[2].split("_nodes")[0]

		elem_file = [f for f in elems_files if f[2].split("_elems")[0] == fname][0]

		if len(nodes_files_hex) > 0:
			node_file_hex = [f for f in nodes_files_hex if f[2].split("_elems")[0] == fname][0]
			elem_file_hex = [f for f in elems_files_hex if f[2].split("_elems")[0] == fname][0]
		else:
			node_file_hex = node_file
			elem_file_hex = elem_file

		theta_endo = 75
		theta_epi = -45

		print(node_file[0])
		print(elem_file[0])
		print(node_file_hex[0])
		print(elem_file_hex[0])


		params = "'"+ node_file[0] + "'" + ',' + "'"+ elem_file[0] + "'" + ',' + \
			"'" + node_file_hex[0] + "'" + ',' + "'" + elem_file_hex[0] + "'" + ',' + \
			str(theta_endo) + ',' + str(theta_epi) + ',' + \
			"'" + path_o_folder + "\\" + fname + "'"

		print(params)


		res = subprocess.call([
		"matlab.exe",
		"-wait",
		"-nodisplay",
		"-nojvm",
		"-nosplash",
		"-nodesktop",
		'/r',
		'"cd'+ " '" + path_m_folder + "'; " + "calc_fibers("+params+");" + ' exit"'
		])
		if res != 0:
			print(res)