import os
from dotenv import load_dotenv
# features.py
from langchain_ibm import WatsonxLLM
load_dotenv()
# Retrieve IBM API credentials from environment variables
ibm_key = os.environ["WATSONX_APIKEY"]
ibm_project_id = os.environ.get('PROJECT_ID')
ibm_url = os.environ.get('WATSONX_URL')

parameters = {
    "decoding_method": "sample",
    "max_new_tokens": 300,
    "min_new_tokens": 150,
    "temperature": 1,
    "top_k": 50,
    "top_p": 1,
}

watsonx_llm = WatsonxLLM(
    model_id="ibm/granite-13b-instruct-v2",
    url=ibm_url,
    project_id=ibm_project_id,
    params=parameters,
)
def task_breakdown(task_description):
    response = watsonx_llm.invoke("You are expert AI cook, user will give a dish, and you will give step by step guide to prepare: {task_description}")
    return response

# def generate_project_roadmap(requirements):
#     response = watsonx_model(prompt_template.format(input=f"Generate a project roadmap based on these requirements: {requirements}"))
#     return response

# def code_migration(source_code, target_version):
#     response = watsonx_model(prompt_template.format(input=f"Migrate this code to the new version {target_version}: {source_code}"))
#     return response

# def summarize_issues(issue_data):
#     response = watsonx_model(prompt_template.format(input=f"Summarize these issues and suggest priorities: {issue_data}"))
#     return response

# def summarize_dependencies(dependencies):
#     response = watsonx_model(prompt_template.format(input=f"Analyze and suggest updates for these dependencies: {dependencies}"))
#     return response

# def plan_sprints(progress_data, upcoming_tasks):
#     response = watsonx_model(prompt_template.format(input=f"Generate a sprint plan based on this progress data and upcoming tasks: {progress_data} {upcoming_tasks}"))
#     return response

# def generate_release_notes(commit_messages):
#     response = watsonx_model(prompt_template.format(input=f"Generate release notes from these commit messages: {commit_messages}"))
#     return response

# def identify_technical_debt(source_code):
#     response = watsonx_model(prompt_template.format(input=f"Identify and prioritize areas of technical debt in this codebase: {source_code}"))
#     return response
