from mcp.server.fastmcp import FastMCP
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, VideoUnavailable
from youtube_transcript_api.formatters import TextFormatter, JSONFormatter

mcp = FastMCP("youtube-transcripts")

def get_youtube_transcript(video_id: str, lang_code: str = 'en', format: str = 'json') -> str:
  """
  Retrieve the transcript of a YouTube video in the specified language and format.
  """
  
  # Validate input types
  if not isinstance(video_id, str):
    raise ValueError("The video_id must be a string.")
  if not isinstance(lang_code, str):
    raise ValueError("The lang_code must be a string.")
  if not isinstance(format, str) or format not in ['text', 'json']:
    raise ValueError("The format must be either 'text' or 'json'.")

  try:
    # Attempt to retrieve the transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang_code])

    # Initialize the appropriate formatter
    if format == 'text':
      formatter = TextFormatter()
      return formatter.format_transcript(transcript)
    else:
      formatter = JSONFormatter()
      return formatter.format_transcript(transcript)

  except VideoUnavailable:
    raise ValueError(f"The video with ID '{video_id}' is unavailable.")
  except TranscriptsDisabled:
    raise ValueError(f"Transcripts are disabled for the video with ID '{video_id}'.")
  except Exception as e:
    raise ValueError(f"An error occurred while fetching the transcript: {e}")
  

@mcp.tool()
def fetch_youtube_transcript(video_id: str, lang_code: str = 'en', format: str = 'json') -> str:
  """
  Tool to fetch the transcript of a YouTube video.

  :param video_id: The unique identifier of the YouTube video.
  :param lang_code: The language code for the transcript (default is 'en' for English).
  :param format: The desired output format of the transcript; either 'text' or 'json'.
  :return: The transcript in the specified format.
  """
  return get_youtube_transcript(video_id, lang_code, format)

if __name__ == "__main__":
  mcp.run()