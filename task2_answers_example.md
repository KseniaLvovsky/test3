# Task 2 Answers Example

## Sample API test cases
1. Valid request with all required fields returns 201.
2. Missing `user_id` returns 400.
3. Missing `service_id` returns 400.
4. Missing `booking_date` returns 400.
5. Missing `time_slot` returns 400.
6. `booking_date` in the past returns 400 or 422.
7. Invalid `time_slot` format returns 400 or 422.
8. `notes` longer than 250 chars returns 400 or 422.
9. Duplicate booking for same user/service/date/time returns 409.
10. Unsupported content type returns 415.
11. Unauthorized request returns 401.
12. Forbidden request returns 403 if token lacks access.
13. Malformed JSON returns 400.
14. Server failure returns 500.

## Response fields to validate
- `booking_id` exists and is not empty
- `status` equals `confirmed`
- `message` is correct and consistent
- Response schema and field types are correct

## Questions for team
- Time zone expectations
- Whether bookings are idempotent
- Exact validation messages
- Whether `notes` trims whitespace
- Duplicate booking business rules
