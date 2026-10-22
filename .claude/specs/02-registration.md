# Spec: Registration

## Overview
The Registration feature allows new users to create an account on Spendly. This is a foundational step in the roadmap, enabling personalized expense tracking by associating every expense with a unique user identity.

## Depends on
None.

## Routes
- `GET /register` — Display the registration form — public
- `POST /register` — Process registration data and create user account — public

## Database changes
No database changes. The `users` table already exists with necessary fields (`name`, `email`, `password_hash`).

## Templates
- **Create:** None.
- **Modify:** `register.html` — Ensure it aligns with design standards and provides clear feedback.

## Files to change
- `app.py` — Review existing `/register` route for completeness and security.

## Files to create
No new files.

## New dependencies
No new dependencies.

## Rules for implementation
- No SQLAlchemy or ORMs
- Parameterised queries only
- Passwords hashed with werkzeug
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`

## Definition of done
- [ ] Visiting `/register` loads the registration page.
- [ ] Submitting the form with all fields filled and matching passwords creates a user in the database.
- [ ] Submitting the form with missing fields triggers a "All fields are required" flash message.
- [ ] Submitting the form with mismatching passwords triggers a "Passwords do not match" flash message.
- [ ] Attempting to register with an email that already exists triggers an "Email already registered" flash message.
- [ ] Successful registration redirects the user to the login page with a success message.
- [ ] Logged-in users visiting `/register` are redirected to their profile page.
