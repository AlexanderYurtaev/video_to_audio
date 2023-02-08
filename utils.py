def get_parsed_filepath(file_path: str) -> list:
    """
    Function return list of the path to file and it's name.
    :param file_path: full path to file, include it's name
    :return: list contain two elements  file path and file name
    """

    slash_index = file_path.rindex('/')
    dot_index = file_path.rindex('.')
    return [file_path[:slash_index + 1], file_path[slash_index + 1:dot_index]]
