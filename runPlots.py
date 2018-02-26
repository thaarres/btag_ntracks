#!/usr/bin/env python
import os, glob, sys
from commands import getoutput
import re
import datetime
import subprocess
import itertools

now = datetime.datetime.now()
timestamp =  now.strftime("%Y_%m_%d")

def split_seq(iterable, size):
    it = iter(iterable)
    item = list(itertools.islice(it, size))
    while item:
        yield item
        item = list(itertools.islice(it, size))
        
def getFileListDAS(dataset,instance="prod/phys03",run=-1):
	cmd='das_client --limit=0 --query="file dataset=%s instance=%s"'%(dataset,instance)
	cmd_out = getoutput( cmd )
	tmpList = cmd_out.split(os.linesep)
	files = []
	for l in tmpList:
	   if l.find(".root") != -1:
	      files.append(l)        
	return files 
   
def runPlotter(f,name):
  infile = "root://cms-xrd-global.cern.ch/"+f
  cmd = 'python plotter.py %s %s'%(infile,name)
  print cmd
  os.system(cmd)
  return 1

if __name__ == "__main__":
  if len(sys.argv) > 1:
    if sys.argv[1].find("M2000")!=-1:		patterns = ["/RSGravitonToWWToQQQQ_M-2000_TuneCUETP8M1_14TeV-pythia8/PhaseIITDRSpring17DR-PU200_91X_upgrade2023_realistic_v3-v3/GEN-SIM-RECO"]
    print 'Location of input files', patterns
  else:
    print "No input sample given, please pas a valid DAS name!"
    exit(0)

  for pattern in patterns:
    files = getFileListDAS(pattern)
    name = pattern.split("/")[1].replace("/","")
    # filelists = list(split_seq(files,10))
    for i,f in enumerate(files):
      print "Running on file %i = %s"%(i,f)
      runPlotter(f,name)
      if i==0: break
