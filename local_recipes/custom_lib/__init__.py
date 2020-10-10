'''A dummy recipe to build my custom lib
'''
from pythonforandroid.recipe import CythonRecipe


class CustomLibRecipe(CythonRecipe):
    version = '1.0'
    name = 'custom_lib'
    depends = [('genericndkbuild', 'sdl2'), 'setuptools']
    site_package_name = 'custom_lib'


recipe = CustomLibRecipe()
