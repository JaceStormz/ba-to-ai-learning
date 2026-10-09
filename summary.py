# summary.py

requirements = [
    {"id": "REQ-001", "text": "The system shall validate user login.", "status": "approved"},
    {"id": "REQ-002", "text": "The system shall respond quickly to queries.", "status": "draft"},
    {"id": "REQ-003", "text": "The system shall log all admin actions.", "status": "approved"},
    {"id": "REQ-004", "text": "The interface should be user-friendly.", "status": "draft"},
]


def get_ids(reqs):
    # Extract IDs in a separate, reusable function.
    return [req.get("id", "missing ID") for req in reqs]


def filter_by_status(reqs, status):
    # Return only requirements matching the requested status.
    return [
        req for req in reqs
        if req.get("status", "missing") == status
    ]


def count_by_status(reqs):
    # Treat requirements without a status as "missing".
    counts = {}

    for req in reqs:
        status = req.get("status", "missing")
        counts[status] = counts.get(status, 0) + 1

    return counts


def unique_statuses(reqs):
    # Discover statuses from the data instead of hardcoding them.
    return {req.get("status", "missing") for req in reqs}


def summarize_by_status(reqs):
    # Keep report-building logic in one reusable function.
    summary = {}

    for status in sorted(unique_statuses(reqs)):
        matching_requirements = filter_by_status(reqs, status)

        summary[status] = {
            "count": len(matching_requirements),
            "ids": get_ids(matching_requirements),
        }

    return summary


def print_summary(reqs):
    # Present both the count and IDs needed for the meeting.
    summary = summarize_by_status(reqs)

    print("REQUIREMENTS STATUS SUMMARY")
    print("=" * 50)

    for status, details in summary.items():
        print(f"\nStatus: {status}")
        print(f"Count: {details['count']}")
        print(f"IDs: {', '.join(details['ids'])}")


if __name__ == "__main__":
    print_summary(requirements)