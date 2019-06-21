<h1 align="center">Welcome to pathology-large-size-processing-module 👋</h1>
<p>
  <img src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/NEONKID/PLSP#readme">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" target="_blank" />
  </a>
  <a href="https://github.com/NEONKID/PLSP/graphs/commit-activity">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" target="_blank" />
  </a>
</p>

> Large size Pathology Image Processing Module



## Install

This package recommends Python 3.5 or later.

```bash
pip install git+https://github.com/NEONKID/PLSP.git
```



## Author

👤 **Kwang Soo Jeong**

* Github: [@NEONKID](https://github.com/NEONKID)



## 🚀 Usage

Use the **vips** library to read images over 65,000 pixels.

```python
from PLSP import OSF

path = '.svs'
oslide = OSF(path)
```

This code is used in formats supported by **OpenSlide**

```python
import matplotlib.pyplot as plt

im = oslide.getPixelArray()

plt.imshow(im)
plt.show()
```

If you use the **getPixelArray** method to extract pixel data in the form of **numpy**, you can easily see it using Pyplot.


## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/NEONKID/PLSP/issues).

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_