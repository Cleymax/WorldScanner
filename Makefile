dist:
	python setup.py sdist

init:
	pip install -r requirements.txt

clean:
	rm ./dist -rf
	find ./ -type d -name '__pycache__' | xargs rm -r
	rm ./build -rf