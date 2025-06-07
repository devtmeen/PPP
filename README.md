# PPP

This project hosts multiple Flask APIs located in the `API_*` folders.

## Setup

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Run the launcher script to start update jobs and all APIs defined in `New_API/config.ini`:

```bash
python New_API/launcher.py
```
This cross-platform command replaces the old Windows `.bat` launchers.

Each API folder contains its own `config.ini` specifying the port and other configuration. `Run_all_main.py` reads `New_API/config.ini` to determine which folders to start.

## Docker

Build and run using Docker:

```bash
docker build -t ppp-app .
docker run --rm ppp-app
```

Make sure the `patch` path in `New_API/config.ini` matches the location of the API folders inside the container (usually `/app/`).
