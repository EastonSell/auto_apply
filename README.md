# Auto Apply

This repository contains a simple prototype for automatically generating a resume, crafting cover letters for job applications, and writing recruiter outreach messages using the OpenAI API.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and add your OpenAI API key:
   ```bash
   cp .env.example .env
   # Edit .env and set OPENAI_API_KEY
   ```
   The application will automatically load variables from `.env` when run.

## Usage

Run the main script to see sample output:

```bash
python auto_apply.py
```

Cover letters will be written to the `letters` directory when running the
script.

The script demonstrates how to:

- Generate a resume from a dictionary of profile information.
- Create personalized cover letters for multiple job descriptions.
- Compose a short recruiter outreach message.

The `apply_to_jobs` function is a placeholder where integrations with specific job site APIs would go. Currently it only prints the generated cover letter and simulates a submission.
