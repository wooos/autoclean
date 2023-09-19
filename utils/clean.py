import os
import glob
import gzip
import logging
from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from .config import CleanConfig

logging.basicConfig(level=logging.INFO, format='[%(levelname)s][%(asctime)s] %(message)s')
log = logging.getLogger(__name__)


class CleanAction(object):
    def __init__(self, config_file):
        if not os.path.exists(config_file):
            exit('No such file: {}'.format(config_file))
        self.clean_config = CleanConfig(config_file)

    @staticmethod
    def clean(clean_path):
        """

        :param clean_path: <CleanPath>
        :return:
        """
        for filename in glob.glob(r'{}/{}'.format(clean_path.directory, clean_path.filename)):
            mtime = datetime.utcfromtimestamp(os.stat(filename).st_mtime)
            now_time = datetime.utcnow()
            if mtime + timedelta(days=clean_path.expire) < now_time:
                if clean_path.command == 'gzip':
                    if filename.endswith('.gz'):
                        continue
                    log.info('Clean file: {}, command: gzip'.format(filename))
                    with open(filename, 'rb') as f:
                        g = gzip.GzipFile(mode='wb', compresslevel=9, fileobj=open('{}.gz'.format(filename), 'wb'))
                        g.write(f.read())
                        g.close()
                    os.remove(filename)
                elif clean_path.command == 'remove':
                    log.info('Clean file: {}, command: remove'.format(filename))
                    os.remove(filename)
                else:
                    exit('Unknown command: {}, only support gzip and remove'.format(clean_path.command))

    def run(self):
        for clean_path in self.clean_config.paths:
            self.clean(clean_path)

    def cron(self):
        scheduler = BlockingScheduler()
        scheduler_l = self.clean_config.schedule.split()
        scheduler.add_job(self.run, 'cron', minute=scheduler_l[0], hour=scheduler_l[1],
                          day=scheduler_l[2], month=scheduler_l[3], week=scheduler_l[4])
        scheduler.start()
