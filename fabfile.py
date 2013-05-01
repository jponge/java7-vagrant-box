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
    deb.upgrade()

@task
def provision_glassfish():
    require.file('glassfish.zip', url='http://download.java.net/glassfish/3.1.2.2/release/glassfish-3.1.2.2.zip')
    run('unzip -o glassfish.zip')
