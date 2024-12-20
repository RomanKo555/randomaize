import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

@app.head("/", response_class=HTMLResponse)
def get_random_number():
    random_number = random.randint(1, 6)
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Random Number</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #f0f0f0, #d9d9d9);
            }}
            .container {{
                text-align: center;
                background: #fff;
                padding: 20px 40px;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
            .number {{
                font-size: 48px;
                font-weight: bold;
                color: #333;
            }}
            .message {{
                font-size: 20px;
                margin-top: 10px;
                color: #666;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="message">Візьми своє число від 1 до 6</div>
            <div class="message">Лабораторна робота №2</div>
            <div class="number">{random_number}</div>
        </div>
    </body>
    </html>
    """
    return html_content


@app.get("/", response_class=HTMLResponse)
def get_random_number():
    random_number = random.randint(1, 6)
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Random Number</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #f0f0f0, #d9d9d9);
            }}
            .container {{
                text-align: center;
                background: #fff;
                padding: 20px 40px;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
            .number {{
                font-size: 48px;
                font-weight: bold;
                color: #333;
            }}
            .message {{
                font-size: 20px;
                margin-top: 10px;
                color: #666;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="message">Візьми своє число від 1 до 6</div>
            <div class="message">Лабораторна робота №2</div>
            <div class="number">{random_number}</div>
        </div>
    </body>
    </html>
    """
    return html_content

# if __name__ == "__main__":
#     port = 46038
#     host = "127.0.0.1"
#     print(f"Starting server on {host}:{port}")
#     uvicorn.run(app, host=host, port=port)
