import requests


def get_info_from_all_user_repos(user, *kwargs):
    """
    For a given user, yields a list of the information requested in *kwargs.
    An example: this_function('johndoe', 'name', 'description') will yield
    a list of name and description pertaining to all repositories of the
    user johndoe.

    :param user: the github username, i.e. 'johndoe'
    :param keys: the information you're asking for, i.e. 'name','description'
    :return: yields repo's requested info as a list
    """
    repo_info = get_info_from_repos(user)
    for info in repo_info:
        details = [info.get(key) for key in kwargs]
        yield details


def get_info_from_repos(user):
    repos = get_repos(user)
    repo = yield_unforked_repos(repos)
    yield from repo


def yield_unforked_repos(repos):
    for repo in repos:
        if repo.get('fork') == False:
            yield repo


def get_repos(user):
    url = "https://api.github.com/users/{}/repos".format(user)
    data = get_response_in_json(url)
    return data


def get_response_in_json(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("There was an error in the request")
        return
    return response.json()


if __name__ == '__main__':
    info = get_info_from_all_user_repos(
        'adriaanbd',
        'name',
        'description',
        'language',
        'created_at',
        'updated_at'
    )

    for item in info:
        print(item)