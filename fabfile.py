from fabric.api import *
from fabtools.vagrant import vagrant
from fabtools import require, deb

@task
def provision():
    require.file('.vimrc', source='vimrc')
    require.deb.packages([
        'build-essential',
        'openjdk-7-jdk',
        'maven',
        'ant',
        'rake',
        'git',
        'vim'
        ], update=True)
