# YouTube Video Summarizer using CrewAI

## Overview

This project leverages **CrewAI**, an advanced multi-agent framework, to automate the process of converting **YouTube video content** into **structured blog articles**. The system uses a specialized **Crew of AI Agents**, each performing dedicated tasks, to ensure quality and coherence in the generated blogs.

The key differentiator of this project is the **hybrid usage of both OpenAI and Gemini models** for optimal results:
- **Transcription generation** is handled by **OpenAI** (gpt-4-turbo or similar)
- **Summary generation** is handled by **Google Gemini** APIs
- Multi-agent collaboration orchestrated via **CrewAI**

## Features

- Multi-Agent orchestration using CrewAI
- YouTube transcript fetching
- Multi-model integration:
  - OpenAI for transcription
  - Gemini (Google) for summarization
- Outputs blog content in markdown format
- Modular codebase: agents, tasks, tools separated for clarity
- Extendable and production-oriented structure
- Rate-limiting, caching, and memory handling via CrewAI configs
- Runs smoothly in environments like **Kaggle**, **Colab**, and **local machines**


---

## ⚙️ .py files structure

1. **Agents Setup** (`agents.py`)  
   Defines specialized agents like the Blog Researcher and Blog Writer with distinct goals and roles.

2. **Tasks Definition** (`tasks.py`)  
   Configures individual tasks like transcript generation and summarization, connecting them to agents.

3. **Tools Integration** (`tools.py`)  
   Provides external tools powered by Gemini and OpenAI for generating YouTube transcripts and summarizing them.

4. **CrewAI Orchestration** (`crew.py`)  
   Brings agents, tasks, and tools together into a cohesive workflow using CrewAI’s orchestration capabilities.

5. **Environment Variables** (`.env`)  
   Stores API keys required for interacting with OpenAI and Gemini APIs securely.

6. **Documentation** (`README.md`)  
   This file—serves as a complete guide to understanding, setting up, and using the project.



## How It Works

1. **YouTube Video Input**:
   - The process begins by providing a video topic or link.

2. **Agent Collaboration**:
   - **Research Agent** uses OpenAI models to transcribe the YouTube video.
   - **Writer Agent** uses Gemini models to summarize and write structured blog content.

3. **Final Output**:
   - The content is generated in markdown format, ready for use in blogs or publications.


