import os

import re

with open('log_files/201811123025.log',encoding='utf-8') as f:

	count=0

	for line in f:

		if(re.split(',|：',line)[3]=='201811123025'):

			count+=1

print(count)





