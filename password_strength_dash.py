# Password Strength Checker - Dash Web App
# Author: Nikita Tapali
# Contact: kynic406@gmail.com
# Date: Dynamic (Auto-updates)

import dash
from dash import dcc, html, Input, Output
import re
from datetime import datetime

app = dash.Dash(__name__)

# Get the current date dynamically
current_date = datetime.now().strftime("%Y-%m-%d")

def check_password_strength(password):
    strength_criteria = [
        (r".{8,}", "✅ Password length is good (at least 8 characters)."),
        (r"[A-Z]", "✅ Contains uppercase letters."),
        (r"[a-z]", "✅ Contains lowercase letters."),
        (r"\d", "✅ Contains numbers."),
        (r"[!@#$%^&*(),.?\":{}|<>]", "✅ Contains special characters."),
    ]

    feedback = []
    passed_checks = 0

    for regex, message in strength_criteria:
        if re.search(regex, password):
            feedback.append(html.P(message, style={"color": "green"}))
            passed_checks += 1
        else:
            feedback.append(html.P("❌ " + message.replace("✅", "Password should"), style={"color": "red"}))

    if passed_checks == len(strength_criteria):
        feedback.append(html.P("✅ Your password is very strong!", style={"color": "green"}))
    else:
        feedback.append(html.P("❌ Weak password. Please improve it.", style={"color": "red"}))

    return feedback

app.layout = html.Div([
    html.H1("🔐 Password Strength Checker - Dash Web App", style={"text-align": "center", "color": "#2c3e50"}),
    html.H3("📌 Author: Nikita Tapali", style={"text-align": "center", "color": "#16a085"}),
    html.H3("📧 Contact: kynic406@gmail.com", style={"text-align": "center", "color": "#16a085"}),
    html.H3(f"📅 Date: {current_date}", style={"text-align": "center", "color": "#16a085"}),
    html.Br(),
    dcc.Input(id="password_input", type="text", placeholder="Enter your password", debounce=True, style={"width": "100%", "padding": "10px", "font-size": "16px"}),
    html.Br(), html.Br(),
    html.Div(id="password_feedback")
])

@app.callback(
    Output("password_feedback", "children"),
    Input("password_input", "value")
)
def update_feedback(password):
    if password:
        return check_password_strength(password)
    return ""

if __name__ == '__main__':
    app.run_server(debug=True)
