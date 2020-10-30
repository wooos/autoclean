import os
import glob
import gzip
from datetime import datetime, timedelta
from .config import CleanConfig


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
            now_time = datetime.now()
            if mtime + timedelta(days=clean_path.expire) < now_time:
                if clean_path.command == 'gzip':
                    with open(filename, 'rb') as f:
                        g = gzip.GzipFile(mode='wb', compresslevel=9, fileobj=open('{}.gz'.format(filename), 'wb'))
                        g.write(f.read())
                        g.close()
                    os.remove(filename)
                elif clean_path.command == 'rm':
                    os.remove(filename)
                else:
                    exit('Unknown command: {}, only support gzip and rm'.format(clean_path.command))

    def run(self):
        for clean_path in self.clean_config.paths:
            self.clean(clean_path)
