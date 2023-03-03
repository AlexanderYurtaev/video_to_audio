import os
from moviepy.editor import VideoFileClip, AudioFileClip
from utils import get_parsed_filepath, download_from_youtube



def video_to_audio(video_location: str, cut_start=0, cut_end=None, youtube: bool = False):
    """
    Function convert video file to mp3. New file will be created with the same name as video file and in
     the same location.
    :param cut_start: Start time of a new .mp3 file. Should be in format seconds (15.35), in (min, sec),
    in (hour, min, sec). e.g. 15, 20 - means new file will start from 15 min 20 sec of original video file.
    2, 19, 0 - means 2 hour 19 min 0 sec.
    :param cut_end: Start time of a new .mp3 file. The same logic as above.
    :param youtube: is Youtube - source of file which should be converted?
    :return:
    """
    if 'https://www.youtube' in video_location or 'https://youtu' in video_location:
        video_location = download_from_youtube(video_location)
        youtube = True

    parsed_file_path = get_parsed_filepath(video_location)
    file_path = parsed_file_path[0]
    file_name = parsed_file_path[1]

    video_clip = VideoFileClip(video_location)
    audio_clip = video_clip.audio
    nbytes = 2

    if cut_start != '' or cut_end != '':
        cut_clip = audio_clip.subclip(cut_start, cut_end)
        cut_clip.write_audiofile(f'{file_path}{file_name}.mp3', nbytes=4)
    else:
        audio_clip.write_audiofile(f'{file_path}{file_name}.mp3', nbytes=4)

    video_clip.close()
    audio_clip.close()

    if youtube:
        os.remove(video_location)

    saved_file_path = f'{file_path}{file_name}.mp3'
    return saved_file_path


def cut_audio_file(audio_location: str, cut_start=0, cut_end=None, mode='crop'):
    parsed_file_path = get_parsed_filepath(audio_location)
    file_path = parsed_file_path[0]
    file_name = parsed_file_path[1]

    audio_clip = AudioFileClip(audio_location)
    match mode:
        case 'crop':
            cut_clip = audio_clip.subclip(cut_start, cut_end)
            cut_clip.write_audiofile(f'{file_path}{file_name}(1).mp3')
        case 'cut':
            cut_clip = audio_clip.cutout(cut_start, cut_end)
            cut_clip.write_audiofile(f'{file_path}{file_name}(1).mp3')

    audio_clip.close()

    saved_file_path = f'{file_path}{file_name}(1).mp3'
    return saved_file_path


def download_video_from_youtube(video_location: str, func):
    if 'https://www.youtube' in video_location or 'https://youtu' in video_location:
        print('funcs here')
        video_location = download_from_youtube(video_location, func)
    else:
        print('Incorrect URI')

    parsed_file_path = get_parsed_filepath(video_location)
    file_path = parsed_file_path[0]
    file_name = parsed_file_path[1]

    video_clip = VideoFileClip(video_location)
    video_clip.close()

    saved_file_path = f'{file_path}{file_name}.mp4'
    return saved_file_path

