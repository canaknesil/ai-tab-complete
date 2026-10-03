# AI Tab Complete

AI-assisted Bash command completion. The project sends an English description or incomplete shell command to an Ollama-compatible model and places the generated Bash command in the current prompt.

## Setup

Create environment variables for Ollama IP, port, and model. Default values are as below.
```
AI_TAB_COMPLETE_OLLAMA_IP=127.0.0.1
AI_TAB_COMPLETE_OLLAMA_PORT=11434
AI_TAB_COMPLETE_OLLAMA_MODEL=qwen2.5-coder:3b
```

Source Bash bindings:
```bash
source .../ai-tab-complete/binding/activate_in_bash
```

## Usage

1. Type an English description, a broken command, or a combination of both.
```
$ merge a.pdf and b.pdf with pdftk
```
2. Press `Ctrl-x TAB`. The prompt is replaced with the suggested command.
```
$ pdftk a.pdf b.pdf cat output merged.pdf
```
3. Review the generated command and edit it as needed.
4. Press `Enter` to run it, or use `Ctrl-x r` to restore the original prompt.



