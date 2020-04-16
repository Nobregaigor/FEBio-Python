
from os.path import join
from .possible_commands import POSSIBLE_COMMANDS, POSSIBLE_INPUTS
import pathlib

OUTPUT_FOLDER_DEFAULT_KEY = hash("OUTPUT_FOLDER")

STORAGE_DIR = join("Active","storage")
WORKING_DIR = pathlib.Path().absolute()

PATH_TO_STORAGE = join(WORKING_DIR.parents[0], STORAGE_DIR)


INPUT_DEFAULTS = {
	POSSIBLE_COMMANDS.ADD_PROPERTIES: {
		POSSIBLE_INPUTS.INPUT_FOLDER: join(PATH_TO_STORAGE,"raw"),
		POSSIBLE_INPUTS.PROPERTIES_FOLDER: join(PATH_TO_STORAGE,"properties"),
		POSSIBLE_INPUTS.OUTPUT_FOLDER: join(PATH_TO_STORAGE,"with_properties"),
		POSSIBLE_INPUTS.SELECTED_PROPERTIES: "all"
	},
	POSSIBLE_COMMANDS.CREATE_LOADCURVE: {
		POSSIBLE_INPUTS.CURVE_FOLDER: join(PATH_TO_STORAGE,"loads"),
		POSSIBLE_INPUTS.CURVE_TYPE: "smooth",
	},
	POSSIBLE_COMMANDS.ADD_LOAD: {
		POSSIBLE_INPUTS.INPUT_FOLDER: join(PATH_TO_STORAGE,"with_properties"),
		POSSIBLE_INPUTS.OUTPUT_FOLDER: join(PATH_TO_STORAGE,"with_load"),
		POSSIBLE_INPUTS.LOAD_FOLDER: join(PATH_TO_STORAGE,"loads"),
		POSSIBLE_INPUTS.LOAD_NAME: "endocardio",
		POSSIBLE_INPUTS.LOAD_ATTRS: None,
	},
	POSSIBLE_COMMANDS.EXTRACT_GEOMETRY_DATA: {
		POSSIBLE_INPUTS.INPUT_FOLDER: join(PATH_TO_STORAGE,"raw"),
		POSSIBLE_INPUTS.OUTPUT_FOLDER: join(PATH_TO_STORAGE,"geometry_data"),
	},
	POSSIBLE_COMMANDS.CALCULATE_FIBERS: {
		POSSIBLE_INPUTS.FEB_NAME: "all",
		POSSIBLE_INPUTS.GEOMETRY_DATA_FOLDER: join(PATH_TO_STORAGE,"geometry_data"),
		POSSIBLE_INPUTS.OUTPUT_FOLDER: join(PATH_TO_STORAGE,"fibers_data"),
		POSSIBLE_INPUTS.PATH_TO_MATLAB_FOLDER: join(WORKING_DIR, "matlab_functions")
	},
	POSSIBLE_COMMANDS.ADD_FIBERS: {
		POSSIBLE_INPUTS.INPUT_FOLDER: join(PATH_TO_STORAGE, "with_properties"),
		POSSIBLE_INPUTS.FIBERS_DATA_FOLDER: join(PATH_TO_STORAGE, "fibers_data"),
		POSSIBLE_INPUTS.OUTPUT_FOLDER: join(PATH_TO_STORAGE,"with_fibers")
	},
	POSSIBLE_COMMANDS.PREPARE: {
		POSSIBLE_INPUTS.INPUT_FOLDER: join(PATH_TO_STORAGE, "raw"),
		POSSIBLE_INPUTS.OUTPUT_FOLDER: join(PATH_TO_STORAGE,"with_fibers")
	},


}



