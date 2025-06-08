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
This command starts all configured APIs.
Each API folder contains its own `config.ini` specifying the port and other configuration. `Run_all_main.py` reads `New_API/config.ini` to determine which folders to start.

`folder_list` should include only folders that are present under the patch directory; missing folders will be skipped with a warning.

## Docker

Build and run using Docker:

```bash
docker build -t ppp-app .
docker run --rm ppp-app
```

`New_API/config.ini` contains a `patch` option pointing to the directory that
holds the `API_*` folders. By default it uses a relative path (`./`). You can
override this location by setting the environment variable `PATCH_DIR` when
running the scripts. When running in Docker the project is copied to `/app`, so
start the container with `PATCH_DIR=/app` if you do not run from that directory.
