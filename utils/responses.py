servers = {
    200:
    {
     "content":
     {
      "application/json":
      {
       "example":
        [
            {
                "address": "1.1.1.1",
                "port": 25565,
                "version": "1.21.1",
                "protocol": "767",
                "software": "JAVA",
                "motd": "A Minecraft Server",
                "country": "US",
                "asn": "AS24940 Hetzner Online GmbH",
                "org": "Hetzner Online GmbH",
                "firstseen": 1732377334,
                "lastseen": 1732377334,
                "hostname": "mail.funtimes909.xyz",
                "whitelist": False,
                "cracked": False,
                "enforces_secure_chat": False,
                "prevents_reports": False,
                "icon": "data:image/png;base64,iVBORw0KGg... (base64 encoded image)"
            }
        ]
       }
      },
        "description": "Return Servers"
    },
}

takedown = {
    200:
    {
     "content":
     {
      "application/json":
      {
       "example":
        {
            "success": True
        }
       }
      },
        "description": "Remove a server from the database"
    },
}

random = {
    200:
    {
     "content":
     {
      "application/json":
      {
       "example":
        {
                "address": "1.1.1.1",
                "port": 25565,
                "version": "1.21.1",
                "protocol": "767",
                "software": "JAVA",
                "motd": "A Minecraft Server",
                "country": "US",
                "asn": "AS24940 Hetzner Online GmbH",
                "org": "Hetzner Online GmbH",
                "firstseen": 1732377334,
                "lastseen": 1732377334,
                "hostname": "mail.funtimes909.xyz",
                "whitelist": False,
                "cracked": False,
                "enforces_secure_chat": False,
                "prevents_reports": False,
                "icon": "data:image/png;base64,iVBORw0KGg... (base64 encoded image)"
        }
       }
     },
        "description": "Returns a random server"
    },
}

history = {
    200:
    {
     "content":
     {
      "application/json":
      {
       "example":
        [
            {
            "address": "mc.example.com",
            "playername": "Nucceteere",
            "playeruuid": "1f8a091c-3daa-4dbd-a15f-a3753a6f36b3",
            "lastseen": 1733107822
            },
            {
            "address": "mc.example.com",
             "playername": "Nucceteere",
             "playeruuid": "1f8a091c-3daa-4dbd-a15f-a3753a6f36b3",
             "lastseen": 1731888338
            }
        ]
       }
      },
        "description": "Return Player History"
    },

    422:
    {
     "content":
     {
      "application/json":
      {
        "example":
       {
        "detail": "You can't use both player and address!"
       }
      }
     }
     , "description": "Unprocessable Content"
    },

    403:
    {
     "content":
     {
      "application/json":
      {
        "example":
       {
        "detail": "Forbidden"
       }
      }
     }
     , "description": "Forbidden"
    },

    401:
    {
     "content":
     {
      "application/json":
      {
        "example":
       {
        "detail": "Unauthorized"
       }
      }
     }
     , "description": "Unauthorized"
    }
}

stats = {
    200:
    {
     "content":
     {
      "application/json":
      {
        "example":
        {
            "all": 417519,
            "java": 149253,
            "modded": {
                "lexforge": 65946,
                "neoforge": 16530
            },
            "plugin": {
                "bukkit": 885,
                "spigot": 16585,
                "paper": 55814,
                "purpur": 3807,
                "pufferfish": 364
            },
            "multi_threaded": {
                "folia": 165,
                "lumina": 0
            },
            "proxies": {
                "velocity": 6835,
                "waterfall": 1411,
                "bungeecord": 2820
            }
        }
      }
     }
     , "description": "Return Stats"
    }
}