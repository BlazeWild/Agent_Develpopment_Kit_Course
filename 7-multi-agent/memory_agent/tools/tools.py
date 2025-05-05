from datetime import datetime

def get_current_time()-> dict:
    """Get the current time and date."""
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
