import logging
import subprocess

logger = logging.getLogger()

def query(capability_type, instance):
    if capability_type == "devices.capabilities.on_off":
        p = subprocess.run(["ping", "-c", "1", "192.168.0.2"], stdout=subprocess.PIPE)
        state = p.returncode == 0
        return state, "on" # State and instance

def action(capability_type, instance, value, relative):
    if capability_type == "devices.capabilities.on_off":
        if value:
            logger.debug("sending WoL to PC")
            subprocess.run(["wakeonlan", "-i", "192.168.0.255", "00:11:22:33:44:55"])
        else:
            logger.debug("sending shutdown command to PC")
            subprocess.run(["sh", "-c", "echo shutdown -h | ssh clust@192.168.0.2"])
        return "DONE"
