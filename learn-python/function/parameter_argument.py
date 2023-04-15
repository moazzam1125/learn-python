''' Parameters & Arguments of function '''

## Positional


def fname(pname, aname):
    ''' using function of function '''
    print(aname + " to " + pname)

fname(pname='Paramter', aname='Argument')

# Default value

def dname(dnum = 125):
    ''' set Defaults '''
    print(str(dnum) + " is default")

dname()

## Arbitrary


def arb_info(fname, **other):
    ''' Arbitrary function '''
    repo = {
        'name': fname,
    }
    for key, value in other.items():
        repo[key] = value
    return repo

repo_info = arb_info(
    'learn-python',
    cname = 'Playground',
    type = 'cheat sheet'
)
print(repo_info)