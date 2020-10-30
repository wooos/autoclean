import os
import glob
import gzip
import logging
from datetime import datetime, timedelta
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
                    log.info('gzip file: {}'.format(filename))
                    with open(filename, 'rb') as f:
                        g = gzip.GzipFile(mode='wb', compresslevel=9, fileobj=open('{}.gz'.format(filename), 'wb'))
                        g.write(f.read())
                        g.close()
                    os.remove(filename)
                elif clean_path.command == 'remove':
                    log.info('remove file: {}'.format(filename))
                    os.remove(filename)
                else:
                    exit('Unknown command: {}, only support gzip and remove'.format(clean_path.command))
        log.info('Completion')

    def run(self):
        for clean_path in self.clean_config.paths:
            self.clean(clean_path)
