from matplotlib import pyplot as plt
import numpy as np
import os
from PIL import Image
from rawkit.raw import Raw

dirname = os.path.realpath('.')
imageDir = dirname + '\\RECORD.RAW'

filename = '/path/to/your/image.cr2'
raw_image = Raw(filename)
buffered_image = np.array(raw_image.to_buffer())
image = Image.frombytes('RGB', (raw_image.metadata.width, raw_image.metadata.height), buffered_image)
image.save('/path/to/your/new/image.png', format='png')