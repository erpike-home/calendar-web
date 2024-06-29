import uvicorn

from app import ChurchCalendar
from utils import parse_args


app = ChurchCalendar()


def main(args):
    uvicorn.run("run:app", reload=args.reload)


if __name__ == "__main__":
    main(parse_args())
