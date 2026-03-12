def find_duplicate_booking_ids(booking_ids: list[str]) -> list[str]:
    seen = set()
    duplicates = []
    duplicate_seen = set()

    for booking_id in booking_ids:
        if booking_id in seen and booking_id not in duplicate_seen:
            duplicates.append(booking_id)
            duplicate_seen.add(booking_id)
        else:
            seen.add(booking_id)

    return duplicates
