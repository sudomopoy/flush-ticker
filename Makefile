generate:
	buf generate
	sh make_inits.sh
	python3 modify_imports.py 
