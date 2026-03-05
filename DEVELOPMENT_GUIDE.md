# FoxPRO-HR — Step-by-Step Development Guide

## Tech stack chosen (PythonAnywhere friendly)
- Backend: Django
- Frontend: Django templates + modern CSS
- DB (starter): SQLite (switchable to MySQL on PythonAnywhere)
- Deployment target: PythonAnywhere (WSGI)

## Project structure and where code goes
- `foxpro_hr/settings.py`: global config, apps, DB, static/media, auth model
- `foxpro_hr/urls.py`: root routes
- `apps/<module>/models.py`: each module data model
- `apps/<module>/admin.py`: admin registration for CRUD via Django admin
- `apps/core/views.py`: dashboard/specification/guide pages
- `foxpro_hr/templates/`: all HTML pages
- `foxpro_hr/static/css/styles.css`: modern responsive UI and animations

## Build phases
1. Setup environment and dependencies
2. Model entities module-by-module
3. Run migrations and admin setup
4. Create role-based pages and dashboards
5. Add business logic workflows
6. Add notifications, exports, reporting
7. Harden security and audit trails
8. Deploy on PythonAnywhere

## Local run commands
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## PythonAnywhere deployment (exact flow)
1. Create web app (Manual configuration, Python 3.10+)
2. Open a Bash console and upload project to home folder.
3. Create virtualenv and install requirements:
```bash
mkvirtualenv foxprohr --python=/usr/bin/python3.10
pip install -r /home/<your-user>/FoxPRO-HR/requirements.txt
```
4. In Web tab, set source code path to project and static mapping:
   - URL: `/static/` → `/home/<your-user>/FoxPRO-HR/staticfiles`
   - URL: `/media/` → `/home/<your-user>/FoxPRO-HR/media`
5. Update WSGI config to load `foxpro_hr.settings` and `foxpro_hr.wsgi.application`.
6. Run migrations on PythonAnywhere Bash:
```bash
cd /home/<your-user>/FoxPRO-HR
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```
7. Reload web app.

## Next implementation backlog (recommended)
- Build full CRUD screens per module
- Add DRF APIs for mobile app and biometric device integration
- Implement approval workflows and audit logs
- Add Celery for scheduled payroll jobs and reminders
