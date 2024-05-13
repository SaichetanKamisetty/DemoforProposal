# Does not do anything as of 490, this is to show the controller portion of the architecture, and facade.

from model import DetectBubbles, DetectText, TranslateText, ModifyText, ProcessOutput

def process_images(file_loc):
    img_array = []
    return img_array

class TranslateWebtoons():
    def __init__(file_loc): 
        file_loc = file_loc
        processed_images = process_images(file_loc=file_loc)

    def TranslateWebtoon():
        DetectBubbles()
        DetectText()
        TranslateText()
        ModifyText()
        ProcessOutput()
        pass