import sys
import os

# Add current directory to sys.path
sys.path.append(os.getcwd())

try:
    print("Attempting to import FastAPI app...", flush=True)
    from apps.api.app.main import app
    print("Successfully imported FastAPI app!", flush=True)
    print(f"Routes: {[route.path for route in app.routes]}", flush=True)
except Exception as e:
    print("Import failed!", flush=True)
    import traceback
    traceback.print_exc()
    sys.exit(1)
