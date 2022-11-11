all:
	make install
	make decompress

decompress:
	python scripts/decompress-data.py

install:
	pip install -r ./requirements.txt
