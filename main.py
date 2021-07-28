from bs4 import BeautifulSoup
from status import Status, status_classes
from utils import get_task_id_from_url
from jinja2 import Environment, FileSystemLoader, select_autoescape
from scraper import get_user_tasks, get_chapters
import os
import requests
import copy
import argparse

package_directory = os.path.dirname(os.path.abspath(__file__))

env = Environment(
    loader=FileSystemLoader(searchpath=package_directory),
    autoescape=True
)

template = env.get_template('template.html')


def init_argparse():
    parser = argparse.ArgumentParser(
        description='Generate HTML with CSES standings.'
    )
    parser.add_argument('-u', '--usersfile',
                        default='users.txt',
                        metavar='FILE',
                        help='Get users from FILE')
    parser.add_argument('-o', '--outfile',
                        default='standings.html',
                        metavar='FILE',
                        help='Write the result to FILE')
    return parser


def read_users_file(filename):
    users = []
    with open(filename, 'r') as f:
        for line in f:
            user_id, name = line.rstrip().split(':')
            tmp = get_user_tasks(user_id)
            tmp['name'] = name
            users.append(tmp)
    return users


def main():
    parser = init_argparse()
    args = parser.parse_args()
    users = read_users_file(args.usersfile)
    chapters = get_chapters()
    result = template.render(chapters=chapters,
                             users=users,
                             status_classes=status_classes)
    with open(args.outfile, 'w') as f:
        f.write(result)


if __name__ == "__main__":
    main()
