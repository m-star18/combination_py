# combination_py

[![BuildStatus][build-status]][ci-server]
[![PackageVersion][pypi-version]][pypi-home]
[![Stable][pypi-status]][pypi-home]
[![Format][pypi-format]][pypi-home]
[![License][pypi-license]](LICENSE)

[build-status]: https://travis-ci.com/m-star18/combination_py.svg?branch=master
[ci-server]: https://travis-ci.org/m-star18/combination_py
[pypi-version]: https://badge.fury.io/py/combination-py.svg
[pypi-license]: https://img.shields.io/pypi/l/combination-py.svg
[pypi-status]: https://img.shields.io/pypi/status/combination-py.svg
[pypi-format]: https://img.shields.io/pypi/format/combination-py.svg
[pypi-home]: https://badge.fury.io/py/combination-py
[python-home]: https://python.org

Python package for combination calculation

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install combination_py.

```bash
pip install combination-py
```

## Usage

```python
import combination

# combination.Combination(n_max, mod=10**9+7)
comb = combination.Combination(10 ** 6)

# comb.nCr(n, r)
comb.nCr(10, 5) # return 252

# comb.nPr(n, r)
comb.nPr(10, 5) # return 30240

# comb.nHr(n, r)
comb.nHr(10, 5) # return 2002

# 上昇階乗冪 n * (n + 1) * ... * (n + r - 1)
# comb.rising_factorial(n, r)
comb.rising_factorial(10, 5) # return 240240

# 第1種スターリング数
# n要素をk個の巡回列に分割する場合の数
# comb.stirling_first(n, k)
comb.stirling_first(10, 5) # return 269325

# 第2種スターリング数
# n要素を区別のないkグループに分割する場合の数
# comb.stirling_second(n, k)
comb.stirling_second(10, 5) # return 42525

# n要素を区別のあるkグループに分割する場合の数
# comb.balls_and_boxes_3(n, k)
comb.balls_and_boxes_3(10, 5) # return 5103000

# ベルヌーイ数
# comb.bernoulli(n)
comb.bernoulli(10) # return 348484851

# n要素をk個の空でない順序付き集合に分割する場合の数
# comb.lah(n, k)
comb.lah(10, 5) # return 3810240

# n要素をkグループ以下に分割する場合の数
# comb.bell(n, k)
comb.bell(10, 5) # return 86472
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
