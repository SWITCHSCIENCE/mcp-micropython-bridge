# Recipes

Use these short recipes as starting points for common tasks.

## List available ports

1. Run `micropython_list_ports`.
2. Choose the target serial port from the result.

## Connect to a board

1. Run `micropython_connect` with the selected port.
2. Confirm the connection before reading device resources.

## Read `HARDWARE.md`

1. Connect to the board.
2. Read `micropython://device/HARDWARE.md`.
3. Use it before assuming wiring, GPIO, or attached peripherals.

## Inspect the filesystem

1. Connect to the board.
2. Read `micropython://filesystem/list/root`.
3. Read specific files with `micropython://filesystem/read/{path}` or `micropython_read_file`.

## Read a temperature sensor

1. Read `HARDWARE.md` or existing code to identify the sensor and bus.
2. Use `micropython_eval` for a simple probe or `micropython_exec` for a short read script.
3. Keep the first check small and explicit.

## Read a light sensor

1. Confirm the sensor model and wiring from `HARDWARE.md` or existing code.
2. Use a short `micropython_exec` script that only initializes the needed bus and prints one reading.

## Recover from a hang

1. Run `micropython_interrupt`.
2. If the REPL does not recover, reconnect.
3. If the board was reset, treat the session as disconnected.

## Disconnect

1. Run `micropython_disconnect` when finished.
