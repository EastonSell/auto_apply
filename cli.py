# Command Line Interface for auto_apply
import argparse
from typing import Optional

from auto_apply import generate_resume, generate_cover_letter, message_recruiter, apply_to_jobs
from profile_manager import load_profile, save_profile
from job_scraper import scrape_job_descriptions
from application_tracker import ApplicationTracker
from templates import RESUME_TEMPLATES, COVER_LETTER_TEMPLATES
from error_handler import handle_error


def main() -> None:
    parser = argparse.ArgumentParser(description="Auto Apply CLI")
    parser.add_argument("profile", help="Path to profile JSON file")
    args = parser.parse_args()

    try:
        profile = load_profile(args.profile)
    except FileNotFoundError:
        print("Profile not found. Creating a new one.")
        profile = save_profile(args.profile)

    tracker = ApplicationTracker()

    while True:
        print("\n=== Auto Apply ===")
        print("1. Generate Resume")
        print("2. Generate Cover Letter")
        print("3. Message Recruiter")
        print("4. Scrape Jobs")
        print("5. Apply to Jobs")
        print("6. View Applications")
        print("0. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            resume = generate_resume(profile)
            template = RESUME_TEMPLATES.get("default", "{content}")
            print(template.format(content=resume))
        elif choice == "2":
            jd = input("Enter job description: ")
            letter = generate_cover_letter(jd, profile)
            template = COVER_LETTER_TEMPLATES.get("default", "{content}")
            print(template.format(content=letter))
        elif choice == "3":
            recruiter = input("Recruiter name: ")
            print(message_recruiter(recruiter, profile))
        elif choice == "4":
            query = input("Job search query: ")
            jobs = scrape_job_descriptions(query)
            for j in jobs:
                print("-", j)
        elif choice == "5":
            job = input("Job description: ")
            apply_to_jobs([job], profile)
            tracker.add_application(job)
        elif choice == "6":
            for app in tracker.list_applications():
                print(app)
        elif choice == "0":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        handle_error(e)
