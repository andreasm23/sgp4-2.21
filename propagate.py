#!/usr/bin/env python

from sgp4.api import Satrec, jday, days2mdhms
import sys
import yaml
import array
import datetime
import numpy as np

class bc:
    GRE = '\033[92m' #GREEN
    YEL = '\033[93m' #YELLOW
    RED = '\033[91m' #RED
    RES = '\033[0m' #RESET COLOR

def headtail_list(l,d,n):
  sys.stderr.write(f"{bc.GRE}Showing the first and last {n} entries of {d}:{bc.RES}\n")
  sys.stderr.write("\n".join(l[:n]))
  sys.stderr.write("\n".join(l[-n:]))

def array_fmt(a,fmt="%.12e"):
  l,r=a.shape
  return f"{fmt} "*r

def headtail_np(a,d,n,fmt="%.12e"):
  np.set_printoptions(precision=4,linewidth=180)
  sys.stderr.write(f"{bc.GRE}Showing the first and last {n} entries of {d}:{bc.RES}\n")
  sys.stderr.write('\n'.join([array_fmt(a,fmt)%tuple(row) for row in a[:n ,:]])+'\n')
  sys.stderr.write('\n'.join([array_fmt(a,fmt)%tuple(row) for row in a[-n:,:]])+'\n')
  np.set_printoptions()

def list_methods(o):
  for i in dir(o):
    if i[:1] != '_':
      try:
        a=getattr(o,i)
      except RuntimeError:
        pass
      else:
        sys.stderr.write(i)

# load configuration
with open('propagate.yml', 'r') as file:
  config = yaml.safe_load(file)
#inform user
if config['debug']:
  sys.stderr.write(f"{bc.GRE}Loaded configuration data:{bc.RES}\n")
  for key,value in config.items():
    sys.stderr.write ("{:>17} : {:}\n".format(key,value))

#load TLE from stdin
tle=[];
c=0;
if config['debug']:
  sys.stderr.write(f"{bc.RED}Waiting for TLE data from stdin...{bc.RES}\n")
for line in sys.stdin:
  c=c+1;
  if c>3:
    break
  tle.append(line.rstrip())
#inform user
if config['debug']:
  sys.stderr.write(f"{bc.GRE}Loaded TLE data:{bc.RES}\n")
  for i in tle:
    sys.stderr.write(f"{i}\n")

#load TLE to sgp4
sat = Satrec.twoline2rv(tle[1], tle[2])
if config['debug']:
  sys.stderr.write(f"{bc.GRE}SGP4 object shows:{bc.RES}\n")
  for i in config['sgp4_init_methods']:
    sys.stderr.write ("{:>20} : {:}\n".format(i,getattr(sat,i)))

#create array of dates
fr=np.arange(config['start'],config['stop']+config['step'],config['step'], dtype = float)/3600/24
n=fr.size
jd=sat.jdsatepoch+np.floor(fr)

#propagate orbit
e, r, v = sat.sgp4_array(jd, fr)

#enforce requested time domain format
if (config['time_domain']=="original"):
  orbit=np.concatenate((jd.reshape(n,1),fr.reshape(n,1),r*1e3,v*1e3),axis=1)
else:
  #these are time domain formats that result in simple scaling
  if (config['time_domain']=="days"):
    s=1;
  elif (config['time_domain']=="hours"):
    s=24;
  elif (config['time_domain']=="minutes"):
    s=60*24;
  elif (config['time_domain']=="seconds"):
    s=60*60*24;
  else:
    raise Exception(f"Cannot handle the following time format: {config['time_domain']}")
  #scale the time domain
  # orbit=np.concatenate((((jd+fr)*s-jd*s).reshape(n,1),r*1e3,v*1e3),axis=1)
  orbit=np.concatenate(((fr*s).reshape(n,1),r*1e3,v*1e3),axis=1)

#inform user
if config['debug']:
  headtail_np(orbit,'orbit',config['htlen'],config['float_fmt'])

#write orbit data to screen
if config['debug']:
  sys.stderr.write(f"{bc.GRE}Writing TLE to stdout:{bc.RES}\n")
print('\n'.join([array_fmt(orbit,config['float_fmt'])%tuple(row) for row in orbit]))





