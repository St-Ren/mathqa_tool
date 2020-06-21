from unicodedata import numeric
import json
def sen2numre(sen):
	sen = sen.replace(' , ',',').replace(',',' , ')
	l = sen.split()
	n = []
	for i in range(len(l)):
		try:
			_ = float(l[i])
			n.append(float(l[i]))
			l[i] = 'n{}'.format(len(n) - 1)
		except:
			continue
	return ' '.join(l),n
def main():
	for split in ['dev','test','train']:
		lines = open(split + '.pro', encoding='utf-8').readlines()
		new_file = open('new/' + split + '.pro','w', encoding='utf-8')
		list_file = open(split + '1.nlist','w', encoding='utf-8')
		for line in lines:
			l,n = sen2numre(line)
			new_file.write(l+'\n')
			list_file.write(json.dumps(n) + '\n')
if __name__ == "__main__":
	main()