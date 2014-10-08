__author__ = 'kshk'
#!/use/bin/env python

import jenkins
import sys
import json

def testJenkins():
    j = jenkins.Jenkins("https://jenkins_url","login","password")
    jobs = j.get_jobs()
    for i in jobs:
        #print i['name']
        if (i['name'] == 'JOB1'):
            if i['color'] == 'red':
                print "Failed"
            elif i['color'] == 'blue':
                print "Build :- Passed"
            else:
                print "Unkown"
        if (i['name'] == 'JOB2'):
            if i['color'] == 'red':
                print "Failed"
            elif i['color'] == 'blue':
                print "Build :- Passed"
            else:
                print "Unkown"
        if (i['name'] == 'JOB3'):
            if i['color'] == 'red':
                print "Failed"
            elif i['color'] == 'blue':
                print "Build :- Passed"
            else:
                print "Unkown"


def main():
    testJenkins()

if __name__ == "__main__":
    main()
