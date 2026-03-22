
## Cụm 1: Giả lập "Máy 1" (Node chính & Hạ tầng)

Mở 4 tab Terminal và chạy lần lượt:

1. **Terminal 1 (Orderer):** `python bcb_server/orderer.py`
2. **Terminal 2 (CA):** `python bcb_server/certificate_authority.py --orderer 127.0.0.1`
3. **Terminal 3 (Peer 1):** `python bcb_server/peer.py --orderer 127.0.0.1 --ca 127.0.0.1` *(Node này sẽ chạy mặc định ở cổng 5000)*
4. **Terminal 4 (Giao diện 1):** `python vosy_app/vosy.py --host 127.0.0.1` *(Giao diện này chạy ở cổng 8080, kết nối tới Peer 5000)*

---

## Cụm 2: Giả lập "Máy 2" (Node phụ)

Mở thêm 2 tab Terminal mới (đây là nơi bạn giả lập máy khác):

1. **Terminal 5 (Peer 2):** `python bcb_server/peer.py -p 4000 --orderer 127.0.0.1 --ca 127.0.0.1`
    - **Giải thích:** Bạn dùng cổng `-p 4000` để không bị trùng với Peer 1. Chúng ta vẫn dùng IP `127.0.0.1` vì thực tế nó vẫn đang chạy trên cùng máy bạn.
2. **Terminal 6 (Giao diện 2):** `python vosy_app/vosy.py -p 8081 --host 127.0.0.1:4000`
    - **Giải thích:** `-p 8081` để tránh trùng với Giao diện 1 (8080). `--host 127.0.0.1:4000` để ra lệnh cho giao diện này **chỉ kết nối** tới Peer 2.

