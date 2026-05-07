
## Cụm 1: Giả lập "Máy 1" (Node chính & Hạ tầng)

Mở 4 tab Terminal và chạy lần lượt:

1. **Terminal 1 (Orderer):** 
python bcb_server/orderer.py
2. **Terminal 2 (CA):** 
python bcb_server/certificate_authority.py --orderer 127.0.0.1
3. **Terminal 3 (Peer 1):** 
python bcb_server/peer.py --orderer 127.0.0.1 --ca 127.0.0.1 
*(Node này sẽ chạy mặc định ở cổng 5000)*
4. **Terminal 4 (Giao diện 1):** 
python vosy_app/vosy.py --host 127.0.0.1
 *(Giao diện này chạy ở cổng 8080, kết nối tới Peer 5000)*

---

## Cụm 2: Giả lập "Máy 2" (Node phụ)

Mở thêm 2 tab Terminal mới:

1. **Terminal 5 (Peer 2):** 
python bcb_server/peer.py -p 4000 --orderer 127.0.0.1 --ca 127.0.0.1

    - dùng cổng `-p 4000` để không bị trùng với Peer 1. Chúng ta vẫn dùng IP `127.0.0.1` vì thực tế nó vẫn đang chạy trên cùng máy bạn.
2. **Terminal 6 (Giao diện 2):** 
python vosy_app/vosy.py -p 8081 --host 127.0.0.1:4000

    - `-p 8081` để tránh trùng với Giao diện 1 (8080). `--host 127.0.0.1:4000` để ra lệnh cho giao diện này chỉ kết nối tới Peer 2.

## Cụm 3: Giả lập "Máy 3" (Node phụ thứ 2)

**1. Terminal 7 (Peer 3):**

Bash

python bcb_server/peer.py -p 4001 --orderer 127.0.0.1 --ca 127.0.0.1

- gán cổng `p 4001` (hoặc bất kỳ số nào khác 5000 và 4000) để tạo một Node Peer hoàn toàn mới. Nó vẫn kết nối về trung tâm Orderer và CA nội bộ.

**2. Terminal 8 (Giao diện 3):**

Bash

python vosy_app/vosy.py -p 8082 --host 127.0.0.1:4001

- dùng cổng `p 8082` cho giao diện web này để không trùng với Máy 1 (8080) và Máy 2 (8081). Tham số `-host 127.0.0.1:4001` chỉ định giao diện này chỉ giao tiếp với Peer 3.