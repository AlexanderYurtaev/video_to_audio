from moviepy.editor import VideoFileClip, AudioFileClip


def video_to_audio(cut_start: tuple = None, cut_end: tuple = None):
    """
    Function convert video file to mp3. New file will be created with the same name as video file and in
     the same location.
    :param cut_start: Start time of a new .mp3 file. Should be in format seconds (15.35), in (min, sec),
    in (hour, min, sec). e.g. 15, 20 - means new file will start from 15 min 20 sec of original video file.
    2, 19, 0 - means 2 hour 19 min 0 sec
    :param cut_end: Start time of a new .mp3 file. The same logic as above.
    :return:
    """
    file_location = input("Please enter a full path to file you want to convert to audio: \n")
    parsed_file_path = get_parsed_filepath(file_location)
    video_clip = VideoFileClip(file_location)
    audio_clip = video_clip.audio
    if cut_start is not None and cut_end is not None:
        cut_clip = audio_clip.subclip(cut_start, cut_end)
        cut_clip.write_audiofile(f'{parsed_file_path[0]}{parsed_file_path[1]}.mp3')
    else:
        audio_clip.write_audiofile(f'{parsed_file_path[0]}{parsed_file_path[1]}.mp3')
    video_clip.close()
    audio_clip.close()


def cut_video_audio():
    pass


def get_parsed_filepath(file_path: str) -> list:
    """
    Function return list of the path to file and it's name.
    :param file_path: full path to file, include it's name
    :return: list contain two elements  file path and file name
    """
    slash_index = file_path.rindex('/')
    dot_index = file_path.rindex('.')
    return [file_path[:slash_index + 1], file_path[slash_index + 1:dot_index]]


if __name__ == '__main__':
    video_to_audio((13, 37), (2, 19, 0))
    # video_to_audio()
