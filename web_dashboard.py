"""Simple Flask web dashboard for Auto Apply."""
from flask import Flask, request, render_template_string

from auto_apply import generate_resume, generate_cover_letter
from profile_manager import load_profile

app = Flask(__name__)

INDEX_HTML = """
<!doctype html>
<title>Auto Apply</title>
<h1>Generate Cover Letter</h1>
<form method=post>
  Profile path: <input name=profile value="profile.json"><br>
  Job description:<br>
  <textarea name=jd rows=10 cols=60></textarea><br>
  <input type=submit value=Generate>
</form>
{% if letter %}
<h2>Cover Letter</h2>
<pre>{{ letter }}</pre>
{% endif %}
"""


@app.route("/", methods=["GET", "POST"])
def index():
    letter = None
    if request.method == "POST":
        profile = load_profile(request.form["profile"])
        jd = request.form["jd"]
        letter = generate_cover_letter(jd, profile)
    return render_template_string(INDEX_HTML, letter=letter)


if __name__ == "__main__":
    app.run(debug=True)
