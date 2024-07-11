# argparse
import argparse
import json
import sys

from je_api_testka import create_project_dir
from je_api_testka.utils.exception.exception_tags import argparse_get_wrong_data
from je_api_testka.utils.exception.exceptions import APITesterExecuteException
from je_api_testka.utils.executor.action_executor import execute_action
from je_api_testka.utils.executor.action_executor import execute_files
from je_api_testka.utils.file_process.get_dir_file_list import get_dir_files_as_list
from je_api_testka.utils.json.json_file.json_file import read_action_json

if __name__ == "__main__":
    try:
        def preprocess_read_json_file_execute_action(file_path: str):
            execute_action(read_action_json(file_path))


        def preprocess_read_json_files_execute_files(file_path: str):
            execute_files(get_dir_files_as_list(file_path))


        def preprocess_read_str_execute_action(execute_str: str):
            if sys.platform in ["win32", "cygwin", "msys"]:
                json_data = json.loads(execute_str)
            execute_str = json.loads(json_data)
            execute_action(execute_str)


        argparse_event_dict = {
            "execute_file": preprocess_read_json_file_execute_action,
            "execute_dir": preprocess_read_json_files_execute_files,
            "execute_str": preprocess_read_str_execute_action,
            "create_project": create_project_dir
        }

        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-e", "--execute_file",
            type=str, help="choose action file to execute"
        )
        parser.add_argument(
            "-d", "--execute_dir",
            type=str, help="choose dir include action file to execute"
        )
        parser.add_argument(
            "--execute_str",
            type=str, help="execute json str"
        )
        parser.add_argument(
            "-c", "--create_project",
            type=str, help="create project with template"
        )
        args = parser.parse_args()
        args = vars(args)
        for key, value in args.items():
            if value is not None:
                argparse_event_dict.get(key)(value)
        if all(value is None for value in args.values()):
            raise APITesterExecuteException(argparse_get_wrong_data)
    except Exception as error:
        print(repr(error), file=sys.stderr)
        sys.exit(1)
