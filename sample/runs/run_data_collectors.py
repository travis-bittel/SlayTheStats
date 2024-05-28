import json
import os


def all_runs_in_folder(path: str) -> [dict]:
    all_runs = []
    run_files = os.listdir(path)
    for run_file in run_files:
        file_contents = open(os.path.join(path, run_file), 'r').read()
        all_runs.append(json.loads(file_contents))
    return all_runs
