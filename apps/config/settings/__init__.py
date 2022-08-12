# settings/__init__.py
import os

# 환경 변수에 저장된 값을 불러옴
SETTINGS_MODULE = os.environ.get('DJANGO_SETTINGS_MODULE')

# 환경 변수가 비어 있거나 'config.settings'일 경우 dev 설정 파일 불러옴
if not SETTINGS_MODULE or SETTINGS_MODULE == 'config.settings':
    from .dev import *

# 환경 변수가 'config.settings.prod'일 경우 prod 설정 파일 불러옴
elif SETTINGS_MODULE == 'config.settings.prod':
    from .prod import *
