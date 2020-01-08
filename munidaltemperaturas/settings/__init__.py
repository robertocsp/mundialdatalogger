from .base import *


if os.environ.get('PROJECT_PRODUCTION', False):
    from .prod import *
elif os.environ.get('PROJECT_HOMOLOGA', False):
    from .homologa import *
else:
    from .dev import *