
import os
import sys
import importlib

COMMAND_MODULES = {
    "summarize_meeting": "summarize_meeting",
    "generate_sow": "generate_sow",
    "translate_summary": "translate_summary",
    "create_task": "create_task"
}

def detect_intent():
    command = os.getenv("MEETING_COMMAND")
    if not command and len(sys.argv) > 1:
        command = sys.argv[1]
    return command or "summarize_meeting"

def main():
    command = detect_intent()
    print(f"Executing command: {command}")
    module_name = COMMAND_MODULES.get(command)
    if module_name:
        module = importlib.import_module(f"scripts.{module_name}")
        if hasattr(module, "run"):
            module.run()
        else:
            print(f"Module '{module_name}' does not have a 'run' function.")
    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()
