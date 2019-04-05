from fabric import task
from .fabutils import *


@task
def uptime(c):
    """
    Run uptime command on remote host - for testing connection.
    """
    c.run("uptime")


@task
def deploy(c):
    """ Deploy application with packaging in mind """
    version = get_version(c)

    pip_path = os.path.join(
        REMOTE_PROJECT_LOCATION, version, 'bin', 'pip'
    )

    if not c.run(f"test -d {REMOTE_PROJECT_LOCATION}", warn=True):
        # it may not exist for initial deployment on fresh host
        c.run(f"mkdir -p {REMOTE_PROJECT_LOCATION}")

    with c.cd(REMOTE_PROJECT_LOCATION):
        # create new virtual environment using venv
        c.run(f'python3 -m venv {version}')

        c.run(f"{pip_path} install webxample=={version} --index-url {PYPI_URL}")


    switch_versions(c, version)
    # let's assume that Circus is our process supervision tool
    # of choice.
    c.run('circusctl restart webxample')