from starlette.templating import Jinja2Templates
from config import TEMPLATES_DIR

# Initialize Jinja2Templates with the directory containing the templates
tpl = Jinja2Templates(directory=TEMPLATES_DIR)
