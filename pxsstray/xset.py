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


def xset_dpms(enable: bool) -> None:
    run.run(["xset", "+dpms" if enable is True else "-dpms"])


def xset_s(enable: bool) -> None:
    run.run(["xset", "s", "on" if enable is True else "off"])
