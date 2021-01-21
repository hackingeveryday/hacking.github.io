## Crypto - RSA - Confused

Nguồn: Đề Admin tự chế

[Source code](https://github.com/hackingeveryday/hacking.github.io/blob/gh-pages/crypto/RSA/confused/chall.py)

### Mô tả đề bài

* `(p)` : khóa bí mật
* **`(e, n)`** : khóa công khai với **`e = 6996`** và **`n = p**3`**
* `c = m**e % n` : ciphertext với FLAG là `m`

### Cách giải

Từ `n = p**3` tìm được `p` (sử dụng `http://factordb.com/`):
* Euler's totient : ***`phi = (p-1) * (p**2)`***
* Dễ dàng tìm được `d = inverse(e, phi)` và `pow(c, d, n)`

Nhưng chưa thể tìm ra được `FLAG`. Đó là do `GCD(e, phi) != 1`. Khi đó:
* Nếu `GCD(e, phi) == 1` thì `d = inverse(e, phi)` => `d*e = k*phi + 1`
  * `pow(c, d, n) = m**(k*phi + 1) % n = m % n`
* Nếu ***`GCD(e, phi) == x (x != 1)`***. Đặt:
  * `e = a*x` và `phi = b*x` khi đó `GCD(a, b) == 1`
  * `d = inverse(e, phi)` => ***`d == inverse(a, b)`*** => ***`e*d % b == a*x*a**(-1) % b == x % b`***
  * Vậy ***`e*d == k*phi + x`*** hay ***`e*d == k*phi + GCD(e, phi)`***

Hướng giải cụ thể:
* Tính `d = inverse(e, phi)` và lấy `m1 = pow(c, d, n)`. Khi đó ***`m1 = m**x % n`***
* Cuối cùng ta sẽ lấy căn bậc `x` của `m1` trong `n`
  * TH1 : Nếu `m` và `x` nhỏ, có thể căn trực tiếp `m1` ra `m` (tương tự dùng `http://factordb.com/`)
  * TH2: Nếu `x` chẵn, tính `square root` của `m1` trong `n` đến khi đủ nhỏ để áp dụng TH1

[Solve](https://github.com/hackingeveryday/hacking.github.io/blob/gh-pages/crypto/RSA/confused/solve.py)