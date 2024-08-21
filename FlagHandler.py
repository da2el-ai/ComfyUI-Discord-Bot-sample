import re


def identity(x):
    return [x]


def rev_identity(x):
    return x


def res_spliter(x):
    return x.split(':')


def mapped_value(dict):
    def func(x):
        return [dict[x]]

    return func


def rev_mapped_value(dict):
    def func(x):
        return dict[x]

    return func


class FlagsHandler:

    def __init__(self, regex):
        self._paths_by_flag = {}
        self._funcs_by_flag = {}
        self._descs_by_flag = {}
        self._fetchs_by_flag = {}
        self.FLAG_REGEX = regex

    def set_flags(self, flag_name: str, workflow_paths, description: str = None, convert_func=identity,
                  fetch_func=rev_identity):
        self._paths_by_flag[flag_name] = workflow_paths
        self._funcs_by_flag[flag_name] = convert_func
        self._descs_by_flag[flag_name] = description
        self._fetchs_by_flag[flag_name] = fetch_func

    def get_description(self, flag_name: str) -> str:
        return self._descs_by_flag[flag_name]

    def manipulate_prompt(self, flag_name: str, value: str, prompt):
        results = self._funcs_by_flag[flag_name](value)
        index = 0
        for res in results:
            self._set_value(self._paths_by_flag[flag_name][index], prompt, res)
            index += 1

    def get_values(self, flag_name: str, prompt):
        results = []
        index = 0
        for path in self._paths_by_flag[flag_name]:
            results.append(self._get_value(flag_name, path, prompt))
            index += 1
        return results

    def get_value(self, flag_name: str, prompt):
        for path in self._paths_by_flag[flag_name]:
            return self._get_value(flag_name, path, prompt)
        return None

    def clean_from_flags(self, text):
        return re.sub(self.FLAG_REGEX, '', text).strip()

    def extract_flags(self, text):
        return re.findall(self.FLAG_REGEX, text)

    def _set_value(self, path, prompt, value):
        ref = prompt
        for key in path[:-1]:
            ref = ref[key]
        ref[path[-1]] = value

    def _get_value(self, flag, path, prompt):
        ref = prompt
        for key in path[:-1]:
            ref = ref[key]
        return self._fetchs_by_flag[flag](ref[path[-1]])

