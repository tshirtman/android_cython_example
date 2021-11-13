'''A dummy recipe to build my custom lib
'''
from pythonforandroid.recipe import CythonRecipe, IncludedFilesBehaviour


class CustomLibRecipe(IncludedFilesBehaviour, CythonRecipe):
    version = '1.0'
    name = 'custom_lib'
    depends = [('genericndkbuild', 'sdl2'), 'setuptools']
    site_package_name = 'custom_lib'
    url = None
    src_filename = '../../lib/custom_lib'


recipe = CustomLibRecipe()
