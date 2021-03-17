#start to make list for average exon length
L = []
gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,159,81]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
#average length for every sigle exon 
for i in range(0,10):
  L.append(float(gene_lengths[i])/float(exon_counts[i]))

print(L)
#start box plots
import  numpy as np
import matplotlib.pyplot as plt
#Set parameters for box plots
plt.boxplot(L,
	    vert = True,
	    whis = 1.5,
	    meanline =True,
	    showbox = True,
	    showcaps = True,
	    showfliers = True,
	    notch = False,
            patch_artist= False,
            showmeans=True
	    )
#show it 
plt.show()

