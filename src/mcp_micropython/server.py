"""
server.py - MCP サーバーエントリポイント

起動方法:
    uv run mcp-micropython

Claude Desktop / VSCode Extension の設定例:
    {
      "mcpServers": {
        "micropython": {
          "command": "uv",
          "args": ["--directory", "<このディレクトリのパス>", "run", "mcp-micropython"]
        }
      }
    }
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from . import static_resources
from .serial_manager import SerialManager
from .tools import device, execution, filesystem

mcp = FastMCP(
    name="MicroPython Bridge",
    instructions="""## MicroPython MCP rules

- Connect first and inspect the current board state before changing anything.
- Read `HARDWARE.md` first and treat it as the source of truth for wiring, peripherals, helper modules, and board-specific APIs.
- Prefer documented helpers over ad-hoc direct hardware access.
- If new hardware behavior is needed, implement or extend a small reusable helper module instead of leaving a one-off script.
- After adding a helper, append a brief `HARDWARE.md` note with where it lives and a one-line example call so future sessions can reuse it.
- Do not assume hardware details without reading `HARDWARE.md` or existing code.
- Always read `/boot.py` and `/main.py` before modifying them.
- Use writes only for intentional changes; when unsure, prefer small checks and avoid bulk overwrites.
- Disconnect when appropriate, and assume a reset may require reconnection.
""",
)

_manager = SerialManager()


def _register_tools() -> None:
    """全ツールを MCP サーバーに登録する。"""
    static_resources.register(mcp)
    device.register(mcp, _manager)
    execution.register(mcp, _manager)
    filesystem.register(mcp, _manager)


def main() -> None:
    """エントリポイント。stdio トランスポートで MCP サーバーを起動する。"""
    _register_tools()
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
