import re
import dash
from dash import dcc, html, Input, Output

app = dash.Dash(__name__)

def password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("❌ At least 8 characters required.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("❌ Include at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("❌ Include at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("❌ Include at least one number.")

    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        strength += 1
    else:
        feedback.append("❌ Include at least one special character.")

    if strength == 5:
        feedback.append("✅ Your password is very strong!")
    elif strength == 4:
        feedback.append("✅ Your password is strong.")
    elif strength == 3:
        feedback.append("⚠️ Your password is average. Consider adding more complexity.")
    else:
        feedback.append("❌ Weak password. Improve it using the guidelines.")

    return html.Ul([html.Li(msg) for msg in feedback])

app.layout = html.Div([
    html.H1("Password Strength Checker"),
    dcc.Input(id="password", type="password", placeholder="Enter your password", debounce=True),
    html.Div(id="output")
])

@app.callback(
    Output("output", "children"),
    Input("password", "value")
)
def update_output(password):
    if password:
        return password_strength(password)
    return ""

if __name__ == "__main__":
    app.run_server(debug=True)

