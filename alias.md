TODO:

```bash
suggest() {
    python3 /path/to/main.py "$@"
}


suggest() {
    python3 ./main.py "$@"
}






suggest() {
    args=""
    for arg in "$@"; do
        if [[ $arg == *"?"* ]]; then
            arg="${arg//\?/\\?}"
        fi
        args="$args $arg"
    done
    python3 ./main.py "$args"
}



```