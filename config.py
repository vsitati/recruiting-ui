class Config:
    env_config = {
        "browser": "chrome",
        "headless_mode": False,
        "timeout": 20,
        "poll_frequency": 0.5,
        "log_path": "./logs",
        "path_to_resumes": "test_data/resumes",
        "env": {
            "ats": {
                "endpoints": {
                    "openadmin": "/openadmin",
                    "ats_login": "/"
                },
                "url": {
                    "protocol": "https",
                    "domain": "-openhire.silkroad-eng.com"
                }
            },
            "cx": {
                "endpoints": {
                    "admin": "/admin"
                },
                "url": {
                    "protocol": "https",
                    "domain": "cx-qa.silkroad-eng.com"
                }
            },
            "utility": {
                "env": "srerecruit01",
                "endpoints": {
                    "mailbox": "/mailbox/index/environment/sreqadevelop"
                },
                "url": {
                    "protocol": "http",
                    "domain": ".silkroad-eng.local"
                }
            }
        }
    }
