# Hệ thống lưu trữ thông tin học viên và phân bổ khóa học cho học viên HỌC VIỆN TEKY
- Để chạy chương trình, đầu tiên ta cần cài đặt các thư viện cần thiết có để chương trình có thể chạy được: tuy nhiên về cơ bản, thư viện cần thiết trong chương trình là tkinter, os, json đều đã được cài đặt sẵn trong python nên sẽ hầu như không cần cài đặt gì thêm, nếu chương trình xuất hiện lỗi bạn có thể kiểm tra lỗi và cài đặt nếu bị thiếu thư viện nào đó
## TEKY System
- TEKY System là một hệ thống lưu trữ giúp giáo viên cũng như học sinh có thể theo dõi cũng như đăng kí được môn học một cách trực quan và dễ dàng thao tác. Từ nền tảng này, hệ thống sẽ có thể tích hợp thêm nhiều công nghệ AI trong tương lai giúp hệ thống có thể hoạt động một cách thông minh nhất.
## Chạy chương trình:
- Để chạy được chương trình, bạn hãy tải file source code của chương trình, sau khi tải hãy giải nén ra
- Theo đó để chạy được chương trình, bạn chỉ cần chọn vào chương trình X_Main.py để có thể chạy chương trình
## Tính năng:
- Đầu tiên khi login vào chương trình bạn sẽ thấy một giao diện mang hình chính của hệ thống dữ liệu lưu trữ học viên
    + Ở trang này, ta được phép nhập tên, ID, giới tính, địa chỉ liên lạc, số điện thoại, tháng nhập học, tình trạng nhập học: sua khi đã điền xong các thông tin cơ bản, bạn chỉ cần ấn nút lưu, thì chương trình sẽ lưu trữ dữ liệu của bạn vào hệ thống
- Sau khi đã nhập thông tin xong, bạn có thể vào thanh công cụ tiếp theo trên giao diện để sử dụng chức năng đó là hiển thị học sinh: Tại mục này bạn chỉ cần click vào nút hiển thị học sinh, hệ thống sẽ tự động chuyển về cho bạn toàn bộ dữ liệu học sinh đã lưu trữ trong hệ thống, bao gồm cả thông tin học sinh mà bạn đã nhập
- Tiếp theo tại phần tạo khóa học: ở đây bạn có thể nhập mã cửa khóa học mới mà bạn muốn tạo, tiếp theo là tên khóa học và nhấn nút lưu, chương trình sẽ tự động tạo khóa học mới
- Kế đó, trên thanh công cụ là nút hiển thị khóa học, tại đây bạn hãy nhấn nút xem khóa học, tất cả các khóa học có trên cơ sở dữ liệu sẽ được đưa về, bao gồm ID khóa học, tên khóa học
- Và cuối đó, tại mục phân bổ khóa học, ở đây bạn có thể phân bổ khóa mà học sinh sẽ học bằng cách nhập ID của học sinh và sau đó chọn khóa học cho học sinh, chương trình sẽ tự động lưu trữ thông tin vào hệ thống dữ liệu.
## Giải thích
+ main.py:
    - Đầu tiên, chương trình chính sẽ là main.py, đây là nơi có chức năng chính đó là hiển thị các nút ấn, giao hiên hệ thống cho chương trình
    - Đầu tiên, ta khởi tạo và import các thư viện cần thiết của chương trình bao gồm, tkinter, và gọi các chương trình khác để lấy dữ liệu từ chúng
    - Tiếp đến khởi tạo một class Game() để lưu trữ, trực quan hóa các hàm
    - Trong clas Game(), khởi tạo phương tức init, tại đó ta sẽ tạo các đối tượng biến và phương thức lấy kích thước màn hình của thiết bị
    - Tiếp theo là phương thức khởi tạo createWindow() sẽ thiết lâpj các thuộc tính của cửa sổ như tiêu đề, màu, kích thước tối thiểu
    - Tiếp theo là phương thức fillRootWindow của lớp Game tại phương thức này ta sẽ tạo ra ba nhãn chứa 3 hình ảnh của chương trình ở các vị trí khác nhau trong cửa sổ, và tạo hai nhẫn để thực hiện việc hiển thị tên chương trình trong cửa sổ
    - Tiếp theo là phương thức makeTabView tạo các tab khác nhau trong cửa sổ giúp bạn có thể di chuyển qua các tab khác nhau
    - Cuối cùng, khởi tạo một đối tượng là G thể hệ lớp Game và gọi phương thức gameLoop để bắt đầu vòng lặp
