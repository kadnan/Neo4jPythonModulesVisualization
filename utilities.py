from subprocess import PIPE, run
import pkg_resources


def get_pip_list():
    installed_packages = {d.project_name: d.version for d in pkg_resources.working_set}
    return installed_packages


# This function executed pip show command and return all dependents after parsing.
def get_package_detail(name):
    result = run("pip show {}".format(name), stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    detail = result.stdout
    detail_parts = detail.split('\n')
    dependents = []

    for part in detail_parts:
        if part != '' and 'Required-by' in part:
            part = part.replace('Required-by:', '').strip()
            part = part.replace(' ', '')
            dependents = part.split(',')
    return dependents
