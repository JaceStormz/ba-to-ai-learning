requirements = [
    {"id": "REQ-001", "text": "The system shall validate user login.", "status": "approved"},
    {"id": "REQ-002", "text": "The system shall respond quickly to queries.", "status": "draft"},
    {"id": "REQ-003", "text": "The system shall log all admin actions.", "status": "approved"},
    {"id": "REQ-004", "text": "The interface should be user-friendly.", "status": "draft"},
]


def get_ids(reqs):
    # Pull each requirement ID into a new list.
    return [req["id"] for req in reqs]


def filter_by_status(reqs, status):
    # Keep only requirements that match the requested status.
    return [req for req in reqs if req["status"] == status]


def count_by_status(reqs):
    # Build the counts one requirement at a time.
    counts = {}

    for req in reqs:
        status = req["status"]
        counts[status] = counts.get(status, 0) + 1

    return counts


def unique_statuses(reqs):
    # A set comprehension keeps each status only once.
    return {req["status"] for req in reqs}


if __name__ == "__main__":
    print("IDs:", get_ids(requirements))
    print("Approved:", filter_by_status(requirements, "approved"))
    print("Draft:", filter_by_status(requirements, "draft"))
    print("Counts:", count_by_status(requirements))
    print("Unique statuses:", unique_statuses(requirements))