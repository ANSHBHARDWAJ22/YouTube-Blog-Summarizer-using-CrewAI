from crewai_tools import YoutubeChannelSearchTool
import google.generativeai as genai
import os
from dotenv import load_dotenv

# ✅ Load .env and configure Gemini API
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ Tool 1: YouTube Channel Search Tool → Gives video titles, metadata (optional if you only want transcript generation)
yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06')

# ✅ Tool 2: Generate Transcript using Gemini
def yt_tool(topic):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"""
    You are a YouTube Transcript Generator.

    Generate a realistic, detailed YouTube video transcript on the topic: "{topic}".
    Make it educational, engaging, and structured like a real tech YouTube video.
    """
    response = model.generate_content(prompt)
    return response.text

# ✅ Tool 3: Summarizer Tool using Gemini
def summarizer_tool(transcript, topic):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"""
    Summarize the following YouTube video transcript about "{topic}" into a concise, engaging blog post.

    Transcript:
    {transcript}
    """
    response = model.generate_content(prompt)
    return response.text
