from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

# ✅ Create the Crew
crew = Crew(
    agents=[blog_researcher, blog_writer],  # Blog Researcher + Writer agents
    tasks=[research_task, write_task],      # Research first → then summarize/write
    process=Process.sequential,             # Sequential execution (default)
    memory=True,                           # Remember context between tasks
    cache=True,                            # Cache previous results (can save cost/time)
    max_rpm=100,                           # Max requests per minute (adjust as needed)
    share_crew=True                        # Useful for collaboration/debugging in web UIs
)

if __name__ == "__main__":
    topic = 'AI vs ML vs DL vs Data Science'

    # ✅ Kick off the execution
    print(f"\n🚀 Starting blog creation process for topic: '{topic}'\n")

    result = crew.kickoff(inputs={"topic": topic})

    print("\n✅ Final Blog Output:\n")
    print(result)
