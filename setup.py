from distutils.core import setup
setup(
    name='monit',
    description='Interface to the Monit system manager and monitor (http://mmonit.com/monit/)',
    version='0.5',
    author='Camilo Polymeris, Claudio Mignanti',
    author_email='cpolymeris@gmail.com, c.mignanti@gmail.com',
    url='https://github.com/claudyus/python-monit',
    py_modules=['monit'],
    requires=['requests']
    )
