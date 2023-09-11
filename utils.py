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


# def download_from_youtube(uri: str, func, output_type: str = 'Video', path_to_save: str = None):
def download_from_youtube(uri: str, output_type: str = 'Video', path_to_save: str = None):
    print('utils here')
    # video = YouTube(uri, on_progress_callback=func)
    video = YouTube(uri)
    print('utils after')
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


# def progress_func(streams, chunk: bytes, bytes_remaining: int):
#     content_size = streams.filesize
#     # size = contentsize - bytes_remaining
#     # global progress
#     progress = (abs(bytes_remaining-content_size))*100//content_size
#     # video_to_audio_main.my_progress = progress
#     # print(my_progress)
#     # self.progress_bar.setValue(utils.progress)
#     print(progress)

