from django.shortcuts import render
from django.http import HttpResponse
import requests


def get_repositories(username, repo_count):
    url = 'https://api.github.com/orgs/'+username+'/repos'
    arr = []

    # Header is added otherwise Github api reponds unauthorized access
    header = {
        'User-Agent': 'Mohitbalwani26'
    }

    all_repos = requests.get(url, headers=header)

    if all_repos.status_code == 403:
        return []

    for repo in all_repos.json():
        arr.append((repo['html_url'], repo['forks_count'], repo['full_name']))

    # Sorting according to the number of forks in descending order.
    arr.sort(key=lambda x: x[1], reverse=True)

    # returning top repo_count(provided by user) repositories
    return arr[:repo_count]


def get_contributors(all_repos, contributors_count):
    r''' Here the basic idea is to extract all the contributors upto contriutors_count(provided by user)
        There is limitation of getting upto only top 500 contributors from github api.
        In this function we are requesting 100 contributors per page'''

    # Basically a hashmap to store repositiory name with its contributors list.
    dictionary = {}

    header = {
        'User-Agent': 'Mohitbalwani26'
    }

    # It automatically returns the contributors in desceding order by number of commits.
    for repo in all_repos:
        pages = contributors_count//100  # Denotes the limit upto which page it has to go
        remaining_slot = contributors_count % 100
        dictionary[repo[2]] = []
        for number in range(1, pages+1):
            url = 'https://api.github.com/repos/{name}/contributors?page={number}&per_page=100'.format(
                number=number, name=repo[2])
            contributors_of_that_page = requests.get(url, headers=header)
            for contributor in contributors_of_that_page.json():
                dictionary[repo[2]].append(
                    (contributor['login'], contributor['html_url'], contributor['contributions']))

        remaining_url = 'https://api.github.com/repos/{name}/contributors?page={number}&per_page=100'.format(
            number=pages+1, name=repo[2])
        contributors_of_that_page = requests.get(remaining_url, headers=header)
        for contributor in contributors_of_that_page.json():
            if remaining_slot == 0:
                break
            dictionary[repo[2]].append(
                (contributor['login'], contributor['html_url'], contributor['contributions']))
            remaining_slot -= 1

    return dictionary


def combine(top_repos, dictionary):
    arr = []
    for repo in top_repos:
        arr.append((repo[0], repo[1], repo[2], dictionary[repo[2]]))
    return arr


def home(request):
    context = {}
    error = ''
    if request.method == 'POST':
        org_name = request.POST.get('organisation_name')
        try:
            # Type conversion because post method returns it in string.
            repo_count = int(request.POST.get('number_of_repositories'))
            contributors_count = int(
                request.POST.get('number_of_contributors'))
        except:
            repo_count = ''
            contributors_count = ''
            error = 'Enter valid number'
        context['org_name'] = org_name
        context['repo_count'] = repo_count
        context['contributors_count'] = contributors_count

        try:
            top_repos = get_repositories(org_name, repo_count)
            top_contributors = get_contributors(top_repos, contributors_count)
            context['top_repos'] = combine(top_repos, top_contributors)
            context['actual_length_repo'] = len(top_repos)
            if top_repos == []:
                error = 'Api limit has exceeded, Try again after some time.'

        except:

            error = 'Enter valid organisation handle'
            context['top_repos'] = []

        context['error'] = error

    return render(request, 'gitoogle/index.html', context=context)
