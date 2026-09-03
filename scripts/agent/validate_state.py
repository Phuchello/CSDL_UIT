"""
scripts/agent/validate_state.py
Validates .agent/STATE.yaml and .agent/task-contract.json for Phuchello Agent Workflow v2.
"""
import json
import sys
from pathlib import Path
from typing import Any, Dict, Optional

try:
    import yaml
except ImportError:
    print("FAIL: PyYAML is not installed in the active Python environment.")
    sys.exit(1)


def load_state_yaml(repo_root: Path) -> Optional[Dict[str, Any]]:
    state_file = repo_root / ".agent" / "STATE.yaml"
    if not state_file.exists():
        print(f"FAIL: {state_file} does not exist.")
        return None
    try:
        with open(state_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"FAIL: Could not parse {state_file} as YAML: {e}")
        return None

    required_keys = [
        "project",
        "status",
        "workflow",
        "branch",
        "milestone",
        "frozen",
        "current_task",
        "relevant_files",
        "next_action",
    ]
    for key in required_keys:
        if key not in data:
            print(f"FAIL: Missing key '{key}' in {state_file}.")
            return None

    if data.get("project") != "CSDL_UIT":
        print(f"FAIL: Expected project 'CSDL_UIT', got '{data.get('project')}'.")
        return None

    if data.get("workflow", {}).get("version") != 2:
        print(f"FAIL: Expected workflow version 2, got '{data.get('workflow', {}).get('version')}'.")
        return None

    branch = data.get("branch")
    if not isinstance(branch, str) or not branch.strip():
        print("FAIL: STATE.yaml 'branch' must be a non-empty string.")
        return None

    next_action = data.get("next_action")
    if not isinstance(next_action, str) or not next_action.strip():
        print("FAIL: STATE.yaml 'next_action' must be a non-empty string.")
        return None

    return data


def load_task_contract(repo_root: Path) -> Optional[Dict[str, Any]]:
    contract_file = repo_root / ".agent" / "task-contract.json"
    if not contract_file.exists():
        print(f"FAIL: {contract_file} does not exist.")
        return None
    try:
        with open(contract_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"FAIL: Could not parse {contract_file} as JSON: {e}")
        return None

    if "id" not in data or "acceptance" not in data:
        print(f"FAIL: Missing 'id' or 'acceptance' in {contract_file}.")
        return None

    acceptance = data.get("acceptance", [])
    if not isinstance(acceptance, list) or len(acceptance) == 0:
        print(f"FAIL: 'acceptance' must be a non-empty list in {contract_file}.")
        return None

    seen_ids = set()
    for item in acceptance:
        if "id" not in item or "criterion" not in item or "passes" not in item:
            print(f"FAIL: Invalid acceptance item: {item}")
            return None

        crit_id = item["id"]
        if not isinstance(crit_id, str) or not crit_id.strip():
            print(f"FAIL: Acceptance item id must be a non-empty string: {item}")
            return None

        if crit_id in seen_ids:
            print(f"FAIL: Duplicate acceptance id '{crit_id}' found in {contract_file}.")
            return None
        seen_ids.add(crit_id)

        if not isinstance(item["passes"], bool):
            print(f"FAIL: Acceptance item 'passes' must be boolean for id '{crit_id}', got {type(item['passes'])}.")
            return None

    return data


def main():
    repo_root = Path(__file__).resolve().parent.parent.parent
    state_data = load_state_yaml(repo_root)
    if state_data is None:
        sys.exit(1)

    contract_data = load_task_contract(repo_root)
    if contract_data is None:
        sys.exit(1)

    # Cross-validation: STATE current_task.id must equal task-contract id
    state_task = state_data.get("current_task", {})
    state_task_id = state_task.get("id") if isinstance(state_task, dict) else None
    contract_id = contract_data.get("id")

    if state_task_id != contract_id:
        print(f"FAIL: STATE current_task.id ('{state_task_id}') does not match task-contract id ('{contract_id}').")
        sys.exit(1)

    print("PASS: .agent/STATE.yaml is valid.")
    print(f"PASS: .agent/task-contract.json is valid ({len(contract_data['acceptance'])} criteria).")
    print(f"PASS: Task contract ID synchronized ('{contract_id}').")
    sys.exit(0)


if __name__ == "__main__":
    main()
