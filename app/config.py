import os

config = {
    "server": {
        "port": os.getenv('PORT', 3000),
        "ip": "0.0.0.0"
    },
    "debug":os.getenv('DEBUG', False),
    "cors": {
        "api/*": {"origins": "*"}
    }
}

    
