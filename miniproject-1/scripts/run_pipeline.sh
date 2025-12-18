BASE_DIR="/home/thu/repo/dec-lab/miniproject-1"
VENV_PY="/home/thu/repo/dec-lab/.venv/bin/python"
LOG_DIR="$BASE_DIR/logs"
CRON_LOG="$LOG_DIR/cron.log"

export PYTHONPATH="$BASE_DIR"

echo "[$(date)] Starting ETL" >> "$CRON_LOG"

cd "$BASE_DIR"
"$VENV_PY" src/main.py
