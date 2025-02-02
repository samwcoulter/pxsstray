from subprocess import run as srun


def run(cmd):
    output = srun(cmd, text=True, capture_output=True)
    if len(output.stderr) > 0:
        raise Exception(output.stderr)
    return output.stdout
