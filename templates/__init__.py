from datetime import datetime
from starlette.templating import Jinja2Templates

from conf import TEMPLATES_DIR

# Initialize Jinja2Templates with the directory containing the templates
tpl = Jinja2Templates(directory=TEMPLATES_DIR)
tpl.env.globals["current_year"] = lambda: datetime.utcnow().year
