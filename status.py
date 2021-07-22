from enum import Enum


class Status(Enum):
    ACCEPTED = 0
    ATTEMPTED = 1
    NOT_ATTEMPTED = 2


status_classes = {Status.ACCEPTED: 'task-score icon full',
                  Status.ATTEMPTED: 'task-score icon zero',
                  Status.NOT_ATTEMPTED: 'task-score icon'}
