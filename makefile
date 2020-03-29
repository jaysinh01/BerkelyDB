FILENAME: createIdx.py

reviews:reviewsort
	python3 createIdx.py reviews.txt rw.idx 0 ,

products:productsort
	python3 createIdx.py pterms_sorted.txt pt.idx 1 ,

rev:revsort
	python3 createIdx.py rterms_sorted.txt rt.idx 1 ,

scores:scoresort
	python3 createIdx.py scores_sorted.txt sc.idx 1 ,

all: reviews products rev scores

dfsdf:	sort -u -n -t, -k2,2 scores.txt > scores_sorted.txt

reviewsort:
	sort -u reviews.txt -o reviews.txt

productsort:
	sort -u pterms.txt -o pterms.txt
revsort:
	sort -u rterms.txt -o rterms.txt

scoresort:
	sort -u scores.txt -o scores.txt
