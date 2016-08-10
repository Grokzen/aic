from pkg_resources import iter_entry_points
import pdb; pdb.set_trace()
for entry_point in iter_entry_points(group='aic.modules', name=None):
    print(entry_point)
