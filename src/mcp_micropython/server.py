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

- Connect first, then inspect the current board state before making changes.
- Do not assume wiring or attached peripherals until you read `HARDWARE.md` or the existing code.
- Always read `/boot.py` and `/main.py` before modifying them.
- Do not use writes for investigation; use them only for intentional changes.
- When the board state is unclear, prefer small checks and avoid large scripts or bulk overwrites.
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
