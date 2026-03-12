# Task 2 — API Test Design

Answer in `answers/task2_answers.md`.

You are testing the following endpoint:

`POST /v1/bookings`

### Request body
```json
{
  "user_id": "u_123",
  "service_id": "svc_456",
  "booking_date": "2026-03-20",
  "time_slot": "14:00",
  "notes": "Near the back entrance"
}
```

### Success response
Status: `201 Created`

```json
{
  "booking_id": "b_001",
  "status": "confirmed",
  "message": "Booking created successfully"
}
```

## Questions

1. Write at least 12 API test cases for this endpoint.
2. Include positive, negative, validation, and edge cases.
3. What status codes would you expect for different failure types?
4. What fields would you validate in the response?
5. What additional questions would you ask the product or backend team before finalizing test coverage?
