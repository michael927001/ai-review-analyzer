## Live Deployment (Google Cloud Run)

The AI Review Analyzer backend is fully deployed on Google Cloud Run.

**Base URL:**  
https://ai-review-analyzer-689130222700.us-central1.run.app

**Available Endpoints:**
- `/` → Returns a status message confirming the API is running  
- `/health` → Health check endpoint  
- `/upload` → Accepts a CSV file of reviews and returns the total row count + a sample  

---





AI Review Analyzer

An AI-powered web application that automatically collects and analyzes Google and Yelp business reviews. The goal is to give small business owners quick, actionable insights by summarizing sentiment, extracting recurring themes, and generating improvement recommendations.

 Project Purpose

Small business owners often don’t have time to read hundreds of customer reviews. This tool automates that process using AI, allowing users to instantly understand customer trends and pain points.

 Core Features

CSV or API-based review ingestion

AI-powered sentiment analysis

Extraction of top complaints and praises

Keyword frequency and trend detection

Clean dashboard of insights

Optional PDF report export

 Technology Stack

Frontend: HTML/CSS/JS or React
Backend: Python (Flask or FastAPI)
Database: SQLite (MVP) or Firestore
AI Integration: OpenAI / Gemini API
Containerization: Docker
CI/CD: GitHub Actions
Deployment: Google Cloud Run

 Repo Contents

This repository will include:

Backend API code

Frontend interface

AI analysis logic

Docker configuration

Tests + CI/CD workflows

Documentation

 Project Planning & Documentation

Jira for epics, user stories, sprint planning

Confluence for project overview and linked documentation
