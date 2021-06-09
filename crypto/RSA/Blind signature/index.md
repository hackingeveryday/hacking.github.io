## Crypto - RSA - Blind signature

Sau một thời gian dài không biết làm gì thì hôm nay mình nói về chức năng thực tế của RSA đó là tạo các chữ ký điện tử, sau đây là tổng quan về ký và một lỗ hổng cơ bản của một service

Nguồn: cryptohack.org

[Source code](https://github.com/hackingeveryday/hacking.github.io/blob/gh-pages/crypto/RSA/Blind%20signature/chall.py)

### Mô tả đề bài

Đây là một service đơn giản có tác dụng ký các message của user. Đối với admin, sẽ có một message riêng là `ADMIN_TOKEN = "admin=True"`, service verify được admin sẽ trả về FLAG

* Cặp khóa công khai `(e, n)`
* **Người dùng được ký một message `m` bất kỳ**

### Cách giải

Ta xem thêm về nguyên tắc chung trong việc ký một message `m`

* Người dùng gửi lên một message `m`
* Bên ký kiểm tra tính hợp lệ của `m`, nếu đúng sẽ trả về `s = m**d mod n` và `(e, n)`
* Người dùng gửi lên chữ ký và message `(s, m)`
* Bên ký lấy `m1 = s**e mod n`. Nếu `m1 == m` thì đây là message hợp lệ, còn không sẽ không hợp lệ

Do message người dùng gửi lên không bị validate hay filter gì nhiều nên ta có thể lấy được chữ ký của `ADMIN_TOKEN` dựa vào một cặp `(s, m)` khác. Sau khi đã biết `(e, n)`, ta thực hiện như sau:

* Chọn ra một số `k`, tính **`x = k**e mod n`**. Sau đó tính và gửi message `m = x*ADMIN_TOKEN mod n`. Message này hợp lệ do `m != ADMIN_TOKEN`
* Sau khi ký được `s`. Ta tính **`S = s*inverse(2, n) mod n`**
* **`s = m**d == (x*ADMIN_TOKEN)**d == ADMIN_TOKEN**d * x**d == ADMIN_TOKEN**d * 2**(ed) == 2*ADMIN_TOKEN**d [mod n]`** nên `S` chính là chữ ký của `ADMIN_TOKEN`

Thường chọn `k == 2`

[Solve](https://github.com/hackingeveryday/hacking.github.io/blob/gh-pages/crypto/RSA/Blind%20signature/solve.py)

Do tính chất công việc, có lẽ mình sẽ kết thúc series CTF này tại đây. Các thông tin khác mình sẽ thông báo trên page sau. Xin cảm ơn những người đã ủng hộ page trong thời gian qua

Mọi thắc mắc các bạn cứ inbox trực tiếp với page, sẽ có người giải đáp cho các bạn