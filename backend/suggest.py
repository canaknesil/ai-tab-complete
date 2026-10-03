#!/usr/bin/env python3

import json, urllib.request
import sys
import subprocess

def query(prompt, host, port, model):
    body = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": False,
        "keep_alive": "30m",
        "options": {"temperature": 0, "num_predict": 64, "stop": ["```\n"]},
    }).encode()
    req = urllib.request.Request(
        f"http://{host}:{port}/api/generate",
        data=body,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["response"].strip()

    
PREPROMPT = """You convert English descriptions, broken shell commands, or combination of those into one correct bash command for Linux.

Rules: Output the command only. No explanation. The output should be in the following format:
```bash
<one liner command>
```

Input: {text}
Command:"""

def suggest(prompt, host, port, model):
    prompt_with_context = PREPROMPT.format(text=prompt)
    ret = query(prompt_with_context, host, port, model)
    #print(ret)
    
    lines = ret.splitlines()
    if len(lines) < 3:
        raise Exception("Model response format is wrong: Number of lines less 3.")
    elif len(lines) > 7:
        raise Exception("Model response format is wrong: Number of lines greater than 7.")
    elif lines[0].strip() != "```bash":
        raise Exception("Model response format is wrong: First line isn't '```bash'.")
    elif lines[-1].strip() != "```":
        raise Exception("Model response format is wrong: Last line isn't '```'.")
    
    return lines[1].strip()

host = "127.0.0.1"
port = 11435
model = "qwen2.5-coder:3b"

prompt = ' '.join(sys.argv[1:])
#print(prompt)

cmd = suggest(prompt, host, port, model)
print(cmd)

exec_in_python = False
if exec_in_python:
    answer = input("Execute? (y/n): ").lower()
    if answer == "y":
        subprocess.run(cmd, shell=True, executable="/bin/bash", check=True)


