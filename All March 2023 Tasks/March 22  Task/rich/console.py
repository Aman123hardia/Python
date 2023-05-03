from rich.console import Console

console = Console()


def merge_dict(dict_one, dict_two):
    merged_dict = dict_one or dict_two
    console.log(merged_dict, log_locals=False)


merge_dict({'id': 1}, {'name': 'Ashutosh'})