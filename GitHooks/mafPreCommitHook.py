#####################################################
# mafPreCommitHook.py
# author: Alberto Losi
#####################################################

import mafGitHookUtility
import mafSourcesCommentsRule
import sys

addedFiles = mafGitHookUtility.getModifiedFileNames()
print "Executing pre commit hook:"

#####################################################
# check comment
print "Checking comments:"
for f in addedFiles:
    if mafGitHookUtility.fileIsACxx(f):
        if mafSourcesCommentsRule.check(f) == False:
            print "Error! comments rule not satisfied for %s" % f
            print "Commit aborted!"
            sys.exit(1)
#####################################################

print "OK. Committing..."
sys.exit(0)