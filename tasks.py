from invoke import task


@task
def create_environment(c):
    """
    Creates a Conda environment with required dependencies.
    """
    c.run("conda env create -f deploy/conda/env.yml")


@task
def run_flask_app(c):
    """
    Runs the Flask app.
    """
    c.run(
        "source activate flask-environment && pip install -e . && flask --app flaskapp/flask_db run --host=0.0.0.0 --port=8085"
    )


@task(pre=[create_environment])
def deploy(c):
    """
    Deploys the Flask app.
    """
    run_flask_app(c)
