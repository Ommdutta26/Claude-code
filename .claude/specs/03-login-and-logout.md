# Spec: Login and Logout

## Overview
This feature implements the authentication mechanism for Spendly, allowing users to securely access their personal expense data. By implementing login and logout functionality, Spendly ensures that user sessions are managed correctly, preventing unauthorized access to private financial records and providing a personalized experience.

## Depends on
- 02-registration

## Routes
- `GET /login` — Display login form — public
- `POST /login` — Authenticate user and create session — public
- `GET /logout` — Destroy session and redirect to landing — logged-in

## Database changes
No database changes.

## Templates
- **Create:** `login.html`
- **Modify:** `base.html` (to include conditional login/logout links in navigation)

## Files to change
- `app.py`

## Files to create
- `templates/login.html`

## New dependencies
No new dependencies.

## Rules for implementation
- No SQLAlchemy or ORMs
- Parameterised queries only
- Passwords hashed with werkzeug
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`

## Definition of done
- [ ] User can navigate to `/login` and see a login form.
- [ ] User can log in with valid email and password, and is redirected to the profile page.
- [ ] User is shown an error message when attempting to log in with invalid credentials.
- [ ] User already logged in is redirected from `/login` to the profile page.
- [ ] User can log out via `/logout`, session is cleared, and they are redirected to the landing page.
- [ ] Navigation bar shows "Login" when logged out and "Logout" (and user name) when logged in.
