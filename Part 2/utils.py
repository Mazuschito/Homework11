import json


def load_candidates_from_json():
    with open("candidates.json", encoding="UTF-8") as file:
        list_of_candidates = json.load(file)
    return list_of_candidates


def get_candidate_by_name(candidate_name):
    list_of_candidates = load_candidates_from_json()
    for candidate in list_of_candidates:
        if candidate["name"] == candidate_name:
            return candidate


def search_candidates_by_name(candidate_name):
    same_name_candidates = []
    list_of_candidates = load_candidates_from_json()
    for candidate in list_of_candidates:
        candidate_fullname = candidate["name"].lower()
        candidate_fullname = candidate_fullname.split(" ")
        for name in candidate_fullname:
            if name == candidate_name.lower():
                same_name_candidates.append(candidate)
    return same_name_candidates


def get_candidates_by_skill(skill_name):
    skilled_candidates = []
    list_of_candidates = load_candidates_from_json()
    for candidate in list_of_candidates:
        candidate_skills = candidate["skills"].lower()
        candidate_skills = candidate_skills.split(", ")
        for skill in candidate_skills:
            if skill == skill_name.lower():
                skilled_candidates.append(candidate)
    return skilled_candidates
