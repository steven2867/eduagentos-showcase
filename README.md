# EduAgentOS (Showcase)

EduAgentOS is an event-driven automation system designed to manage and structure operational workflows.

This project is built based on real experience running an education business, focusing on reliability, traceability, and clear workflow logic.

---

## What Problem It Solves

Operational workflows are often:
- fragmented across multiple tools
- manually tracked
- prone to inconsistency and errors

EduAgentOS structures these workflows into a consistent, event-driven system.

---

## How It Works (Simple View)
Event → Dispatcher → Services → Storage (JSONL)

- Events represent actions (e.g. enrollment, attendance)
- Dispatcher processes events
- Services apply business logic
- Data is stored as append-only records

---

## Example Workflow
enrollment_created → session_created → attendance_recorded

---

## Real Scenario

**Scenario:** Student joins class late (40 minutes)

**Input Event:**

**System Behavior:**
- Student is marked as `late` (not absent)
- Attendance is recorded correctly
- No data overwrite (append-only record)
- System state remains consistent

---

## Design Principles

- Event-driven architecture  
- Append-only data model (audit-friendly)  
- Deterministic and traceable system state  
- Modular and low-coupling design  

---

## Demo
Run a simple demo:
python demo/demo_run.py

This will:
- simulate an event
- process it
- output the result

---

## Project Structure
eduagentos-showcase/
│
├── README.md
├── demo/
│ └── demo_run.py
└── examples/
└── sample_events.jsonl


## AI Integration (Example)
Text → AI extractor → event → demo system

This showcase includes a simple extraction workflow that demonstrates how unstructured text can be converted into structured event data.

Example:

Input:
"Student STU_001 joined session SES_001 late at 15:40"

Output:
{
  "event_type": "attendance_recorded",
  "student_id": "STU_001",
  "session_id": "SES_001",
  "status": "late"
}

In a production environment, this logic can be extended using LLMs or AI APIs.

---

## Notes

This is a simplified showcase version of the system.

The full implementation includes additional modules and logic for extended automation and AI integration.