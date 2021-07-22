def get_task_id_from_url(url):
    return int(url.rstrip('/').split('/')[-1])
