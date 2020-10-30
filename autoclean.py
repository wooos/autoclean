import sys
from utils import CleanAction


if __name__ == '__main__':
    if len(sys.argv) < 2:
        config_file = '/etc/autoclean/autoclean.yaml'
    else:
        config_file = sys.argv[1]
    ca = CleanAction(config_file)
    ca.cron()
