## Crypto - RSA - Chinese Remainder Theorem

Nguồn: Đề Admin tự chế

[Source code](https://github.com/hackingeveryday/hacking.github.io/blob/gh-pages/crypto/RSA/CRT/chall.py)

### Mô tả đề bài

* **7 cặp khóa bí mật `(p, q)`**
* **7 cặp khóa công khai `(e, n)` trong đó có chung `e = 7`**
* 7 bản mã từ cùng plaintext `c = m**e % n` với `m == FLAG`

### Cách giải

Để giải được thì ta đọc thêm về [Định lý số dư Trung Hoa](https://vi.wikipedia.org/wiki/%C4%90%E1%BB%8Bnh_l%C3%BD_s%E1%BB%91_d%C6%B0_Trung_Qu%E1%BB%91c)

Theo lý thuyết, nếu ta tìm được đủ `e` bộ số `n` (với điều kiện `GCD(nx, ny) == 1`, trong đó `nx, ny` là 2 số bất kỳ khác nhau trong bộ số `n`) thì hoàn toàn có thể tìm được plaintext `m` (do ta tìm được `m**e`)

Ví dụ cho `e = 3` và:
* `c1 = m**e % n1`
* `c2 = m**e % n2`
* `c3 = m**e % n3`

Vậy ta sẽ tìm được **`m**e == m**3`** => Solved.

Trong bài này `e = 7`

[Solve](https://github.com/hackingeveryday/hacking.github.io/blob/gh-pages/crypto/RSA/CRT/CRT.py)