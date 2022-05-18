from flask import Flask, request, render_template
from utils import load_candidates_from_json, get_candidate_by_name, search_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def main_page():
    candidates = load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<name>")
def candidate(name):
    candidate = get_candidate_by_name(name)
    return render_template("single.html", candidate=candidate)


@app.route("/search/")
def search():
    name = request.args.get("name_search")
    candidates = search_candidates_by_name(name)
    qty_of_candidates = len(candidates)
    return render_template("search.html", candidates=candidates, qty_of_candidates=qty_of_candidates)


@app.route("/skill/")
def skill():
    skill = request.args.get("skill_search")
    candidates = get_candidates_by_skill(skill)
    qty_of_candidates = len(candidates)
    return render_template("skill.html", candidates=candidates, qty_of_candidates=qty_of_candidates, skill=skill)


app.run()
