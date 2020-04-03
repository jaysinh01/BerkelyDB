FILENAME: createIdx.py

reviews:reviewsort perlreviewsort
	db_load -T -t hash rw.idx < reviews.txt

perlreviewsort:
	perl break.pl < reviews.txt > reviews.txt

products:productsort perlproductsort
	db_load -c duplicates=1 -T -t btree pt.idx < pterms.txt

perlproductsort:
	perl break.pl < pterms.txt > pterms.txt

rev:revsort perlrevsort
	db_load -c duplicates=1 -T -t btree rt.idx < rterms.txt

perlrevsort:
	perl break.pl < rterms.txt > rterms.txt

scores:scoresort perlscoresort
	db_load -c duplicates=1 -T -t btree sc.idx < scores.txt

perlscoresort:
	perl break.pl < scores.txt > scores.txt

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

