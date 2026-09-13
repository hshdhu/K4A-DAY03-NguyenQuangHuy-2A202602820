"""
🔌 MODEL CONTEXT PROTOCOL (MCP) SERVER MODULE
Mô phỏng kiến trúc MCP Server (Client-Server Architecture) cung cấp công cụ cho Facilities Agent.
"""

import json
import sys
from typing import Dict, Any, List
from tools import TOOLS_SCHEMA, dispatch_tool_call

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


class MCPFacilitiesServer:
    """
    Giả lập MCP Server tuân thủ chuẩn giao thức Model Context Protocol
    """

    def __init__(self, server_name: str = "vinuni-facilities-mcp-server"):
        self.server_name = server_name
        self.version = "2026.1.0"

    def list_tools(self) -> List[Dict[str, Any]]:
        """Trả về danh sách các Tools chuẩn giao thức MCP"""
        return TOOLS_SCHEMA

    def call_tool(
        self,
        tool_name: str,
        arguments: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        [TASK 2.1] Thực thi Tool trên MCP Server
        """

        # Gọi Tool Router
        result_json = dispatch_tool_call(tool_name, arguments)

        # Chuyển JSON string thành Dictionary
        content = json.loads(result_json)

        # Đóng gói phản hồi JSON-RPC 2.0
        return {
            "jsonrpc": "2.0",
            "server": self.server_name,
            "tool": tool_name,
            "result": content
        }


if __name__ == "__main__":
    print("==========================================================")
    print("🔌 KIỂM THỬ ĐỘC LẬP MCP SERVER (vinuni-facilities-mcp-server)")
    print("==========================================================")

    server = MCPFacilitiesServer()
    tools = server.list_tools()

    print(
        f"✅ Khởi tạo thành công MCP Server: "
        f"{server.server_name} (Version: {server.version})"
    )
    print(f"📦 Số lượng Tools công bố: {len(tools)}")

    # Kiểm tra Tool Schema
    for tool in tools:
        print(
            f"✅ Tool: {tool['name']} - "
            f"{tool['description']}"
        )

    # Kiểm tra TASK 2.1
    test_result = server.call_tool(
        "room_availability",
        {
            "date": "15/09/2026",
            "time": "14:00",
            "duration_minutes": 60,
            "capacity": 8,
            "equipment": ["projector"]
        }
    )

    if not test_result:
        print(
            "⏳ [TODO 2.1]: Hàm call_tool() đang trả về rỗng."
        )
    else:
        print(
            "✅ [TODO 2.1]: Test dispatch tool "
            "'room_availability' thành công:"
        )
        print(
            f"   Phản hồi JSON-RPC: "
            f"{json.dumps(test_result, ensure_ascii=False)}"
        )
