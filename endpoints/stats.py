from utils.stat_utils import stats

def run():
    return {
        "all": stats.total.count,
        "java": stats.java.count,
        "modded": {
            "lexforge": stats.modded.lexforge.count,
            "neoforge": stats.modded.neoforge.count
        },
        "plugin": {
            "bukkit": stats.plugin.bukkit.count,
            "spigot": stats.plugin.spigot.count,
            "paper": stats.plugin.paper.count,
            "purpur": stats.plugin.purpur.count,
            "pufferfish": stats.plugin.pufferfish.count
        },
        "multi_threaded": {
            "folia": stats.multi_threaded.folia.count,
            "lumina": stats.multi_threaded.lumina.count
        },
        "proxies": {
            "velocity": stats.proxies.velocity.count,
            "waterfall": stats.proxies.waterfall.count,
            "bungeecord": stats.proxies.bungeecord.count
        }
    }