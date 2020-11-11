import arrow
import logging

from hashlib import sha3_256

from .models import Poll, Vote


logger = logging.getLogger(__name__)


def hash_creation_for_votes(user: "apps.users.User") -> str:
    # TODO : create secret key to update hash
    sign = sha3_256()
    sign.update(b"{username}".format(username=user.username))
    return str(sign.hexdigest())


def make_vote(user: "apps.user.User", poll: Poll, option: str) -> bool:
    """
    :param user:
    :param poll:
    :return: status -> bool, returns if vote was created or not.
    First check if poll is still available.
    Then generate sign.
    At last save Vote referenced to the Poll.
    """
    status = False
    starting_time = arrow.utcnow() # freeze time to avoid race conditions
    if poll.start_time < starting_time < poll.end_time:
        logger.info(f"Creating valid Vote at {arrow.utcnow}")
        hash_value = hash_creation_for_votes(user=user)
        vote = Vote()
        vote.sign = hash_value
        vote.poll = Poll()
        vote.option = option
        vote.save()
        status = True
    return status