+ NewStudent.py
        - Chương trình NewStudent.py có chức năng chính đó là giúp cho chương trình main có thể khởi tạo các thông tin hiển thị trong giao diện main.py phần nhập học sinh mới, và chức năng song song theo đó là giúp ta lưu trữ các thông tin học sinh mới đã nhập vào file json với mục đích lưu trữ vào database
        - Khởi tạo một class nStudent(), tại đây ta khơi khởi tạo hàm init với mục đích để khởi tạo các biến để dùng cho các tác vụ tiếp theo, sau đó ta tao các thuộc tính trống khác, mục đích là các phương thức này sẽ được lưu trữ vào file json dùng để làm database cho chương trình
        - Tiếp theo ở hàm labels sẽ khởi tạo cá danh sách nhãn để hiển thị các trường dùng để nhập liệu cho học sinh, tại phương thức này cũng sẽ khởi tạo các thành phần giao diện và được gán cho các biến đã được khai báo ở trên, tiếp theo nó sử dụng place, set, deselect để thiết lập vị trí, giá trị mặc định của các thành phần giao diện
        - Hàm wrtInJson sẽ nhận hai tham số là data và flName, nó sẽ giúp ta ghi dữ liệu vào tệp dưới dạng file json
        - Hàm saveFile lấy các giá trị nhập vào từ phần giao diện cảu lớp nStudent sau đó sẽ tạo một từ điển để chauws các cặp khóa-giá trị tương ứng.
        - Hàm clearInput xóa các giá trị nhập vào từ các thành phần giao diện của lớp nStudent bằng cách sử dụng phương thức delete, deselect, phương thức nayg sẽ được gọi sau khi người dùng nhập thành công hoặc người dùng nhấn nút xóa
        - Hàm svBttnHvr là sự kiện khi con trỏ chuột di chuyển vào nút Lưu, phương thức này thay đổi thuộc tính của đối tượng svBtnLabel, để hiển thị văn bản lưu bản ghi có đường viền và nổi bật, và sử dụng phương thức place để thiết lập vị trí của Lable dưới nút lưu
        - Hàm svBttnLv với các chức năng chính đấy là sự kiện khi con trỏ chuột di chuyển ra khỏi nút lưu, phương thức này trả lại thuộc tính svBtnLabel vè ban đầu, không có đường viền văn bản hay nổi bật, đồng thời cũng sử dụng phương thức place để thiết lập vị trí của Label ẩn đi
        - cuối cùng là Hàm bttns khởi tạo hai đối tượng là button có chức năng lưu trữ và dữ liệu học sinh và xóa các giá trị được nhập vào khi nhấn
+ DisplayCourse.py 
            - Với chức năng chính là để hiện thị dữ liệu của cá khóa học
            - Ở đây, ta cũng khởi tạo một giao diện cửa sổ tkinter và đặt đường dẫn đến file Course.json
            - Hàm makeTable và fillTable cho phép ta khai báo các giá trị, khởi tạo 2 cột để hiển thị ID khóa học và tên khóa học, sau đó hàm fillTable sẽ giúp ta đọc dữ liệu từ file Course.json và xuất dữ liệu đó trên màn hình hiển thị dữ liệu khóa học 
            - Hàm shwStd, shwBttn, table sẽ giúp ta khởi tạo font chữ, màu sắc sau đó khởi tạo một nút nhấn giúp người dùng có thể xem danh sách các khóa học
+ Display.py
                - Với chức năng chính đóng vai trò là một hàm hiển thị dự liệu học sinh từ file Student.json vào các ô văn bản đã được khởi tạo từ trước đó
                - Với cấu trúc và khởi tạo các hàm tương tự với file DisplayCourse đã được khởi tạo trước đó
+ CourseCreate.py
                    - Với chức năng giúp người dùng có thể tạo thêm khóa học cho chương trình dạy
                    - Ở đây việc khai báo hàm giống như 2 chương trình trên
+ AllocateCourse.py
                        - Với chức năng có thể giúp giảng viên phân bổ khóa học đến với các học sinh bằng thao tác nhập ID học sinh và đưa click chọn khóa học
                        - Với cấu trúc khởi tạo và hàm cũng tương tự với 3 chương trình trên


<img src="https://i.imgur.com/w947S40.png" alt="Alt text">

