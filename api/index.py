import os
import sys

# Ensure project root is on sys.path so we can import app
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app import app as vercel_app  # Flask app instance

# Vercel Python looks for an `app` named variable by default; export it
app = vercel_app

