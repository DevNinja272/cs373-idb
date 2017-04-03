FILES :=                              \
    models.html                        \
    IDB1.log                          \
    app/app.py                        \
    app/models.py                     \
    app/tests.py 					  \
    .gitignore                        \
    apiary.apib                       \
    UML.pdf                           \
    requirements.txt                  \
    README.md                         \

ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(CI), true)                # Travis CI
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Docker
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3.5
    PIP      := pip3
    PYLINT   := pylint3
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
endif


.pylintrc:
	$(PYLINT) --disable=locally-disabled --reports=no --generate-rcfile > $@


models.html: app/models.py
	$(PYDOC) -w models

IDB1.log:
	git log > IDB1.log

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

config:
	git config -l

format:
	$(AUTOPEP8) -i app/app.py
	$(AUTOPEP8) -i app/models.py
	$(AUTOPEP8) -i app/tests.py

scrub:
	make clean
	rm -f  models.html
	rm -f  IDB1.log

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

runtests:
	$(PYTHON) app/tests.py

runserver:
	$(PYTHON) app/app.py

reqs:
	pip install -r requirements.txt

test: models.html IDB1.log check
