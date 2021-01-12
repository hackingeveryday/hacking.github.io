## Crypto - RSA - Binomial

Nguồn: Sinh viên An toàn thông tin 2020 - Sơ khảo (*có một chút thay đổi so với đề gốc*)

[Source code](https://github.com/hackingeveryday/hacking.github.io/blob/gh-pages/crypto/RSA/binomial/zozo.py)

### Mô tả đề bài

* `(p, q)` : khóa bí mật
* `(e, n)` : khóa công khai với `e = 65537` và `n = p * q`
* `c = m**e % n` : ciphertext với FLAG là `m`
* **`a = 2020**(p+q) % n`** và **`b = (2020 + p)**q % n`**

### Cách giải

Từ hai số `a` và `b` ta có thể tìm được khóa bí mật `(p, q)` bằng cách giải nhị thức modulo. Ta có:
* ***`b % p`*** `== ((2020 + p)**q % n) % p == (2020 + p)**q % p ==` ***`2020**q % p`***
  * vì `n % p = 0` và `(2020 + p)**q == 2020**q + p*(...)`
* ***`a % p`*** `== 2020**(p+q) % p == (2020**p)*(2020**q) % p ==` ***`2020**(q+1) % p`***
  * vì `2020**p % p == 2020`
* **Vậy `a == 2020*b % p => (a - 2020**b) % p = 0` hay `GCD(a - 2020*b, n) == p` và `q = n // p`**
  * do `a - 2020*b` và `n` cùng chia hết cho `p`

[Solve](https://github.com/hackingeveryday/hacking.github.io/blob/gh-pages/crypto/RSA/binomial/solve.py)