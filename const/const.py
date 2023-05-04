import random
import string

number = string.digits
TITLE_FOLDER = 'folder-' + ''.join(random.choice(number) for _ in range(3))
TITLE_FILE = 'file-' + ''.join(random.choice(number) for _ in range(3))

LOGIN = "login"
PASSWORD = "password"