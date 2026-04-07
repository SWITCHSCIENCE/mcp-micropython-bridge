# Limitations

## Connection-dependent data

- Some information is only available after connecting to the board.
- Filesystem resources and `HARDWARE.md` cannot be read without an active session.

## Session behavior

- A reset can close the current serial session.
- Long-running or noisy programs may leave the REPL in a state that needs interrupt or reconnect.

## File transfer constraints

- Large text writes may fail because of Raw REPL and transport limits.
- Large binary transfers are not a primary use case of this server.

## Hardware variability

- GPIO assignments and peripheral availability differ by board.
- Generic MicroPython examples may still be wrong for a specific board or wiring setup.
