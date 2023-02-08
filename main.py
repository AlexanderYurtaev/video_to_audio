from moviepy.editor import VideoFileClip, AudioFileClip


def video_to_audio():
    file_location = input("Please enter a full path to file you want to convert to audio: \n")
    converted_file_name = create_converted_filename(file_location)[1]
    file_location = create_converted_filename(file_location)[0]
    print(converted_file_name)
    print(file_location)
    video_clip = VideoFileClip(file_location)
    video_clip.close()
    audio_clip = video_clip.audio
    # audio_clip.write_audiofile(f'{converted_file_name}.mp3')
    audio_clip.close()


def create_converted_filename(file_path: str) -> list:
    slash_index = file_path.rindex('/')
    dot_index = file_path.rindex('.')
    return [file_path[:slash_index+1], file_path[slash_index + 1:dot_index]]


# if __name__ == '__main__':
video_to_audio()
