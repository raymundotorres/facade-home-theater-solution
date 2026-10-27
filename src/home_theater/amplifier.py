class Amplifier:
    def on(self):
        return "amplifier:on"

    def off(self):
        return "amplifier:off"

    def set_volume(self, level):
        return f"amplifier:volume:{level}"
