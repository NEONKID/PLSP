import os

from czifile import CziFile
from pyvips import Image


class CZI:
    filename = None
    czi = None

    def __init__(self, path):
        self.filename = path
        self.czi = CziFile(path)

    @classmethod
    def getPixelArray(cls):
        im = cls.czi.asarray()

        print('Image Width: {}'.format(im.shape[-1]))
        print('Image Height: {}'.format(im.shape[-2]))

        return im[0, 0, 0,]

    @classmethod
    def cvtStandardImgFormat(cls, savePath, fmt, compression=False):
        im_arr = cls.getPixelArray()

        if fmt.endswith('jpg') and im_arr[0] > 65535 and im_arr[1] > 65535:
            print('Too Large size for JPEG-2000 format...')
            return

        elif fmt.endswith('png') and im_arr[0] > 10000 and im_arr[1] > 10000:
            print('Too Large size for PNG format...')
            return

        fname = os.path.basename(cls.filename)
        sname = os.path.splitext(fname)[-1]

        im = Image.new_from_array(im_arr)

        if fmt.endswith('tiff'):
            if compression:
                im.write_to_file(savePath + '/' + sname + '.' + fmt, compression='lzw')
            else:
                im.write_to_file(savePath + '/' + sname + '.' + fmt, compression='lzw')
        else:
            im.write_to_file(savePath + '/' + sname + '.' + fmt)
