# Task 3 Bug Report Example

**Title:** Booking confirmation message shown even though booking is not persisted in booking history

**Environment:** Staging, web app, latest build

**Preconditions:** User is logged in and has access to the booking page.

**Steps to reproduce:**
1. Open booking page.
2. Select a valid available service/date/time slot.
3. Submit booking.
4. Observe confirmation message.
5. Refresh page or open booking history.

**Expected result:** Confirmed booking appears in booking history after successful submission.

**Actual result:** UI shows "Booking confirmed" but booking does not appear in history.

**Frequency:** Intermittent

**Severity:** High

**Priority:** High

**Notes / evidence to collect:** Network response, backend logs, booking DB record, timestamps, screenshots/video, correlation/request ID if available.
