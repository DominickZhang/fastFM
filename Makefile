PYTHON ?= python

all:
	( cd fastFM-core ; $(MAKE) lib )
	$(PYTHON) setup.py build_ext --inplace

.PHONY : clean
clean:
	( cd fastFM-core ; $(MAKE) clean )
	cd fastFM2/
	rm -f *.so
	rm -rf build/
	rm -f fastFM2/ffm.c
