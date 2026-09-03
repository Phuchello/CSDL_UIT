"""
scripts/agent/validate_state.py
Validates .agent/STATE.yaml and .agent/task-contract.json for Phuchello Agent Workflow v2.
"""
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("FAIL: PyYAML is not installed in the active Python environment.")
    sys.exit(1)

def validate_state_yaml(repo_root: Path) -> bool:
    state_file = repo_root / ".agent" / "STATE.yaml"
    if not state_file.exists():
        print(f"FAIL: {state_file} does not exist.")
        return False
    try:
        with open(state_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"FAIL: Could not parse {state_file} as YAML: {e}")
        return False

    required_keys = ["project", "status", "workflow", "branch", "milestone", "frozen", "current_task", "relevant_files", "next_action"]
    for key in required_keys:
        if key not in data:
            print(f"FAIL: Missing key '{key}' in {state_file}.")
            return False

    if data.get("project") != "CSDL_UIT":
        print(f"FAIL: Expected project 'CSDL_UIT', got '{data.get('project')}'.")
        return False

    if data.get("workflow", {}).get("version") != 2:
        print(f"FAIL: Expected workflow version 2, got '{data.get('workflow', {}).get('version')}'.")
        return False

    print("PASS: .agent/STATE.yaml is valid.")
    return True

def validate_task_contract(repo_root: Path) -> bool:
    contract_file = repo_root / ".agent" / "task-contract.json"
    if not contract_file.exists():
        print(f"FAIL: {contract_file} does not exist.")
        return False
    try:
        with open(contract_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"FAIL: Could not parse {contract_file} as JSON: {e}")
        return False

    if "id" not in data or "acceptance" not in data:
        print(f"FAIL: Missing 'id' or 'acceptance' in {contract_file}.")
        return False

    acceptance = data.get("acceptance", [])
    if not isinstance(acceptance, list) or len(acceptance) == 0:
        print(f"FAIL: 'acceptance' must be a non-empty list in {contract_file}.")
        return False

    for item in acceptance:
        if "id" not in item or "criterion" not in item or "passes" not in item:
            print(f"FAIL: Invalid acceptance item: {item}")
            return False

    print(f"PASS: .agent/task-contract.json is valid ({len(acceptance)} criteria).")
    return True

def main():
    repo_root = Path(__file__).resolve().parent.parent.parent
    state_ok = validate_state_yaml(repo_root)
    contract_ok = validate_task_contract(repo_root)
    if state_ok and contract_ok:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
