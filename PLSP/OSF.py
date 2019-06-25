import numpy as np
import os

from openslide import open_slide
from pyvips import Image


class OSF:
    filename = None
    file = None
    slide = None

    def __init__(self, path):
        self.filename = path
        self.file = Image.new_from_file(path, access='sequential')
        self.slide = open_slide(filename=self.filename)

    @classmethod
    def getPixel4Thumbnails(cls):
        Factors = cls.slide.level_downsamples
        [w, h] = cls.slide.dimensions

        # Image Thumbnails size
        size_x = int(w * (Factors[0] / Factors[2]))
        size_y = int(h * (Factors[0] / Factors[2]))

        # Thumbnails Region
        region = np.array(cls.slide.read_region((0, 0), 2, (size_x, size_y)))

        print('Image Thumbnails Width: {0}'.format(size_x))
        print('Image Thumbnails Height: {0}'.format(size_y))

        return region

    @classmethod
    def getPixelArray(cls):
        format_to_dtype = {
            'uchar': np.uint8,
            'char': np.int8,
            'ushort': np.uint16,
            'short': np.int16,
            'uint': np.uint32,
            'int': np.int32,
            'float': np.float32,
            'double': np.float64,
            'complex': np.complex64,
            'dpcomplex': np.complex128,
        }
        return np.ndarray(buffer=cls.file.write_to_memory(),
                          dtype=format_to_dtype[cls.file.format],
                          shape=[cls.file.height, cls.file.width, cls.file.bands])

    @classmethod
    def cvtStandardImgFormat(cls, savePath, fmt, compression=False):
        if fmt.endswith('jpg') and cls.slide.dimensions[0] > 65535 and cls.slide.dimensions[1] > 65535:
            print('Too Large size for JPEG-2000 format...')
            return

        elif fmt.endswith('png') and cls.slide.dimensions[0] > 10000 and cls.slide.dimensions[1] > 10000:
            print('Too Large size for PNG format...')
            return

        fname = os.path.basename(cls.filename)
        sname = os.path.splitext(fname)[-1]

        if fmt.endswith('tiff'):
            if compression:
                cls.file.write_to_file(savePath + '/' + sname + '.' + fmt, compression='lzw')
            else:
                cls.file.write_to_file(savePath + '/' + sname + '.' + fmt, compression='lzw')
        else:
            cls.file.write_to_file(savePath + '/' + sname + '.' + fmt)
