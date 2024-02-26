import os,re
import numpy as np
wd = 'D:\\git\\resume\\'
with open(os.path.join(os.path.split(os.path.abspath(__file__))[0],'resume.md'),'r') as file:
  inpstr = file.read()
inpstr = re.sub('<!--.*-->','',inpstr)
inpstr = re.sub('&#9;\*.*\*','',inpstr)
lst = np.unique(re.split(' |\n|#|\*|\.|,|:|\(|\)',inpstr))
lst = [a.lower() for a in lst if a]
