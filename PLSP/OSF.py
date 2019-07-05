import numpy as np
import os

from openslide import open_slide
from pyvips import Image


class OSF:
    def __init__(self, path):
        self.filename = path
        self.file = Image.new_from_file(path, access='sequential')
        self.slide = open_slide(filename=self.filename)

    def getPixel4Thumbnails(self):
        # Image Thumbnails size
        [size_x, size_y] = slide.level_dimensions[1]	

        # Thumbnails Region
        region = np.array(self.slide.read_region((0, 0), 2, (size_x, size_y)))

        print('Image Thumbnails Width: {0}'.format(size_x))
        print('Image Thumbnails Height: {0}'.format(size_y))

        return region

    def getPixelArray(self):
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
        return np.ndarray(buffer=self.file.write_to_memory(),
                          dtype=format_to_dtype[self.file.format],
                          shape=[self.file.height, self.file.width, self.file.bands])

    def cvtStandardImgFormat(self, savePath, fmt, compression=False):
        if fmt.endswith('jpg') and self.slide.dimensions[0] > 65535 and self.slide.dimensions[1] > 65535:
            print('Too Large size for JPEG-2000 format...')
            return

        elif fmt.endswith('png') and self.slide.dimensions[0] > 10000 and self.slide.dimensions[1] > 10000:
            print('Too Large size for PNG format...')
            return

        fname = os.path.basename(self.filename)
        sname = os.path.splitext(fname)[-1]

        if fmt.endswith('tiff'):
            if compression:
                self.file.write_to_file(savePath + '/' + sname + '.' + fmt, compression='lzw')
            else:
                self.file.write_to_file(savePath + '/' + sname + '.' + fmt, compression='lzw')
        else:
            self.file.write_to_file(savePath + '/' + sname + '.' + fmt)
