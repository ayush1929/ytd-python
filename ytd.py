from pytube import YouTube
import subprocess
import os

def download_music_video(url, resolution='1080p'):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(res=f'{resolution}').first()
        audio_stream = yt.streams.get_audio_only()
        
        if video_stream and audio_stream:
            video_file = video_stream.download(output_path='.', filename='video')
            audio_file = audio_stream.download(output_path='.', filename='audio')

            ffmpeg_path = r'C:\ffmpeg\bin\ffmpeg.exe'  # Specify the full path to ffmpeg.exe
            output_file = f"{os.path.splitext(video_file)[0]}_merged.mp4"
            
            # Use subprocess to execute ffmpeg command
            subprocess.run([ffmpeg_path, '-i', video_file, '-i', audio_file, '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental', output_file], check=True)
            
            # Remove temporary files
            os.remove(video_file)
            os.remove(audio_file)

            print("Music video downloaded successfully.")
        else:
            print(f"No {resolution} resolution available for the provided URL or no audio stream available.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_music_video(video_url)



