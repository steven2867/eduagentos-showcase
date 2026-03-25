import re
import json


def extract_event(text_input):
    student_match = re.search(r"STU_\d+", text_input)
    session_match = re.search(r"SES_\d+", text_input)

    status = "present"
    if "late" in text_input.lower():
        status = "late"
    elif "no show" in text_input.lower() or "absent" in text_input.lower():
        status = "no_show"

    return {
        "event_type": "attendance_recorded",
        "student_id": student_match.group() if student_match else None,
        "session_id": session_match.group() if session_match else None,
        "status": status
    }


if __name__ == "__main__":
    sample_text = "Student STU_001 joined session SES_001 late at 15:40"

    result = extract_event(sample_text)

    print("Input:")
    print(sample_text)
    print("\nExtracted JSON:")
    print(json.dumps(result, indent=2))