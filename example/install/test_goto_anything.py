
import os
import random

folder_name = ['plounce', 'anodynic', 'melton', 'rhinophyma', 'unburly', 'trenchmore', 'impulsivity', 'preindebted', 'raceway', 'highheartedness', 'Anglogaea', 'overcleanness']

for name in folder_name:
    try:
        os.mkdir(name)
    except:
        print("folder %s exist" % name)
        continue

    for i in range(random.randint(1, 5)):
        fname = name + str(i)
        path = os.path.join(name, fname)

        # os.system('touch %s' % path)
        with open(path, "w") as fp:
            fp.close()
    