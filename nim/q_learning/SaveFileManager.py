import os.path as path

SAVEFILE_BASE_PATH = path.dirname(path.realpath(__file__))
SAVEFILE_BASE_PATH = path.join(SAVEFILE_BASE_PATH, 'saveFiles')

class SaveFileManager():
    @staticmethod
    def has_savefile_for_size(pearlsPerRow):
        filePath = SaveFileManager.get_path_of_savefile_for_size(pearlsPerRow)

        if path.isfile(filePath):
            return True
        else:
            return False

    @staticmethod
    def get_path_of_savefile_for_size(pearlsPerRow):
        fileName = "nim"
        for perls in pearlsPerRow:
            fileName += '_'
            fileName += str(perls)
        fileName += '.npy'

        filePath = path.join(SAVEFILE_BASE_PATH, fileName)
        return filePath