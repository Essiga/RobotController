class Behavior:
    def __init__(self):
        self.state = "none"
        self.resolX, self.resolY = 64, 64

    def is_applicable(self, robot):
        pass

    def execute(self, robot):
        pass

    def detect_box(self, image):
        """
            looks in current image for a black blob on a red background, from left to right
            :param
                    resolX, resolY: int
                        image resolution in pixel
                    image: PIL.Image
                        a rgb image with black blobs on red background
                    xCenter: [int]
                        the center of the image: result of the function

            :return: true,  if black blob found
            """
        minBlobWidth = 5
        xStart = -1
        xCenter = [-1]
        for y in range(self.resolY):
            blobwidth = 0
            for x in range(self.resolX):
                pixel = image.getpixel((x, y))
                if pixel == (0, 0, 0):  # black pixel: a box!
                    blobwidth += 1
                    if blobwidth == 1:
                        xStart = x
                else:
                    if blobwidth >= minBlobWidth:
                        xCenter[0] = xStart + blobwidth / 2
                        # print('blob detected at: ', xStart, y, ' with center at: ', xCenter[0])
                        return True
                    elif blobwidth > 0:
                        blobwidth = 0
            if blobwidth >= minBlobWidth:
                xCenter[0] = xStart + blobwidth / 2
                # print('blob detected at: ', xStart, y, ' with center at: ', xCenter[0])
                return True

        return False