import requests

def download_video(url):
  response = requests.get(url)
  file_size = int(response.headers.get("Content-Length", 0))
  filename = url.split("/")[-1]

  with open(filename, "wb") as f:
	  f.write(response.content)

if __name__ == "__main__":
  # Replace this with the URL of the TikTok video you want to download
  video_url = "https://www.tiktok.com/@mdkamin42/video/7165072447190928683?is_from_webapp=1&sender_device=pc"
  download_video(video_url)

## Not working code got from OpenAI