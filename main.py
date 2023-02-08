from moviepy.editor import *


# file_location = '/Users/aleksandr/Downloads/Архив с ютуба/Собеседование Python. Разбор вопросов.mp4'
def video_to_audio():
    file_location = input("Please enter a full path to file you want to convert to audio.")
    print(f'file location is: {file_location}')
    converted_file_name = create_converted_filename(file_location)
    print(converted_file_name)
    audioclip = AudioFileClip(file_location)
    audioclip.write_audiofile(converted_file_name)


def create_converted_filename(file_path: str) -> str:
    slash_index = file_path.rindex('/')
    dot_index = file_path.rindex('.')
    return file_path[slash_index + 1:dot_index]

# if __name__ == '__main__':
video_to_audio()