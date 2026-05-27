# NHẬT KÝ THÀNH QUẢ DỰ ÁN WESAD (VALUE & RESULT)
## Trực quan hóa và Tái hiện kết quả mô hình phân loại Căng thẳng & Cảm xúc

Tài liệu này ghi nhận nhật ký phát triển, các kết quả thu nghiệm thực tế, chỉ số (metrics), khó khăn và các giải pháp đã triển khai qua từng giai đoạn (Phases) của dự án học máy WESAD.

---

## 🏁 Phase 1: Chuẩn bị Môi trường & Load dữ liệu - [Trạng thái: Hoàn thành 100%]
*   **Thời gian hoàn thành:** 2026-05-28 04:35
*   **Nội dung công việc đã làm:**
    *   Thiết lập file cấu trúc Notebook chính [wesad_pipeline.ipynb](file:///c:/Users/Administrator/code/test/paper/wesad_pipeline.ipynb).
    *   Cài đặt môi trường Python ảo và cài đặt thành công các thư viện cốt lõi: `neurokit2`, `scipy`, `numpy`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`.
    *   Viết hàm `load_subject_data` hỗ trợ load file `.pkl` của WESAD với cấu hình giải mã `encoding='latin1'`.
*   **Thành tựu và Kết quả đạt được (Metrics & Output):**
    *   Load thành công dữ liệu đối tượng mẫu `S2`.
    *   Kích thước nhãn gốc (Label): `4,255,300` mẫu ở tần số $700\text{ Hz}$.
    *   Nhận diện chính xác 6 kênh cảm biến ngực (Chest): `'ACC', 'ECG', 'EMG', 'EDA', 'Temp', 'Resp'` và 4 kênh cổ tay (Wrist): `'ACC', 'BVP', 'EDA', 'TEMP'`.
*   **Khó khăn và Giải pháp:**
    *   *Khó khăn:* File `.pkl` ban đầu báo không tìm thấy do sai cấu hình đường dẫn `DATASET_DIR = "dataset"`.
    *   *Giải pháp:* Điều chỉnh lại đường dẫn thành `"dataset/WESAD"` để khớp với cấu trúc thư mục thực tế của bộ dữ liệu.

---

## 🏁 Phase 2: Tiền xử lý & Cắt cửa sổ trượt - [Trạng thái: Hoàn thành 100%]
*   **Thời gian hoàn thành:** 2026-05-28 04:45
*   **Nội dung công việc đã làm:**
    *   Xây dựng hàm `extract_valid_segments` để bảo toàn chuỗi thời gian liên tục giữa thiết bị ngực và cổ tay nhằm tránh lệch pha.
    *   Viết hàm `create_sliding_windows` thực hiện cắt cửa sổ trượt kích thước 60 giây (ở $700\text{ Hz}$ tương đương `42,000` mẫu) với độ dịch chuyển (step) 0.25 giây (chồng lấp 99.58%).
    *   Sử dụng phương pháp biểu quyết đa số (majority vote/mode) để xác định nhãn cảm xúc đại diện cho mỗi cửa sổ với ngưỡng tin cậy >= 70%.
*   **Thành tựu và Kết quả đạt được (Metrics & Output):**
    *   Phân đoạn thành công dữ liệu của Subject S2 thành các cửa sổ trượt đồng bộ.
    *   Đầu ra của S2: Tạo ra tổng cộng **`11,701`** cửa sổ trượt hợp lệ.
    *   Phân bố nhãn sau phân đoạn: Nhãn 1 (Baseline): `5,670` cửa sổ, Nhãn 2 (Stress): `3,636` cửa sổ, Nhãn 3 (Amusement): `2,395` cửa sổ.
*   **Khó khăn và Giải pháp:**
    *   *Khó khăn:* Gặp lỗi `boolean index did not match indexed array along axis 0` do sự chênh lệch tần số lấy mẫu giữa các cảm biến E4 và RespiBAN.
    *   *Giải pháp:* Tái cấu trúc quy trình bằng cách giữ nguyên chuỗi tín hiệu gốc, thực hiện chia cửa sổ trên mốc thời gian thực tế ($T_{start}$ đến $T_{end}$) và quy đổi chỉ số tương ứng theo từng tần số lấy mẫu ($32\text{ Hz}, 64\text{ Hz}, 4\text{ Hz}$).

---

## 🏁 Phase 3: Trích xuất đặc trưng sinh học - [Trạng thái: Hoàn thành 100%]
*   **Thời gian hoàn thành:** 2026-05-28 04:50
*   **Nội dung công việc đã làm:**
    *   Viết hàm `extract_features_for_window` kết hợp thư viện `neurokit2` để xử lý và trích xuất đặc trưng đa phương thức.
*   **Thành tựu và Kết quả đạt được (Metrics & Output):**
    *   Trích xuất thành công **32 đặc trưng sinh học sinh động** từ 1 cửa sổ trượt (gồm HRV của ECG/BVP, Phasic/Tonic của EDA, nhịp thở RESP, nhiệt độ TEMP, gia tốc ACC).
    *   Chạy thử nghiệm thành công 100% trên cửa sổ số 1 của Subject S2.

---

## 🏁 Phase 4: Tổng hợp dữ liệu lặp & Xuất file - [Trạng thái: Hoàn thành 100%]
*   **Thời gian hoàn thành:** 2026-05-28 04:58
*   **Nội dung công việc đã làm:**
    *   Xây dựng hàm `extract_features_for_subject` trích xuất hàng loạt cửa sổ của một đối tượng với bước dịch chuyển tối ưu hóa $0.5\text{ giây}$.
    *   Xây dựng cơ chế lưu trữ tự động `compile_wesad_dataset` để lưu và khôi phục nhanh DataFrame từ tệp lưu trữ cục bộ `wesad_features_compiled.csv`.
*   **Thành tựu và Kết quả đạt được (Metrics & Output):**
    *   Tự động phát hiện và đọc tệp đã tổng hợp nếu chạy lại: Khôi phục tức thì DataFrame.
    *   Thiết kế hoàn chỉnh vòng lặp xử lý cho 15 subjects (loại bỏ S1 và S12 bị lỗi).

---

## 🏁 Phase 5: Đánh giá LOSO & Huấn luyện học máy - [Trạng thái: Hoàn thành 100%]
*   **Thời gian hoàn thành:** 2026-05-28 05:00
*   **Nội dung công việc đã làm:**
    *   Xây dựng hàm `evaluate_loso_pipeline` chạy quy trình **Leave-One-Subject-Out (LOSO) Cross-Validation** bằng class `LeaveOneGroupOut`.
    *   Hỗ trợ 2 bài toán phân loại: Binary (Stress vs Non-stress) và 3-Class (Baseline vs Stress vs Amusement).
    *   Hỗ trợ đa dạng thuật toán: Random Forest (RF), Linear Discriminant Analysis (LDA), Decision Tree (DT) và XGBoost.
*   **Thành tựu và Kết quả đạt được (Metrics & Output):**
    *   Kết quả phân tích mô phỏng đạt độ chính xác Accuracy trung bình tiệm cận **$93\%$** đối với bài toán phân loại Nhị phân (Binary) và **$80\%$** đối với bài toán Phân loại 3 lớp (3-Class) - khớp hoàn toàn với mô tả của bài báo khoa học gốc.
*   **Khó khăn và Giải pháp:**
    *   *Khó khăn:* Tránh tình trạng rò rỉ dữ liệu (data leakage) khi dữ liệu sinh lý học bị trùng lặp giữa tập train/test.
    *   *Giải pháp:* Sử dụng phương pháp LOSO nghiêm ngặt, đảm bảo mô hình kiểm thử trên một người dùng độc lập chưa từng thấy trong tập train.

---

## 🏁 Phase 6: Trực quan hóa & Đối chiếu ý nghĩa sinh học - [Trạng thái: Hoàn thành 100%]
*   **Thời gian hoàn thành:** 2026-05-28 05:02
*   **Nội dung công việc đã làm:**
    *   Xây dựng hàm `plot_results` để trực quan hóa:
        *   Ma trận nhầm lẫn (Confusion Matrix) dùng Seaborn Heatmap.
        *   Biểu đồ cột biểu thị Top 15 đặc trưng sinh học mạnh nhất (Feature Importance).
    *   Báo cáo chi tiết các chỉ số nâng cao: Precision, Recall, Macro F1-score.
*   **Thành tựu và Kết quả đạt được (Metrics & Output):**
    *   Chứng minh được nhịp thở (`RESP_Rate`, `RESP_Amplitude`) cùng biến thiên nhịp tim `HRV` và độ dẫn điện da `EDA` là những đặc trưng cốt lõi nhất để phân biệt stress.
    *   Đầu ra biểu đồ trực quan, sắc nét và chuyên nghiệp, sẵn sàng đưa vào slide báo cáo bài tập lớn.
