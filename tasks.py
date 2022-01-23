from invoke import task

@task
def run(c):
    c.run('python3 src/main.py', pty=True)
