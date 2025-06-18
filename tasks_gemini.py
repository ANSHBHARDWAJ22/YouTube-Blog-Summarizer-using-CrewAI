from crewai import Task
from tools import yt_tool, summarizer_tool
from agents import blog_researcher, blog_writer

# ✅ Research Task → Generates transcript from YouTube video (Gemini under the hood)
research_task = Task(
    description=(
        "Research and generate a detailed YouTube video transcript about the topic: {topic}."
    ),
    expected_output=(
        "A comprehensive, realistic 3-paragraph transcript based on the topic '{topic}'. "
        "It should sound like a YouTube video explaining this topic in detail."
    ),
    tools=[yt_tool],   # Gemini transcript generation tool
    agent=blog_researcher,
)

# ✅ Writing Task → Summarizes the transcript into a blog post (Gemini under the hood)
write_task = Task(
    description=(
        "Summarize the generated YouTube video transcript on the topic '{topic}' "
        "into an engaging, well-structured blog post."
    ),
    expected_output=(
        "A concise, blog-ready summary of the key points from the video about '{topic}'. "
        "The summary should be easy to understand, professional, and engaging."
    ),
    tools=[summarizer_tool],   # Gemini summarizer tool
    agent=blog_writer,
    async_execution=False,     # Synchronous execution: First research_task → then write_task
    output_file='new-blog-post.md'  # ✅ Output file where blog content will be saved
)
