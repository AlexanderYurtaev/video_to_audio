from pytube import YouTube
import os


def get_parsed_filepath(file_path: str) -> list:
    """
    Function return list of the path to file and it's name.
    :param file_path: full path to file, include it's name
    :return: list contain two elements  file path and file name
    """

    slash_index = file_path.rindex('/')
    dot_index = file_path.rindex('.')
    return [file_path[:slash_index + 1], file_path[slash_index + 1:dot_index]]


def download_from_youtube(uri: str, output_type: str = 'Video', path_to_save: str = None):
    video = YouTube(uri)
    # try:
    #     video = YouTube(uri)
    # except Exception as ex:
    #     print(f'FAILED TO DOWNLOAD VIDEO! Check that URL is correct.\nError occured: {ex}')

    file_name = video.streams.get_highest_resolution().title
    file_extension = video.streams.get_highest_resolution().subtype
    full_name = f'{file_name}.{file_extension}'
    path_to_save = f'{os.path.expanduser("~")}/Downloads'

    # vd1080 = video.streams.filter()
    # for i in vd1080:
    #     print(i)
    # print('\n')
    # video.streams.get_by_resolution('1080p').download(output_path=path_to_save, filename=full_name)
    # video.streams.get_by_itag(299).download(output_path=path_to_save, filename=full_name)
    video.streams.get_highest_resolution().download(output_path=path_to_save, filename=full_name)

    return f'{path_to_save}/{file_name}.{file_extension}'
