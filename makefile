FILENAME: createIdx.py

reviews:reviewsort perlreviewsort
	db_load -T -t hash rw.idx < reviews_1.txt

perlreviewsort:
	perl break.pl < reviews.txt > reviews_1.txt

products:productsort perlproductsort
	db_load -c duplicates=1 -T -t btree pt.idx < pterms_1.txt

perlproductsort:
	perl break.pl < pterms.txt > pterms_1.txt

rev:revsort perlrevsort
	db_load -c duplicates=1 -T -t btree rt.idx < rterms_1.txt

perlrevsort:
	perl break.pl < rterms.txt > rterms_1.txt

scores:scoresort perlscoresort
	db_load -c duplicates=1 -T -t btree sc.idx < scores_1.txt

perlscoresort:
	perl break.pl < scores.txt > scores_1.txt

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

