from pxsstray import run


class DPMSSettings:
    def __init__(self, enabled, standby, suspend, off):
        self.enabled = enabled
        self.standby = standby
        self.suspend = suspend
        self.off = off

    def Apply(self, force=False):
        cmd = ["xset", "dpms", self.standby, self.suspend, self.off]
        return run.run(cmd)

    def Parse(xset_output: str):
        return DPMSSettings()


class XSettings:
    def __init__(self, dpms):
        self.dpms = dpms


def xset_q():
    settingsText = run.run(["xset", "q"])
    return settingsText
