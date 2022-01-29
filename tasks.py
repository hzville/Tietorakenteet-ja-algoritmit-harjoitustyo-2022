from invoke import task

@task
def run(c):
    c.run('python3 src/main.py', pty=True)

@task
def test(c):
    c.run('pytest src')

@task
def coverage(c):
    c.run('coverage run --branch -m pytest src; coverage html')

@task
def pylint(c):
    c.run('pylint src')