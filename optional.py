
# from pytube import YouTube
# from pytube import Playlist
# from pytube import Channel
# import os

# def playlist(url):
#     playlist = Playlist(url)
#     print('Number of videos in playlist: %s' % len(playlist.video_urls))
#     for video in playlist.videos:
#         video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
#         print("Done !!")

# def video(url):
#     video_caller = YouTube(url)
#     print(video_caller.title)
#     video_caller.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download()
#     print("Done!!")

# def channel(url):
#     channel_videos = Channel(url)
#     print(f'Downloading videos by: {channel_videos.channel_name}')
#     for video in channel_videos.videos:
#         video.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download()
#     print("Done!!")

# def video_voice_only(url):
#     video_caller = YouTube(url)
#     print(video_caller.title)
#     audio = video_caller.streams.filter(only_audio=True).first()
#     out_path = audio.download(output_path=video_caller.title)
#     new_name = os.path.splitext(out_path)
#     os.rename(out_path,new_name[0] + ".mp3")
#     print("Done!!")

# def picture_only(url):
#     video_caller = YouTube(url)
#     print(video_caller.title)
#     video = video_caller.streams.filter(only_video=True).first()
#     out_path = video.download(output_path=video_caller.title)
#     new_name = os.path.splitext(out_path)
#     os.rename(out_path,new_name[0] + ".mp4")
#     print("Done!!")

# if __name__ == "__main__":
#     required = input("Enter playlist to download playlist; video to download a videonchannel to download all videos from a channelnvoice for only voice filenpicture for picture onlyn")
#     if required=="playlist":
#         url = input("Enter the url for whole playlistn")
#         playlist(url=url)
#     elif required=="video":
#         url = input("Enter the url of the videon")
#         video(url=url)
#     elif required=="channel":
#         url = input("Enter the url of the channeln")
#         channel(url=url)
#     elif required == "voice":
#         url = input("Enter the url of the videon")
#         video_voice_only(url)
#     elif required == "picture":
#         url = input("Enter the url of the videon")
#         picture_only(url)    
#     else:
#         print("Invalid")

# 2nd
# from pytube import YouTube

# def download_video(url, resolution='2160p'):
#     try:
#         yt = YouTube(url)
#         streams = yt.streams.filter(res=f'{resolution}').first()
#         if streams:
#             streams.download()
#             print("Video downloaded successfully.")
#         else:
#             print(f"No {resolution} resolution available for the provided URL.")
#     except Exception as e:
#         print(f"Error: {str(e)}")

# if __name__ == "__main__":
#     video_url = input("Enter the YouTube video URL: ")
#     download_video(video_url)

# 3 rd
