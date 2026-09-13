# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Nguyễn Quang Huy
> **Mã Sinh Viên / Mã Học viên:** 2A202602820  
> **Chủ đề Lựa chọn:** *Trợ lý Đặt Phòng họp & Thiết bị (Facilities Agent):* Kiểm tra lịch phòng trống, thiết bị và tạo booking phòng họp.  
---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4 / 5 | Bài toán có yêu cầu chia nhỏ nhiều bước suy luận nối tiếp nhau không? |
| **2. Tool Interaction** | 5 / 5 | Hệ thống có cần kết nối với MCP Server / Cơ sở dữ liệu bên ngoài không? |
| **3. Dynamic Decision** | 5 / 5 | Bước tiếp theo có phụ thuộc vào kết quả quan sát bước trước không? |
| **4. Long Horizon Goal** | 4 / 5 | Hệ thống có phải giữ mục tiêu xuyên suốt qua nhiều lượt xử lý không? |
| **TỔNG ĐIỂM AGENTIC FIT** | **18 / 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Hãy đặt cho tôi một phòng họp 20 người vào lúc 18:00 ngày 16/09/2026, cần máy chiếu và bảng trắng. Nếu không có phòng phù hợp thì hãy cho tôi biết.",
    "action_type": "TOOL_EXECUTION",
    "thought": "Gemini quyết định gọi công cụ 'room_availability' với tham số: {\"time\": \"18:00\", \"date\": \"16/09/2026\", \"capacity\": 20, \"duration_minutes\": 60, \"equipment\": [\"projector\", \"whiteboard\"]}",
    "tool_name": "room_availability",
    "arguments": {
      "time": "18:00",
      "date": "16/09/2026",
      "capacity": 20,
      "duration_minutes": 60,
      "equipment": [
        "projector",
        "whiteboard"
      ]
    },
    "observation": {
      "status": "NOT_FOUND",
      "message": "Không tìm thấy phòng họp phù hợp vào lúc 18:00 ngày 16/09/2026 với sức chứa ít nhất 20 người và thiết bị yêu cầu: ['projector', 'whiteboard']."
    },
    "latency_ms": {
      "llm": 4225.85,
      "tool": 0.0
    }
  },
  {
    "step": 2,
    "query": "Hãy đặt cho tôi một phòng họp 20 người vào lúc 18:00 ngày 16/09/2026, cần máy chiếu và bảng trắng. Nếu không có phòng phù hợp thì hãy cho tôi biết.",
    "action_type": "FINAL_ANSWER",
    "thought": "Gemini phản hồi trực tiếp bằng văn bản (không cần gọi công cụ).",
    "output": "Không tìm thấy phòng họp nào phù hợp vào lúc **18:00 ngày 16/09/2026** đáp ứng đủ sức chứa **20 người** và trang bị đầy đủ **máy chiếu (projector)** cùng **bảng trắng (whiteboard)**. \n\nDo đó, hệ thống không thể thực hiện đặt phòng theo yêu cầu. Bạn có thể cân nhắc thay đổi khung giờ, ngày họp hoặc điều chỉnh các yêu cầu thiết bị/sức chứa để kiểm tra lại.",
    "latency_ms": 3973.54
  },
  {
    "step": 1,
    "query": "Tôi cần đặt phòng họp cho 6 người vào ngày 17/09/2026 lúc 10:00.",
    "action_type": "TOOL_EXECUTION",
    "thought": "Gemini quyết định gọi công cụ 'room_availability' với tham số: {\"duration_minutes\": 60, \"equipment\": [], \"capacity\": 6, \"date\": \"17/09/2026\", \"time\": \"10:00\"}",
    "tool_name": "room_availability",
    "arguments": {
      "duration_minutes": 60,
      "equipment": [],
      "capacity": 6,
      "date": "17/09/2026",
      "time": "10:00"
    },
    "observation": {
      "status": "SUCCESS",
      "date": "17/09/2026",
      "time": "10:00",
      "duration_minutes": 60,
      "requested_capacity": 6,
      "requested_equipment": [],
      "available_rooms": [
        {
          "room_name": "Meeting Room A",
          "capacity": 6,
          "equipment": [
            "projector",
            "whiteboard"
          ],
          "date": "17/09/2026",
          "time": "10:00",
          "duration_minutes": 60
        },
        {
          "room_name": "Meeting Room B",
          "capacity": 10,
          "equipment": [
            "projector",
            "whiteboard",
            "video_conference"
          ],
          "date": "17/09/2026",
          "time": "10:00",
          "duration_minutes": 60
        },
        {
          "room_name": "Meeting Room D",
          "capacity": 12,
          "equipment": [
            "whiteboard"
          ],
          "date": "17/09/2026",
          "time": "10:00",
          "duration_minutes": 60
        }
      ]
    },
    "latency_ms": {
      "llm": 5801.49,
      "tool": 0.0
    }
  },
  {
    "step": 2,
    "query": "Tôi cần đặt phòng họp cho 6 người vào ngày 17/09/2026 lúc 10:00.",
    "action_type": "TOOL_EXECUTION",
    "thought": "Gemini quyết định gọi công cụ 'book_room' với tham số: {\"time\": \"10:00\", \"capacity\": 6, \"room_name\": \"Meeting Room A\", \"date\": \"17/09/2026\", \"duration_minutes\": 60, \"equipment\": []}",
    "tool_name": "book_room",
    "arguments": {
      "time": "10:00",
      "capacity": 6,
      "room_name": "Meeting Room A",
      "date": "17/09/2026",
      "duration_minutes": 60,
      "equipment": []
    },
    "observation": {
      "status": "SUCCESS",
      "booking_id": "BK-MEETING-ROOM-A-17092026-1000",
      "room_name": "Meeting Room A",
      "date": "17/09/2026",
      "time": "10:00",
      "duration_minutes": 60,
      "capacity": 6,
      "equipment": [],
      "message": "Đặt phòng thành công: Meeting Room A vào lúc 10:00 ngày 17/09/2026, thời lượng 60 phút."
    },
    "latency_ms": {
      "llm": 3587.47,
      "tool": 0.0
    }
  },
  {
    "step": 3,
    "query": "Tôi cần đặt phòng họp cho 6 người vào ngày 17/09/2026 lúc 10:00.",
    "action_type": "FINAL_ANSWER",
    "thought": "Gemini phản hồi trực tiếp bằng văn bản (không cần gọi công cụ).",
    "output": "Phòng họp của bạn đã được đặt thành công. Dưới đây là thông tin chi tiết về cuộc họp:\n\n- **Mã đặt phòng:** BK-MEETING-ROOM-A-17092026-1000\n- **Phòng họp:** Meeting Room A\n- **Ngày:** 17/09/2026\n- **Thời gian:** 10:00\n- **Thời lượng:** 60 phút\n- **Số lượng người tham dự:** 6 người\n- **Thiết bị có sẵn tại phòng:** Máy chiếu (Projector), Bảng trắng (Whiteboard)",
    "latency_ms": 4196.21
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [X] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 6 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
