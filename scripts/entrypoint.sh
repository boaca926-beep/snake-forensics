#!/bin/bash
set -e

echo "🐍 Snake Game - DEV MODE"
echo "========================"
echo "X11 Display: ${DISPLAY}"
echo "Debug port: 5678"

# Check if X11 socket is available (for GUI)
if [ -n "$DISPLAY" ] && [ -e "/tmp/.X11-unix/X${DISPLAY#*:}" ]; then
    echo "✅ X11 forwarding detected - GUI will be displayed"
else
    echo "⚠️  No X11 forwarding - running with virtual display"
    Xvfb :99 -screen 0 1024x768x24 &
    export DISPLAY=:99
fi

# Start debugpy server for remote debugging (optional)
if [ "${ENABLE_DEBUG:-false}" = "true" ]; then
    echo "🐛 Debugger listening on port 5678"
    python -m debugpy --listen 0.0.0.0:5678 --wait-for-client snake.py &
    DEBUG_PID=$!
    wait $DEBUG_PID
else
    # Execute the command
    exec "$@"
fi
