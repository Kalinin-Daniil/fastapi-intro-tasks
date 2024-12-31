from fastapi import FastAPI, Form

app = FastAPI()

# BEGIN (write your solution here)
html_form = """
<!DOCTYPE html>
<html>
    <head>
        <title>User Login</title>
    </head>
    <body>
        <h2>User Login</h2>
        <form action="/login" method="post">
            <label for="username">Username:</label><br>
            <input type="text" id="username" name="username" required><br><br>
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password" required><br><br>
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
"""

@app.get("/")
async def read_form():
    return html_form

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    return {
        "username": username,
        "password": password,
        "status": "Login successful"
    }
# END
