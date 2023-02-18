import os
from moviepy.editor import VideoFileClip, AudioFileClip
from utils import get_parsed_filepath, download_from_youtube


def video_to_audio(cut_start: tuple = None, cut_end: tuple = None, youtube: bool = False):
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

    video_location = input("Please enter a full path to file you want to convert to audio: \n")

    if 'https://youtu' in video_location:
        video_location = download_from_youtube(video_location)
        youtube = True

    parsed_file_path = get_parsed_filepath(video_location)
    file_path = parsed_file_path[0]
    file_name = parsed_file_path[1]

    video_clip = VideoFileClip(video_location)
    audio_clip = video_clip.audio

    if cut_start is not None and cut_end is not None:
        cut_clip = audio_clip.subclip(cut_start, cut_end)
        cut_clip.write_audiofile(f'{file_path}{file_name}.mp3')
    else:
        audio_clip.write_audiofile(f'{file_path}{file_name}.mp3')

    video_clip.close()
    audio_clip.close()

    if youtube:
        os.remove(video_location)


def cut_video_audio():
    pass


if __name__ == '__main__':
    video_to_audio()
