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
`Run_all_main.py` assigns ports sequentially beginning at **8080** and updates each API's `config.ini` with the computed port before launching it. When starting a single API manually you must ensure its configured port is free. Either stop any process currently using that port or edit the API's `config.ini` to use a different value.

`folder_list` should include only folders that are present under the patch directory; missing folders will be skipped with a warning.
If an entry in `folder_list` does not correspond to a real API directory containing a `config.ini`, the update scripts will skip it and log a warning. The scripts also verify that each `config.ini` has a valid `Config` section before proceeding.

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

## Healthcheck

Each API exposes a `/healthcheck` endpoint that simply returns `"OK"`.
