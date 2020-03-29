#%%
import shlex

from lib import examine_func

examine_func.assert_functions(shlex.split)


# %%
# Will raise exception
shlex.split("set foo 'bar ")

# %%
