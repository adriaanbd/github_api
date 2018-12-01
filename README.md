# About

This repo is just a place to experiment with the GitHub API.

The `user_repos.py` script gets a list of all repositories from a provided username, and retrieves information such as *name*, *description*, *programming language*, *date created* and *date updated* for each repository that belongs to the user (hasn't been forked). For example, `get_info_from_all_user_repos('johndoe', 'name', 'description')` will retrieve the name and description of all repositories of johndoe.

To know what information you can ask for after the username, check out the GitHub API page [here](https://developer.github.com/v3/), but more specifically the list user repositories section [here] (https://developer.github.com/v3/repos/#list-user-repositories).