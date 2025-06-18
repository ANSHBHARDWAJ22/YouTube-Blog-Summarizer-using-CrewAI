from crewai import Agent
from dotenv import load_dotenv
import os
import google.generativeai as genai

# ✅ Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ Gemini-based YouTube Transcript Tool
def yt_tool(topic):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"""
    You are a YouTube Transcript Generator.

    Generate a detailed, realistic YouTube video transcript about the topic: "{topic}".
    Make it educational, engaging, and structured like a real YouTube video script.
    """
    response = model.generate_content(prompt)
    return response.text

# ✅ Gemini-based Summarizer Tool
def summarizer_tool(transcript, topic):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"""
    Summarize the following transcript in a concise, engaging way for a blog audience.
    Focus on explaining the key concepts of "{topic}".

    Transcript:
    {transcript}
    """
    response = model.generate_content(prompt)
    return response.text

# ✅ Blog Researcher Agent → Generates transcript (using Gemini)
blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    goal='Get the relevant video transcription for the topic {topic}.',
    verbose=True,  # DEBUG OUTPUT ON (fix typo from your code → verboe → verbose)
    memory=True,
    backstory="Expert in understanding videos in AI, Data Science, Machine Learning, and GenAI topics.",
    tools=[yt_tool],  # Gemini used via yt_tool
    allow_delegation=True
)

# ✅ Blog Writer Agent → Summarizes the transcript (also using Gemini under the hood)
blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from the YT transcript.',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging narratives "
        "that captivate and educate, bringing new discoveries to light in an accessible manner."
    ),
    tools=[summarizer_tool],  # Gemini summarizer tool
    allow_delegation=False
)

# ✅ Example run: Fetch transcript → Summarize → Print both
if __name__ == "__main__":
    topic = "What is Generative AI?"

    print(f"🔹 Generating YouTube transcript for: {topic}")
    transcript = yt_tool(topic)
    print("✅ Transcript generated!\n")

    print("🔹 Generating summary for blog...")
    summary = summarizer_tool(transcript, topic)
    print("✅ Summary generated!\n")

    print("📌 FINAL SUMMARY:\n")
    print(summary)
