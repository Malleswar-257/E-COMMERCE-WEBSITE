from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI(title="Fallback Backend", description="Minimal scaffold")

@app.get('/health')
def health():
    return {'status': 'ok'}

    # TODO: Implement endpoints from PRD and impact analysis