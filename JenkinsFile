node { // The "node" directive tells Jenkins to run commands on the same slave.
 	PYENV_HOME=$WORKSPACE/.pyenv/

	# Delete previously built virtualenv
	if [ -d $PYENV_HOME ]; then
	    rm -rf $PYENV_HOME
	fi

    checkout scm

    stage 'test'
    
	# Create virtualenv and install necessary packages
	virtualenv --no-site-packages $PYENV_HOME
	. $PYENV_HOME/bin/activate
	pip install --quiet pytest
	pip install --quiet pytest-cov
	pip install --quiet pylint

	py.test --junitxml=report.xml --cov-report xml --cov=. tests
	pylint -f parseable . | tee pylint.out
}