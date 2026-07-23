import subprocess
import os

subprocess.run([
    "streamlit",
    "run",
    "src/analysis/models/dashboard/dashboard.py",
    "--server.port",
    os.environ.get("PORT", "8501"),
    "--server.address",
    "0.0.0.0"
])