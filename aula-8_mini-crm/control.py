from pathlib import Path
import json

DATA_DIR = Path(__file__).parent
DB_PATH = DATA_DIR / "leads.json"

# Read

def read_leads():
    if not DB_PATH.exists():
        return []

    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

# Create
def create_lead(lead_dic):
    leads = read_leads()
    leads.append(lead_dic)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent = 2),encoding="utf-8")