"""Check sample JSON files and basic n8n workflow structure using Python stdlib."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = list(ROOT.glob('workflows/*.json')) + list(ROOT.glob('examples/*.json'))
for path in files:
    with path.open(encoding='utf-8') as fh:
        data = json.load(fh)
    if path.parent.name == 'workflows':
        assert data['nodes'] and data['connections'], 'Workflow requires nodes and connections'
    print('OK', path.relative_to(ROOT))
print(f'Validated {len(files)} JSON files. This does not test Vapi/n8n compatibility.')
