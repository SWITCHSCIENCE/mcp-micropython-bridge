# mcp-micropython

MicroPython REPL への MCP ブリッジサーバー。

Claude Desktop, Codex (VSCode), Copilot (VSCode), Antigravity などの MCP クライアントから、
USB Serial 経由で MicroPython (ESP32, RP2040, etc.) を操作できます。

## セットアップ

```powershell
# 依存関係のインストール
uv sync

# サーバー起動（動作確認用）
uv run mcp-micropython
```

## MCP クライアントへの登録

`claude_desktop_config_example.json` を参考に、各クライアントの設定ファイルに追記してください。

```json
{
  "mcpServers": {
    "micropython": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\Users\\sasaki.yusuke\\144Lab\\0079_MCP",
        "run",
        "mcp-micropython"
      ]
    }
  }
}
```

## 提供ツール

| ツール | 説明 |
|---|---|
| `micropython_list_ports` | 利用可能なシリアルポートを列挙 |
| `micropython_connect` | 指定ポートに接続 |
| `micropython_disconnect` | 接続を切断 |
| `micropython_exec` | Python コードをブロック実行 |
| `micropython_eval` | 式を評価して値を返す |
| `micropython_get_info` | デバイス情報取得 |
| `micropython_reset` | ソフトリセット |
| `micropython_list_files` | ファイル一覧 |
| `micropython_read_file` | ファイル読み出し |
| `micropython_write_file` | ファイル書き込み |
| `micropython_delete_file` | ファイル削除 |
