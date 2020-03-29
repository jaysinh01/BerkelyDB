reviews:
	python3 $(FILENAME) reviews.txt 0 rw.idx ,

products:
	python3 $(FILENAME) pterms_sorted.txt 1 pt.idx ,

reviews:
	python3 $(FILENAME) rterms_sorted.txt 1 rt.idx ,

scores:
	python3 $(FILENAME) scores_sorted.txt 1 sc.idx ,

all: products reviews scores

