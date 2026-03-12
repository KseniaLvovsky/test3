# API Notes

Additional assumptions for the booking API:

- `user_id` is required.
- `service_id` is required.
- `booking_date` must not be in the past.
- `time_slot` must follow `HH:MM` 24-hour format.
- `notes` is optional and supports up to 250 characters.
- A user cannot create two bookings for the same service, date, and time slot.
- The API uses JSON.
- Authentication is required, but auth behavior is out of scope unless relevant to your test design.
