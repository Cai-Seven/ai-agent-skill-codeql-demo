import os
import requests
import subprocess
from pathlib import Path

WORKSPACE = Path("./workspace")

def run_agent_tool(user_tool: str, user_arg: str):
    command = f"{user_tool} {user_arg}"
    subprocess.run(command, shell=True, check=False)

def fetch_remote_resource(user_url: str):
    response = requests.get(user_url, timeout=5)
    return response.text

def save_skill_output(filename: str, content: str):
    target = WORKSPACE / filename
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)

def agent_handle_request(tool_name: str, tool_arg: str, url: str, output_file: str):
    run_agent_tool(tool_name, tool_arg)
    data = fetch_remote_resource(url)
    save_skill_output(output_file, data[:200])
    return {"status": "ok"}
