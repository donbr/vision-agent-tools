# config.py
import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
MODEL_NAME = "claude-3-5-sonnet-20240620"
WANDB_API_KEY = os.getenv('WANDB_API_KEY')
WEAVE_PROJECT = "vision_agent_tools"