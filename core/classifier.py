
class Classifier:
    """
    Classifying different file types (example: JPEG, PNG, GIF...etc)
    """

    file_types = {
        "image": [
            '.jpg',
            '.png',
            '.gif',
            '.webp',
            '.tiff',
            '.psd',
            '.raw',
            '.bmp',
            '.heif',
            '.indd',
            '.jpeg',
            '.ai',
            '.ps',
            '.ico',
            '.svg',
            '.tif',
        ],
        "document": [
            '.pdf',
            '.docx',
            '.xlsx',
            '.doc',
            '.html',
            '.htm',
            '.odt',
            '.xls ',
            '.ods',
            '.ptt',
            '.pptx',
            '.txt'
        ],
        "video": [
            '.webm'
            '.mpg',
            '.mp2',
            '.mpeg',
            '.mpe',
            '.mpv',
            '.ogg',
            '.mp4',
            '.m4p',
            '.m4v',
            '.avi',
            '.wmv',
            '.mov',
            '.qt',
            '.flv',
            '.swf',
            '.avchd'
        ],
        "audio": [
            '.aif',
            '.cda',
            '.mid',
            '.midi',
            '.mp3',
            '.mpa',
            '.ogg',
            '.wav',
            '.wma',
            '.wpl'
        ],
        "compressed": [
            '.7z',
            '.arj',
            '.deb',
            '.pkg',
            '.rar',
            '.rpm',
            '.tar.gz',
            '.z',
            '.zip'
        ],
        "data": [
            '.csv',
            '.dat',
            '.db',
            '.dbf',
            '.log',
            '.mdb',
            '.sav',
            '.sql',
            '.tar',
            '.xml',
        ],
        "disc": [
            '.bin',
            '.dmg',
            '.iso',
            '.vcd',
            '.toast'
        ],
        "executables": [
            '.apk',
            '.bat',
            '.bin',
            '.cgi',
            '.com',
            '.exe',
            '.jar',
            '.msi',
            '.wsf',
            '.pl',
            '.py',
            '.gadget'
        ],
        "font": [
            '.fnt',
            '.fon',
            '.otf',
            '.ttf'
        ]
    }

    @staticmethod
    def file_class(file):
        file_class = "other"
        for file_type in Classifier.file_types:
            if file.file_extension in Classifier.file_types[file_type]:
                file_class = file_type

        return file, file_class
