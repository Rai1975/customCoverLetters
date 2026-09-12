# Consolidating all tools in one place
import os
import json

def get_experiences():
    path = os.path.join(os.getcwd(), "data/experiences.json")
    with open(path, "r", encoding="utf-8") as f:
        exp = json.load(f)

    formatted_string = "**Experiences**\n"
    count = 1
    for experience in exp:
        formatted_string += f"\n{count}) "
        formatted_string += f"Position: {experience.get('title')}\n\n"
        formatted_string += f"Company: {experience.get('organization')}\n\n"
        formatted_string += f"Description: {experience.get('description')}\n\n"
        formatted_string += f"Duration: {experience.get('date')}\n\n"
        formatted_string += "-"*60
        count += 1

    return formatted_string


def get_coursework():
    path = os.path.join(os.getcwd(), "data/coursework.json")
    with open(path, "r", encoding="utf-8") as f:
        coursework = json.load(f)

    formatted_string = "**Coursework**\n"
    count = 1
    for course in coursework:
        formatted_string += f"\n{count}) "
        formatted_string += f"Title: {course.get('title')}\n\n"
        formatted_string += f"Stack and Course: {course.get('stack')}\n\n"
        formatted_string += f"Description: {course.get('description')}\n\n"
        formatted_string += "-"*60
        count += 1

    return formatted_string

def get_projects():
    path = os.path.join(os.getcwd(), "data/projects.json")
    with open(path, "r", encoding="utf-8") as f:
        projects = json.load(f)

    formatted_string = "**Projects**\n"
    count = 1
    for project in projects:
        formatted_string += f"\n{count}) "
        formatted_string += f"Title: {project.get('title')}\n\n"
        formatted_string += f"Stack and Course: {project.get('stack')}\n\n"
        formatted_string += f"Description: {project.get('description')}\n\n"
        formatted_string += f"Link: {project.get('link')}\n\n"
        formatted_string += "-"*60
        count += 1

    return formatted_string

def get_profile_summary():
    combined_string = ""
    combined_string += "\n\n" + get_experiences()
    combined_string += "\n\n" + get_projects()
    combined_string += "\n\n" + get_coursework()

    return combined_string

if __name__ == "__main__":
    print(get_profile_summary())