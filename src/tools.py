"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer
phục vụ cho Facilities Agent - Trợ lý Đặt Phòng họp & Thiết bị.
"""

import json
from typing import Dict, Any


# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [

    # --------------------------------------------------------------------------
    # Tool 1: Kiểm tra phòng họp còn trống
    # --------------------------------------------------------------------------
    {
        "name": "room_availability",
        "description": (
            "Kiểm tra các phòng họp còn trống theo ngày, thời gian, "
            "thời lượng, số lượng người tham dự và yêu cầu thiết bị."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "date": {
                    "type": "string",
                    "description": (
                        "Ngày cần kiểm tra phòng họp, "
                        "ví dụ: '15/09/2026'"
                    )
                },
                "time": {
                    "type": "string",
                    "description": (
                        "Thời gian bắt đầu cuộc họp, "
                        "ví dụ: '14:00'"
                    )
                },
                "duration_minutes": {
                    "type": "integer",
                    "description": (
                        "Thời lượng cuộc họp tính bằng phút, "
                        "ví dụ: 60"
                    )
                },
                "capacity": {
                    "type": "integer",
                    "description": (
                        "Số lượng người tham dự cuộc họp, "
                        "ví dụ: 8"
                    )
                },
                "equipment": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": (
                        "Danh sách thiết bị cần thiết, "
                        "ví dụ: ['projector', 'whiteboard']"
                    )
                }
            },
            "required": [
                "date",
                "time",
                "duration_minutes",
                "capacity",
                "equipment"
            ]
        }
    },

    # --------------------------------------------------------------------------
    # Tool 2: Đặt phòng họp
    # --------------------------------------------------------------------------
    {
        "name": "book_room",
        "description": (
            "Đặt một phòng họp còn trống theo phòng, ngày, thời gian, "
            "thời lượng, sức chứa và yêu cầu thiết bị."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "room_name": {
                    "type": "string",
                    "description": (
                        "Tên phòng họp cần đặt, "
                        "ví dụ: 'Meeting Room A'"
                    )
                },
                "date": {
                    "type": "string",
                    "description": (
                        "Ngày đặt phòng, "
                        "ví dụ: '15/09/2026'"
                    )
                },
                "time": {
                    "type": "string",
                    "description": (
                        "Thời gian bắt đầu cuộc họp, "
                        "ví dụ: '14:00'"
                    )
                },
                "duration_minutes": {
                    "type": "integer",
                    "description": (
                        "Thời lượng cuộc họp tính bằng phút, "
                        "ví dụ: 60"
                    )
                },
                "capacity": {
                    "type": "integer",
                    "description": (
                        "Số lượng người tham dự cuộc họp, "
                        "ví dụ: 8"
                    )
                },
                "equipment": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": (
                        "Danh sách thiết bị cần thiết, "
                        "ví dụ: ['projector', 'whiteboard']"
                    )
                }
            },
            "required": [
                "room_name",
                "date",
                "time",
                "duration_minutes",
                "capacity",
                "equipment"
            ]
        }
    }
]


# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU PHÒNG HỌP
# ==============================================================================

MOCK_ROOMS = [
    {
        "room_name": "Meeting Room A",
        "capacity": 6,
        "equipment": ["projector", "whiteboard"],
        "available": True
    },
    {
        "room_name": "Meeting Room B",
        "capacity": 10,
        "equipment": ["projector", "whiteboard", "video_conference"],
        "available": True
    },
    {
        "room_name": "Meeting Room C",
        "capacity": 20,
        "equipment": ["projector", "whiteboard", "video_conference"],
        "available": False
    },
    {
        "room_name": "Meeting Room D",
        "capacity": 12,
        "equipment": ["whiteboard"],
        "available": True
    }
]


# ==============================================================================
# 3. EXECUTION LAYER
# ==============================================================================

def execute_room_availability(
    date: str,
    time: str,
    duration_minutes: int,
    capacity: int,
    equipment: list
) -> str:
    """
    Kiểm tra các phòng họp đáp ứng yêu cầu về:
    - Thời gian
    - Thời lượng
    - Sức chứa
    - Thiết bị
    """

    required_equipment = [
        str(item).strip().lower()
        for item in equipment
    ]

    available_rooms = []

    for room in MOCK_ROOMS:

        # Phòng phải đang available
        if not room["available"]:
            continue

        # Kiểm tra sức chứa
        if room["capacity"] < capacity:
            continue

        # Kiểm tra thiết bị
        room_equipment = [
            str(item).strip().lower()
            for item in room["equipment"]
        ]

        if not all(
            item in room_equipment
            for item in required_equipment
        ):
            continue

        available_rooms.append({
            "room_name": room["room_name"],
            "capacity": room["capacity"],
            "equipment": room["equipment"],
            "date": date,
            "time": time,
            "duration_minutes": duration_minutes
        })

    if available_rooms:
        return json.dumps(
            {
                "status": "SUCCESS",
                "date": date,
                "time": time,
                "duration_minutes": duration_minutes,
                "requested_capacity": capacity,
                "requested_equipment": equipment,
                "available_rooms": available_rooms
            },
            ensure_ascii=False
        )

    return json.dumps(
        {
            "status": "NOT_FOUND",
            "message": (
                f"Không tìm thấy phòng họp phù hợp vào lúc {time} "
                f"ngày {date} với sức chứa ít nhất {capacity} người "
                f"và thiết bị yêu cầu: {equipment}."
            )
        },
        ensure_ascii=False
    )


def execute_book_room(
    room_name: str,
    date: str,
    time: str,
    duration_minutes: int,
    capacity: int,
    equipment: list
) -> str:
    """
    Thực hiện đặt phòng họp.

    Tool chỉ cho phép booking nếu phòng:
    - Tồn tại
    - Đang available
    - Đủ sức chứa
    - Có đầy đủ thiết bị yêu cầu
    """

    room = None

    for item in MOCK_ROOMS:
        if item["room_name"].lower() == room_name.strip().lower():
            room = item
            break

    # Không tìm thấy phòng
    if room is None:
        return json.dumps(
            {
                "status": "NOT_FOUND",
                "message": (
                    f"Không tìm thấy phòng họp '{room_name}'."
                )
            },
            ensure_ascii=False
        )

    # Phòng đã được sử dụng
    if not room["available"]:
        return json.dumps(
            {
                "status": "UNAVAILABLE",
                "message": (
                    f"Phòng '{room_name}' hiện không còn trống."
                )
            },
            ensure_ascii=False
        )

    # Không đủ sức chứa
    if room["capacity"] < capacity:
        return json.dumps(
            {
                "status": "INVALID",
                "message": (
                    f"Phòng '{room_name}' chỉ có sức chứa "
                    f"{room['capacity']} người, không đáp ứng "
                    f"yêu cầu {capacity} người."
                )
            },
            ensure_ascii=False
        )

    # Kiểm tra thiết bị
    room_equipment = [
        str(item).strip().lower()
        for item in room["equipment"]
    ]

    required_equipment = [
        str(item).strip().lower()
        for item in equipment
    ]

    missing_equipment = [
        item
        for item in required_equipment
        if item not in room_equipment
    ]

    if missing_equipment:
        return json.dumps(
            {
                "status": "INVALID",
                "message": (
                    f"Phòng '{room_name}' thiếu thiết bị: "
                    f"{missing_equipment}."
                )
            },
            ensure_ascii=False
        )

    # Booking thành công
    booking_id = (
        f"BK-{room_name.replace(' ', '-').upper()}-"
        f"{date.replace('/', '')}-{time.replace(':', '')}"
    )

    return json.dumps(
        {
            "status": "SUCCESS",
            "booking_id": booking_id,
            "room_name": room_name,
            "date": date,
            "time": time,
            "duration_minutes": duration_minutes,
            "capacity": capacity,
            "equipment": equipment,
            "message": (
                f"Đặt phòng thành công: {room_name} vào lúc "
                f"{time} ngày {date}, thời lượng {duration_minutes} phút."
            )
        },
        ensure_ascii=False
    )


# ==============================================================================
# 4. ROUTER GỌI TOOL THỰC TẾ
# ==============================================================================

TOOL_ROUTER = {
    "room_availability": execute_room_availability,
    "book_room": execute_book_room
}


def dispatch_tool_call(
    tool_name: str,
    arguments: Dict[str, Any]
) -> str:
    """
    Hàm trung chuyển thực thi Tool.
    """

    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)

        except Exception as e:
            return json.dumps(
                {
                    "status": "EXECUTION_ERROR",
                    "error": str(e)
                },
                ensure_ascii=False
            )

    return json.dumps(
        {
            "status": "UNKNOWN_TOOL",
            "error": f"Tool '{tool_name}' không tồn tại!"
        },
        ensure_ascii=False
    )

