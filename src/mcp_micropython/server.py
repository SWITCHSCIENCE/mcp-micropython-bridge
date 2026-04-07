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

from .serial_manager import SerialManager
from .tools import device, execution, filesystem

mcp = FastMCP(
    name="MicroPython Bridge",
    instructions=(
        "MicroPython インタープリタを操作するブリッジサーバーです。\n"
        "推奨手順:\n"
        "1. micropython_list_ports で接続可能なポートを確認\n"
        "2. micropython_connect で接続 (例: port='COM3')\n"
        "3. micropython_read_hardware_md を使ってハードウェア構成を確認\n"
        "4. micropython_exec や micropython_eval でコードを実行\n"
        "5. 終了時は micropython_disconnect で切断"
    ),
)

_manager = SerialManager()


def _register_tools() -> None:
    """全ツールを MCP サーバーに登録する。"""
    device.register(mcp, _manager)
    execution.register(mcp, _manager)
    filesystem.register(mcp, _manager)


def main() -> None:
    """エントリポイント。stdio トランスポートで MCP サーバーを起動する。"""
    _register_tools()
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
