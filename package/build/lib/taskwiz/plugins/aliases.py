"""
TaskWiz Bot Plugin - aliases

add aliases
"""

from taskwiz import config
import sys, os

config.aliases["!autogen"] = f"!{sys.executable} {os.path.join(config.taskWizAIFolder, 'autogen_assistant.py')}"
config.aliases["!math"] = f"!{sys.executable} {os.path.join(config.taskWizAIFolder, 'autogen_math.py')}"
config.aliases["!retriever"] = f"!{sys.executable} {os.path.join(config.taskWizAIFolder, 'autogen_retriever.py')}"
config.aliases["!teachable"] = f"!{sys.executable} {os.path.join(config.taskWizAIFolder, 'autogen_teachable.py')}"
config.aliases["!etextedit"] = f"!{sys.executable} {os.path.join(config.taskWizAIFolder, 'eTextEdit.py')}"

config.inputSuggestions += ["!autogen", "!math", "!retriever", "!teachable", "!etextedit"]

# Example to set an alias to open-interpreter
#config.aliases["!interpreter"] = f"!env OPENAI_API_KEY={config.openaiApiKey} ~/open-interpreter/venv/bin/interpreter"