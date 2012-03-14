# ---
# I should live here:
# /usr/lib/yum-plugins/multiverse.py

import re
from yum import config
from yum.plugins import TYPE_CORE

requires_api_version = '2.4'
plugin_type = TYPE_CORE

def config_hook(conduit):
    config.RepoConf.multiversions = config.ListOption()

def postreposetup_hook(conduit):
     base = conduit._base
     installonly = []
     for repo in conduit.getRepos().listEnabled():
         patterns = [pkg.replace("*", '.*') for pkg in repo.multiversions]
         if(len(patterns)):
             regex = re.compile("^(" + ( ")|(".join(patterns) ) + ")$")
             pkgs = [pkg.name for pkg in base.pkgSack.returnPackages(repo.id) if regex.match(pkg.name)]
             installonly.extend(pkgs)
     installonly = list(set(installonly))
     #print installonly
     base.conf.installonlypkgs.extend(installonly)
     #print base.conf.installonlypkgs
