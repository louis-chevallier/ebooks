TOOLS_=${TOOLS:-/mnt/hd1/tools}

#wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-x86_64.sh
MINICONDA=Miniconda3-latest-Linux-x86_64.sh
MINICONDA=Miniconda3-py38_4.12.0-Linux-x86_64.sh

function inred() {
    red=`tput setaf 1`
    green=`tput setaf 2`
    reset=`tput sgr0`
    bold=`tput bold`    # Select bold mode
    under=`tput smul`    # Select bold mode
    echo "${under}${bold}${red}$*${reset}"
    #red text ${green}green text${reset}"
}

function testXX() {
    inred en rouge
}

function myhome() {
    if [ -d '/home/wp02/' ] ; then
        local ret="home"
    else
        local ret="srv"
    fi
    echo $ret
}

function buildtheenv_orange() {

    # install driver
    # sudo apt purge "nvidia*" "libnvidia*"
    # sudo apt install nvidia-driver-510
    #

    DEST=${DESTINATION:-condaorange}
    PYTHON_VERSION_=${PYTHON_VERSION:-3.8}
    
    DD1=$( dirname ${BASH_SOURCE[0]}) 
    echo dd1 $DD1
    DD2=$(readlink -m $DD1)
    echo dd2 $DD2 dest= $DEST
    pwd
    DD=${DD2}
    source $DD/buildenv.sh
    ANA=${TOOLS_}/${DEST}
    CUDA_VERSION_=${CUDA_VERSION:-11.6}
    #CUDA_VERSION_=11.1

    printf python version ${PYTHON_VERSION_} "\n"

#    which python
    if [ 0"$1" == 0install ]; then
        echo a3
        set -vx
        rm -fr ${ANA}
        DIST=${TOOLS_}/${MINICONDA}
        SOURCE=${DIST}
        bash ${SOURCE} -p $ANA -b -f
        PATH=${ANA}/bin:${PATH} 
        which python
        which pip
        ls -l ${ANA}/bin/pip
        which pip
        python --version
        #conda update -y --prefix ${ANA}  anaconda
        conda update conda -y
        #conda install -y python=${PYTHON_VERSION_}
        which python
        conda install -y python==${PYTHON_VERSION_}
        python --version
        conda install -y pip
        pip install --upgrade pip
        pip install utillc
        
        conda install -y -c conda-forge numpy==1.22.3
        conda install -y scipy        
	if [ 1 == 1 ]; then
            conda install -y -c anaconda scikit-learn
            conda install -y matplotlib
            pip install opencv-python scikit-image  imageio plotly
            pip install loguru
            pip3 install PyQt5
            pip install psutil
            pip install utillc
            conda install -y sympy
            pip install webdriver-manager
            pip install selenium            
	fi
        set +vx
    else
        which python
        $*
    fi
    printf ${ANA}
    #cuda92
    PATH=${ANA}/bin:${PATH}

    echo a2
    which python
}

function test_version3() {
    source /mnt/hd2/users/louis/dev/git/orange/buildenv.sh
    # avec install ou run en params
    DESTINATION=condaorange buildtheenv $* 
 }

