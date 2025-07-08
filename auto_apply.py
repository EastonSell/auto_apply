import os
import json
from typing import List
import openai
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

# Ensure the OpenAI API key is set in environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY environment variable not set")
openai.api_key = OPENAI_API_KEY

SYSTEM_PROMPT = "You are a helpful assistant that creates resumes and cover letters for job applicants." 


def generate_resume(profile: dict) -> str:
    """Generate a resume using the OpenAI API given a profile dictionary."""
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Create a concise professional resume for the following profile:\n{json.dumps(profile, indent=2)}"},
    ]
    response = openai.chat.completions.create(model="gpt-4-turbo", messages=messages)
    return response.choices[0].message.content.strip()


def generate_cover_letter(job_description: str, profile: dict) -> str:
    """Generate a cover letter for a given job description."""
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": (
                "Write a short personalized cover letter targeting the following job "
                f"description:\n{job_description}\n\nApplicant details:\n{json.dumps(profile, indent=2)}"
            ),
        },
    ]
    response = openai.chat.completions.create(model="gpt-4-turbo", messages=messages)
    return response.choices[0].message.content.strip()


def message_recruiter(recruiter_name: str, profile: dict) -> str:
    """Generate a recruiter outreach message."""
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": (
                f"Write a short friendly message to recruiter {recruiter_name} "
                f"introducing the applicant described here:\n{json.dumps(profile, indent=2)}"
            ),
        },
    ]
    response = openai.chat.completions.create(model="gpt-4-turbo", messages=messages)
    return response.choices[0].message.content.strip()


def apply_to_jobs(job_descriptions: List[str], profile: dict, output_dir: str | None = None) -> None:
    """Generate cover letters and optionally save them to files."""
    for idx, jd in enumerate(job_descriptions, 1):
        letter = generate_cover_letter(jd, profile)
        print("\n=== Generated Cover Letter ===")
        print(letter)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            path = os.path.join(output_dir, f"cover_letter_{idx}.txt")
            with open(path, "w") as f:
                f.write(letter)
        # Placeholder for actual API call to submit application
        print("[Simulated] Application submitted for job\n")


def main() -> None:
    sample_profile = {
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "skills": ["Python", "Data Analysis", "Machine Learning"],
        "experience": [
            {"company": "Example Corp", "role": "Data Scientist", "years": 2},
            {"company": "Acme Inc", "role": "Data Analyst", "years": 1},
        ],
    }

    resume = generate_resume(sample_profile)
    print("Generated Resume:\n", resume)

    job_descriptions = [
        "Data Scientist role focusing on predictive analytics and model deployment.",
        "ML Engineer position working with deep learning models and production pipelines.",
    ]

    apply_to_jobs(job_descriptions, sample_profile, output_dir="letters")

    recruiter_message = message_recruiter("Alex", sample_profile)
    print("Recruiter Message:\n", recruiter_message)


if __name__ == "__main__":
    main()
