# pylint: disable=W0401,W0614,C0114

from skyant.tools.duty.general import *  # noqa=F403
from skyant.tools.duty.venv import *  # noqa=F403
from skyant.tools.duty.pypi import *  # noqa=F403

from duty import duty
import yaml


@duty
def pypireq2env(ctx):
    '''
    Installed requirements from python packages source to current environment.
    '''

    with open('setup.yml', 'r', encoding='utf-8') as vars_file:
        conf = yaml.safe_load(vars_file)

    list_packages = ' '.join(conf.get('REQUIREMENTS', ''))

    if len(list_packages) > 0 and list_packages[0] != '':
        ctx.run(f'pip3 install --upgrade {list_packages}', title='Installing requirements')

    print('Please, don\'t forget to make freeze! You can do it with command \'duty freeze\'')
