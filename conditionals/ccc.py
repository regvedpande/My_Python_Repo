# Define a variable for the completeness score of a portfolio project
project_completeness_score = 95 # You mentioned your ATS score was 95, let's use that as an example

# Conditional statements to categorize the project
if project_completeness_score == 100:
  project_status = "Fully Complete and Polished"
elif project_completeness_score >= 90:
  project_status = "Almost Ready - Needs Final Review"
elif project_completeness_score >= 70:
  project_status = "In Good Shape - Minor Additions/Fixes Needed"
elif project_completeness_score >= 50:
  project_status = "In Progress - Core Functionality Built"
else:
  project_status = "Early Stages - Needs Significant Work"

# Print the status of the project
print(f"Portfolio Project Status: {project_status}")

# Another example based on your job application efforts
# (using the information from your previous message)
days_spent_building_portfolio = 16
applied_to_jobs = False # Based on "without applying to jobs"

if days_spent_building_portfolio > 14 and not applied_to_jobs:
  print("You've dedicated significant time to building your portfolio. That's great groundwork!")
  print("Next step could be to start applying for jobs with your strong portfolio.")
elif applied_to_jobs:
  print("Good luck with your job applications!")
else:
  print("Keep up the great work on your portfolio!")

