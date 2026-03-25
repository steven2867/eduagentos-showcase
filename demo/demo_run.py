import json
from pathlib import Path

# Path to sample data
DATA_PATH = Path(__file__).resolve().parent.parent / "examples" / "sample_events.jsonl"


def process_event(event):
    event_type = event.get("event_type")

    if event_type == "enrollment_created":
        return f"Enrollment created for student {event['student_id']}"

    elif event_type == "session_created":
        return f"Session {event['session_id']} scheduled"

    elif event_type == "attendance_recorded":
        student = event.get("student_id")
        status = event.get("status")

        if status == "late":
            return f"Student {student} marked as LATE"
        elif status == "present":
            return f"Student {student} marked as PRESENT"
        elif status == "no_show":
            return f"Student {student} marked as NO SHOW"

    return "Unknown event"


def main():
    print("=== EduAgentOS Demo Run ===\n")

    with open(DATA_PATH, "r") as f:
        for line in f:
            event = json.loads(line.strip())
            result = process_event(event)

            print(f"Event: {event['event_type']}")
            print(f"Result: {result}")
            print("-" * 40)


if __name__ == "__main__":
    main()