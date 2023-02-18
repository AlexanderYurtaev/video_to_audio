import os
from moviepy.editor import VideoFileClip, AudioFileClip
from utils import get_parsed_filepath, download_from_youtube


def video_to_audio(video_location: str, cut_start: tuple = None, cut_end: tuple = None, youtube: bool = False):


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
