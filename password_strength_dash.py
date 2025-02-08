import dash
from dash import dcc, html, Input, Output
import re
import dash_bootstrap_components as dbc
import random

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Function to check password strength
def check_password(password):
    feedback = []
    
    if len(password) < 8:
        feedback.append("❌ Password should be at least 8 characters long.")
    else:
        feedback.append("✅ Sufficient length (8+ characters).")
    
    if not re.search(r"[A-Z]", password):
        feedback.append("❌ Password should contain at least one uppercase letter.")
    else:
        feedback.append("✅ Contains uppercase letters.")
    
    if not re.search(r"[a-z]", password):
        feedback.append("❌ Password should contain at least one lowercase letter.")
    else:
        feedback.append("✅ Contains lowercase letters.")
    
    if not re.search(r"\d", password):
        feedback.append("❌ Password should contain at least one number.")
    else:
        feedback.append("✅ Contains numbers.")
    
    if not re.search(r"[@$!%*?&]", password):
        feedback.append("❌ Password should contain at least one special character (@$!%*?&).")
    else:
        feedback.append("✅ Contains special characters.")
    
    if len(feedback) == 5 and feedback.count("✅") == 5:
        feedback.append("✅ Strong password! Well done.")
    else:
        feedback.append("❌ Weak password. Please improve it.")
    
    return feedback

# Function to generate password suggestions
def suggest_password():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@$!%*?&"
    return "".join(random.choice(chars) for _ in range(12))

# Layout of the Dash app
app.layout = dbc.Container([
    html.Div(style={'background': 'linear-gradient(45deg, #ff99cc, #ffcc66)', 'padding': '20px', 'borderRadius': '10px'}, children=[
        html.H1("🔐 Password Strength Checker", className="text-center mt-4 mb-2", style={'color': 'white'}),
        html.H5("📌 Author: Nikita Tapali", className="text-center", style={'color': 'black'}),
        html.H6("📧 Contact: kynic406@gmail.com", className="text-center mb-4", style={'color': 'black'}),
        dbc.Input(id='password-input', type='password', placeholder='Enter a password', className="mb-3"),
        dbc.Checkbox(id='show-password', label='Show Password', className='mb-3'),
        html.Button('Check Password', id='check-button', n_clicks=0, className="btn btn-warning mb-3"),
        html.Div(id='password-feedback', className="mt-2"),
        html.Button('Suggest Strong Password', id='suggest-button', n_clicks=0, className="btn btn-info mb-3"),
        html.Div(id='suggested-password', className="mt-2", style={'font-weight': 'bold', 'color': '#008080'})
    ])
])

# Callback to toggle password visibility
@app.callback(
    Output('password-input', 'type'),
    [Input('show-password', 'value')]
)
def toggle_password_visibility(show_password):
    return 'text' if show_password else 'password'

# Callback to update password feedback
@app.callback(
    Output('password-feedback', 'children'),
    [Input('check-button', 'n_clicks')],
    [Input('password-input', 'value')]
)
def update_feedback(n_clicks, password):
    if n_clicks > 0 and password:
        feedback = check_password(password)
        return html.Div([html.P(point, style={"color": "#32CD32"} if "✅" in point else {"color": "#FF4500"}) for point in feedback])
    return ""

# Callback to suggest strong password
@app.callback(
    Output('suggested-password', 'children'),
    [Input('suggest-button', 'n_clicks')]
)
def suggest_strong_password(n_clicks):
    if n_clicks > 0:
        return f"🔑 Suggested Password: {suggest_password()}"
    return ""

if __name__ == '__main__':
    app.run_server(debug=True)
