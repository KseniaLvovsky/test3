# Task 2 Answers
{
  "user_id": "u_123",
  "service_id": "svc_456",
  "booking_date": "2026-03-20",
  "time_slot": "14:00",
  "notes": "Near the back entrance"
}

{
  "booking_id": "b_001",
  "status": "confirmed",
  "message": "Booking created successfully"
}
Write your answers here.

tests:
1. Mandatory fields
   - Try to send empty fields, expect a 401 error
2. Negative flow
   Send the date/numbers/time in the wrong format
   Use a string instead of an int format
   Send an invalid ID
3. Security testing
   Send not authorized user
   SQL injection
   Send the same request multiple times.
4. Code validation
   Success - 200/201
   Invalid data - 401/402/403...
   Server error - 500
5. Relevant message in the request, after sending an error.
6. DB validation after each request
7. Log validation after each request
