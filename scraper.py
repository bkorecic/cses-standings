from bs4 import BeautifulSoup
from status import Status
from utils import get_task_id_from_url
import requests

# Concatenate user id at the end of BASE_SOLVED_URL to get solved tasks url
BASE_SOLVED_URL = 'https://cses.fi/problemset/user/'


def get_user_tasks(user_id):
    url = BASE_SOLVED_URL + user_id
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'lxml')
    result = {}
    accepted = soup.select('td > a.full')
    attempted = soup.select('td > a.zero')
    not_attempted = soup.select("td > a[class='task-score icon']")
    for task in accepted:
        task_id = get_task_id_from_url(task['href'])
        result[task_id] = Status.ACCEPTED
    for task in attempted:
        task_id = get_task_id_from_url(task['href'])
        result[task_id] = Status.ATTEMPTED
    for task in not_attempted:
        task_id = get_task_id_from_url(task['href'])
        result[task_id] = Status.NOT_ATTEMPTED
    return result


def get_chapters():
    req = requests.get('https://cses.fi/problemset')
    soup = BeautifulSoup(req.content, 'lxml')
    # The first tag with .task is not a chapter
    chapters = []
    chapters_html = soup.select('.task-list')[1:]
    for chapter_html in chapters_html:
        name = chapter_html.previous_sibling.text
        tasks_html = chapter_html.select('.task')
        tasks = []
        for task_html in tasks_html:
            a = task_html.find('a')
            task_id = get_task_id_from_url(a['href'])
            task_name = a.text
            tasks.append((task_name, task_id))
        chapters.append((name, tasks))
    return chapters
