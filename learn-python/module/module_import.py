''' Importing module '''

# Import entire module

import module_main
module_main.mtest('entire module')

# Import apart of module

from module_main import mtest   # (*) for all
mtest('function of module')

# Alias

from module_main import mtest as mt
mt('Alias')