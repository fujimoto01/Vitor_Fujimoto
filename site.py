from flask import Flask, render_template_string

app = Flask(__name__)

# Replace these variables with seus dados
USER = {
    "name": "Vitor Fujimoto",
    "title": "Statistic undergraduated",
    "bio": "UFPR student, passionate about data science and machine learning. Always eager to learn and share knowledge.",
    "avatar": "https://avatars.githubusercontent.com/u/181305668?s=400&u=23cb75ff18217d9bba1ec01999e76f5a7a572241&v=4",
    "links": [
        {"label": "GitHub", "url": "https://github.com/fujimoto01"}],
}

HTML = """
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ user.name }}</title>
  <style>
    body{font-family:Inter, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;display:flex;min-height:100vh;align-items:center;justify-content:center;background:#0f172a;color:#e6eef8;margin:0}
    .card{background:linear-gradient(180deg,#07102a 0%,#0b1530 100%);padding:36px;border-radius:12px;box-shadow:0 10px 30px rgba(2,6,23,.7);width:min(720px,94vw)}
    .header{display:flex;gap:20px;align-items:center}
    .avatar{width:96px;height:96px;border-radius:16px;object-fit:cover;border:2px solid rgba(255,255,255,.06)}
    h1{margin:0;font-size:1.6rem}
    p.lead{margin:8px 0 18px;color:#9fb0d9}
    .links{display:flex;flex-wrap:wrap;gap:10px}
    .link{background:rgba(255,255,255,.03);padding:10px 14px;border-radius:10px;color:#dbeafe;text-decoration:none;border:1px solid rgba(255,255,255,.04)}
    footer{margin-top:18px;color:#7f93b4;font-size:0.9rem}
    @media (max-width:520px){.header{flex-direction:row}}
  </style>
</head>
<body>
  <div class="card">
    <div class="header">
      <img class="avatar" src="{{ user.avatar }}" alt="avatar">
      <div>
        <h1>{{ user.name }} — <small style="opacity:.8">{{ user.title }}</small></h1>
        <p class="lead">{{ user.bio }}</p>
        <div class="links">
          {% for l in user.links %}
            <a class="link" href="{{ l.url }}" target="_blank" rel="noopener">{{ l.label }}</a>
          {% endfor %}
        </div>
      </div>
    </div>
  </div>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML, user=USER)


if __name__ == "__main__":
    # Rode: python site.py
    app.run(host="0.0.0.0", port=8000, debug=True)
