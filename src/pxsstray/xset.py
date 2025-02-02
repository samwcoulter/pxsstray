from subprocess import run


def xset_q():
    cmd = run(["xset", "q"], text=True, capture_output=True)
    return cmd.stdout
